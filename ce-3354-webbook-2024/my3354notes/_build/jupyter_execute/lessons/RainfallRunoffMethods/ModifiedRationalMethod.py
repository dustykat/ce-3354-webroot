#!/usr/bin/env python
# coding: utf-8

# # Modified Rational Method
# 
# ## Background
# The rational method is used to estimate peak discharges for sizing drainage structures, such as storm drains and culverts. The modified rational method (MRM) is an extension of the rational method to produce simple runoff hydrographs. The MRM is often called the rational hydrograph method. Application of the MRM produces a runoff hydrograph and runoff volume in contrast to application of the rational method, which produces only a peak design discharge (Qp). 
# 
# The hydrograph developed from application of the MRM is a special case of the unit hydrograph method and is sometimes termed the modified rational unit hydrograph (MRUH); as a unit hydrograph, the MRUH can be applied to nonuniform rainfall distributions. Furthermore, the MRUH can be used on watersheds with drainage areas in excess of the typical limit for application of the rational method. Application of the MRUH method involves two steps: (1) determination of rainfall loss using rational method concept, that is, use of the runoff coefficient, and (2) determination of the MRUH using drainage area (A) and time of concentration (Tc) as input parameters, in addition to applying the procedure of unit hydrograph convolution.  
# 
# Tc and runoff coefficients, C, can be estimated by a variety of methods.
# 
# ## Readings
# 1. [Smith, A. A. and K.-B. Lee. 1984. "The Rational Method Revisited." Canadian Journal of Civil Engineering 11, 854–862.](http://54.243.252.9/ce-3354-webroot/ce-3354-webroot-2024/3-Readings/smith_and_lee_1984.pdf)
# 
# 1. [A Osman Akan. 2002. Modified rational method for sizing infiltration structures. Canadian Journal of Civil Engineering. 29(4): 539-542. https://doi.org/10.1139/l02-038](http://54.243.252.9/ce-3354-webroot/ce-3354-webroot-2024/3-Readings/Akan_2002.pdf)
# 
# 2. [Fang, X., Thompson, D.B., Cleveland, T.G., Pradhan, D.E., Malla, R. 2008. "Time of Concentration Estimated Using Watershed Parameters Determined by Automated and Manual Methods" American Society of Civil Engineers, Journal of Irrigation and Drainage Engineering, Vol. 134, No 2, pp 202-211.](http://54.243.262.9/ce-3354-webroot/ce-3354-webroot-2024/3-Readings/fang_2008_1.pdf)
# 
# 2. [ Cleveland, T.G., Thompson, D.B., and Fang,X. 2011. "Use of the Rational and Modified Rational Method for Hydraulic Design." Texas Department of Transportation, Research Report 0-6070-1](http://54.243.252.9/ce-3354-webroot/ce-3354-webroot-2024/3-Readings/techmrt_0-6070-1.pdf)
# 
# 3. [Dhakal, N., Fang, X., Asquith, W.H., Cleveland, T.G., Thompson, D.B. 2012 "Rate-based Estimation of the Runoff Coefficients for Selected Watersheds in Texas." American Society of Civil Engineers, Journal of Hydrologic Engineering doi:10.1061/(ASCE)HE. 1943-5584.0000753 (November 29, 2012) ASCE_Hydrology_1297](http://54.243.252.9/about-me-webroot/about-me/MyWebPapers/journal_papers/ASCE-JHE-1297/Rate-Based-C-Texas.pdf)
# 
# 4. [Dhakal, N., Fang, X., Cleveland, T.G., Thompson, D.B.; Asquith, W.H., Marzen, L.J. 2012 "Estimation of Volumetric Runoff Coefficients for Texas Watersheds Using Land-Use and Rainfall-Runoff Data" American Society of Civil Engineers, Journal of Irrigation and Drainage Engineering, Vol. 138, No 1, pp 43-54.](http://54.243.252.9/ce-3354-webroot/ce-3354-webroot-2024/3-Readings/Volumetric_C_Nirajan2012.pdf)
# 
# 5. [Dhakal, N., Fang, X., Cleveland, T.G., Thompson, D.B. 2014 "Modified Rational Unit Hydrograph Method and Applications" Institute of Civil Engineers, Journal of Water Management, WATER-D-13-00032R2](http://54.243.252.9/ce-3354-webroot/ce-3354-webroot-2024/3-Readings/MRM_WAMA1300032h.pdf)
# 
# 
# 
# 

# ## Modified Rational Method Hydrograph Generator
# 
# This script performs discrete convolution to generate a direct runoff hydrograph from a hyetograph for a drainage area using the modified rational method unit-hydrograph approach (cite).
# 
# The direct runoff hydrograph is computed using a convolution integral:
# 
# $$ Q(t) = \int_{0}^{\tau}{p(t)u(t-\tau)d\tau} $$
# 
# where
# - $p(t)$ is the excess rainfall hyetograph
# - $u(t)$ is the drainage area response kernel (a unit hydrograph)
# - $Q(t)$ is the direct runoff hydrograph
# 
# The response kernel for the modified rational method is
# 
# $$ u(t) = \frac{A}{T_c}~\text{for}~t \le T_c$$
# 
# where
# - $A$ is the contributing drainage area
# - $T_c$ is the time of concentration
# 
# The excess rainfall hyetograph is obtained from the precipitation input signal as
# 
# $$ p(t)=C \times P(t) $$
# 
# where
# - $C$ is the rational equation runoff coefficient
# - $P(t)$ is a rainfall hyetograph (design storm)
# 
# The example script below illustrates the calculations for an NRCS Type 2 design storm, the other design storms are included and a simple change in storm type in the `interp1d(minutes, type2, kind='linear')` function call (i.e. change type2 to another type in the program). Alternatively the analyst could supply any hyetograph they choose, but would have to fuss a bit with the array lengths.
# 
# The script has several prototype functions:
# > `Convolve` is the discrete convolution integrator <br>
# > `kernel` is the $u(t)$ kernel function above <br>
# > `ModRat` is the function that actually computes the time-shifted response kernel, scales inputs and outputs to produce dimensional outputs
# 
# After these prototype functions is a block that generates an input excess rainfall hyetograph. The next block is the input block, the actual function call to `ModRat`, some mass balance summary calculations.
# Finally the plotting section prepares graphical output, reports the inputs, summary values in the chart title, and then charts the input hyetograph (an excess hyetograph, losses are already removed), and the direct runoff hydrograph.

# In[1]:


###### INPUT BLOCK ############################################
PT = 6.96 # Total storm depth in inches         #####INPUT VALUE
area= 181 # Drainage area in acres           #####INPUT VALUE
C = 0.65 # Runoff coefficient                  #####INPUT VALUE
Tc = 6.0 # Time of concentration in minutes   #####INPUT VALUE
hyetType = 'type2'                              #####INPUT VALUE
# Design storm options are: 'type1','type1A','type2','type3','user'
# need to manually insert user hyetograph in the Hydrograph Engine section
###############################################################
# Convolution Engine
#############################################
def Convolve(duration, excitation, kernel):
    response = [0 for i in range(duration)] # populate response vector with zeros
  # response = direct runoff hydrograph (unscaled)
  # excitation = input rate in length per time
  # kernel = unit response
    for i in range(duration):
        for j in range(i,duration-1):
            response[j]=excitation[i]*kernel[(j-i)+1]+response[j]
    return(response)

#############################################
# Kernel Engine
#############################################
def kernel(time,area,tc):
# area = drainage area (in acres)
# tc = time of concentration (in minutes)
    if time > tc:
        kernel=0.0
    else:
        kernel=area/tc
    return(kernel)

##############################################
# Modified Rational Convolution 
#############################################
def ModRat(area,runoff_coefficient,precipitation,time,Tc):
    excess=[0 for i in range(len(precipitation))]
    flow=[0 for i in range(len(precipitation))]
# Generate Excess Rainfall
    for i in range(len(precipitation)):
        excess[i]=runoff_coefficient*precipitation[i]
# Generate Unitgraph for Rational Method
#  unitgraph<-(sapply(time,kernel,area,Tc))/sum(sapply(time,kernel,area,Tc));
    unitgraph=[0 for i in range(len(precipitation))] # start with zeroes
    accumulator=0.0
    for i in range(len(precipitation)):
        unitgraph[i] = kernel(time[i],area,Tc)
        accumulator=accumulator+unitgraph[i]
# now rescale each by the accumulator
    for i in range(len(precipitation)):
        unitgraph[i] = unitgraph[i]/accumulator
# Apply discrete convolution     
    flow=Convolve(len(excess),excess,unitgraph)
    flow = [area*(i) for i in flow]
    return(flow)

###############################################
# Hyetograph Engine
###############################################
# SCS Type Curves
hour = [0,2,4,6,7,8,8.5,9,9.5,9.75,10,10.5,11,11.5,11.75,12,12.5,13.0,13.6,14,16,20,24,48]
minutes = [i*60 for i in hour]
type1 = [0,0.035,0.076,0.125,0.156,0.194,0.219,0.254,0.303,0.362,0.515,0.583,0.624,0.654,0.669,0.682,0.706,0.727,0.748,0.767,0.83,0.926,1,1]
type1A = [0,0.05,0.116,0.206,0.268,0.425,0.48,0.52,0.55,0.564,0.577,0.601,0.624,0.645,0.655,0.664,0.683,0.701,0.719,0.736,0.8,0.906,1,1]
type2 = [0,0.022,0.048,0.08,0.098,0.12,0.133,0.147,0.163,0.172,0.181,0.204,0.235,0.283,0.357,0.663,0.735,0.772,0.799,0.82,0.88,0.952,1,1]
type3 = [0,0.02,0.043,0.072,0.089,0.115,0.13,0.148,0.167,0.178,0.189,0.216,0.25,0.298,0.339,0.5,0.702,0.751,0.785,0.811,0.886,0.957,1,1]
usertime =  [0,7,     8,     9,9.3333, 10, 24, 48]
userdepth = [0,0,0.4285,0.8571,   1.0,1.0,1.0,1.0]

from scipy.interpolate import interp1d
if hyetType == 'type1':
    f = interp1d(minutes, type1, kind='linear')  #Design storm options are: 'type1','type1A','type2','type3' 
elif hyetType == 'type1A':
    f = interp1d(minutes, type1A, kind='linear')  #Design storm options are: 'type1','type1A','type2','type3' 
elif hyetType == 'type2':
    f = interp1d(minutes, type2, kind='linear')  #Design storm options are: 'type1','type1A','type2','type3' 
elif hyetType == 'type3':
    f = interp1d(minutes, type3, kind='linear')  #Design storm options are: 'type1','type1A','type2','type3' 
elif hyetType == 'user':
    minutes = [i*60 for i in usertime]
    f = interp1d(minutes, userdepth, kind='linear')  #Design storm options are: 'type1','type1A','type2','type3' 
#
t24 = [float(i) for i in range(2881)] # time in minutes
d24 = f(t24) # cumulative proportional depths - difference to get rates
d24 =[PT*i for i in d24] # scale to total depth
r24 = [0 for i in range(len(d24))] # create destination
r24[0] = d24[0]
for i in range(1, len(d24)):
    r24[i] = d24[i] - d24[i-1] # this will be inches/minute
    r24[i]=r24[i]*60 # inches per hour

#############################################
# Build direct runoff hydrograph
#############################################
result = ModRat(area,C,r24,t24,Tc) 
## Compute summary values
peakQ = max(result)
## Mass balances
totalQ = sum(result)*60/43560 # area under red curve == volume of discharge
totalR = C*d24[-1]*(1/12)*area
#adjust = totalR/totalQ
#totalQ=totalQ*adjust
massE = (totalR-totalQ)/totalR

#############################################
# Graphics engine
#############################################
xlow = -0
xhigh = 2880
import matplotlib.pyplot as plt # the python plotting library
# Plot script adapted from 
plottitle ='Direct Runoff Hydrograph by Modified Rational Method Discrete Convolution\n \n'
if hyetType == 'type1':
    plottitle = plottitle + 'Hyetograph Type: ' + 'SCS Type 1 Design Storm\n' 
elif hyetType == 'type1A':
    plottitle = plottitle + 'Hyetograph Type: ' + 'SCS Type 1A Design Storm\n' 
elif hyetType == 'type2':
    plottitle = plottitle + 'Hyetograph Type: ' + 'SCS Type 2 Design Storm\n' 
elif hyetType == 'type3':
    plottitle = plottitle + 'Hyetograph Type: ' + 'SCS Type 3 Design Storm\n' 
elif hyetType == 'user':
    plottitle = plottitle + 'Hyetograph Type: ' + 'User Supplied Design Storm\n'
plottitle = plottitle + 'Hydrograph Type: ' + 'Modified Rational\n'
plottitle = plottitle + 'Contributing Drainage Area: ' + repr(area) + ' acres\n'
plottitle = plottitle + 'Rainfall Storm Depth: ' + repr(round(PT,2)) + ' inches\n'
plottitle = plottitle + 'Runoff Coefficient: ' + repr(C) +'\n'
plottitle = plottitle + 'Time of Concentration: ' + repr(Tc) + ' minutes\n'
plottitle = plottitle + 'Peak Discharge: ' + repr(round(peakQ,1)) + ' cfs\n'
plottitle = plottitle + 'Total Discharge (Area under red curve): ' + repr(round(totalQ,1)) + ' acre-feet\n'
plottitle = plottitle + 'Total Excess Rain (Area under blue curve): ' + repr(round(totalR,1)) + ' acre-feet\n'
plottitle = plottitle + 'Mass Balance Relative Error : ' + repr(round(100*massE,2)) + ' percent\n'

# Create a figure and axis object
fig, ax1 = plt.subplots(figsize = (10,10))
# Create the first plot on the left y-axis
ax1.step(t24, r24, color='blue', label='Intensity')
ax1.set_xlabel('Time (minutes)')
ax1.set_ylabel('Intensity (in/hr)')
# Create a second axis object for the right y-axis
ax2 = ax1.twinx()
# Create the second plot on the right y-axis
ax2.step(t24, result, color='red', label='Discharge')
ax2.set_ylabel('Discharge (cfs)')
# Add legend and show the plot
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.xlim([xlow,xhigh])
plt.grid(b=True, which='major', axis='y')
plt.title(plottitle)
plt.show()


# In[ ]:




