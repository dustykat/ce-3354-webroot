#!/usr/bin/env python
# coding: utf-8

# # 4. Precipitation
# 
# Precipitation is the water which falls from the atmosphere in either liquid or solid form.

# :::{admonition} Course Website
# [link to webster](http://54.243.252.9/)
# :::
# 
# 

# ## Readings
# 
# 1. [Chow, V.T., Maidment,D.M., and Mays, L.W. (1998) Applied Hydrology, McGraw Hill, (Read pages 26 to 31; 416 to 423)](http://54.243.252.9/ce-3354-webroot/3-Readings/CMM1988/) 
# 
# 2. [McCuen, R.H., Johnson, P.A., and Ragan, R.M. (2002) Highway Hydrology. HDS-2 (2ed) FHWA-NHI-02-001 (Read pages 3-1 to 3-5; 4-86 to 4-89; 5-1 to 5-8; 5-16 to 5-17)](http://54.243.252.9/ce-3354-webroot/3-Readings/FHWAHighwayHydrology/FHWA-NHI-02-001.pdf)
# 
# 3. [Texas Hydraulic Design Manual (2014-1) Texas Department of Transportation. (2014) Hydraulic Design Manual (Read pages 4-1 to 4-5; 4-31 to 4-35)](http://54.243.252.9/ce-3354-webroot/3-Readings/TXDOT-HYDM-2014/txdot-hdm-2014.pdf)
# 
# 4. [Linear Theory of Hydrologic Systems Dooge, J.C. I. (1973) Linear Theory of Hydrologic Systems. USDA ARS Technical Bulletin No. 1468. (Read pages 127 to 147)](http://54.243.252.9/ce-3354-webroot/3-Readings/LS1973/linear-systems-hydrology-dooge.pdf)
# 
# 5. [Cleveland, T. G. (2015) *Engineering Hydrology Notes to Accompany CE 3354 (Hand-written)*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/ce3354book/lessons/lesson04/precipitation-notes.pdf)
# 
# 6. [Cleveland, T. G. (2017) *Engineering Hydrology Notes to Accompany CE 3354 (Discrete Data Analysis; Risk Based Design; Regression Equations)*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/1-Lectures-2017/Lecture05.pdf)
# 
# 7. [Cleveland, T. G. (2017) *Engineering Hydrology Notes to Accompany CE 3354 (Probability Estimation Modeling)*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/1-Lectures-2017/Lecture06.pdf)
# 
# 8. [Cleveland, T. G. (2017) *Engineering Hydrology Notes to Accompany CE 3354 (Point Precipitation; Design Storms)*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/1-Lectures-2017/Lecture08.pdf)
# 
# 9. [Cleveland, T.G., and Thompson, D.B., 2008. ``Rainfall Intensity in Design.'' 87-th Annual Transportation Research Board Meeting, January 14-18, Washington, D.C.](http://54.243.252.9/ce-3354-webroot/3-Readings/TRB-2008-Paper/TRB_2008_IntensityDesign_Rev2.pdf)
# 
# 5. [Williams-Sether, T., Asquith, W.H., Thompson, D.B., Cleveland, T.G., and X. Fang. 2004. ``Empirical, Dimensionless, Cumulative-Rainfall Hyetographs for Texas.'' U.S.Geological Survey Scientific Investigations Report 2004-5075, 138p. ](http://54.243.252.9/ce-3354-webroot/3-Readings/EmpiricalHyetographs/sir2004-5075.pdf)
# 
# 7. [HEC-19 (old)](https://www.fhwa.dot.gov/engineering/hydraulics/pubs/hec/hec19.pdf)
# 
# 7. [HEC-19 (Updated)](https://www.fhwa.dot.gov/engineering/hydraulics/pubs/hif23050.pdf)
# 
# 8. [McCabe, K. (2022) "Rain, sleet or snow?" Royal Meterological Society](https://www.rmets.org/metmatters/rain-sleet-or-snow)

# ## Videos

# ## Outline
# - Forms of Precipitation 
#   - Weather Systems for Precipitation 
# - Measurement of Precipitation 
#   - Raingauge Networks
# - Data Preparation 
#   - Presentation of Rainfall Data
#   - Mean Precipitation Over An Area 
# - Depth-Area-Duration Relationships
#   - Frequency of Point Rainfall
#   - Intensity/Depth-Duration-Frequency Relationship
# - Probable Maximum Precipitation (PMP) 
# - World’s Greatest Observed Rainfalls

# ## Missing Data Replacement Techniques
# 
# In the estimation of missing data from a raingauge station, performance of a group of
# neighbouring stations including the one with missing data are considered. A comparison
# of the recordings of these stations are made by using their normal rainfall as standard
# of comparison. The normal rainfall is the average value of rainfall at a particular date,
# month or year over a specified 30-year period. The 30-year normal is recomputed every
# decade. Thus, the term normal annual precipitation at a station A means the average annual precipitation at station A based on a specified 30-year of record. Insertion of
# missing data to a station record must be done sparingly. If too many data are estimated,
# the quality of the total data set may be diluted due to interpolation. sometimes, if too
# many gaps exist in a record, it may be worthwhile to neglect that station than to have
# a station record with too much of interpolated data. A WMO guideline states that not
# more than 5 to 10% of a record should have interpolated data.
# 
# 
# **Missing Data Estimation Procedure**<br>
# *Problem Statement*<br>
# Given the annual precipitation values $P_1, P_2, P_3,\dots ,P_m$ at neighbouring $M$ stations $1, 2, 3, \dots, M$ respectively, estimate the missing annual precipitation $P_x$ at station $X$ not included in the above $M$ stations. The normal annual precipitations $N_1, N_2,\dots,N_i, \dots$ at each of the above ($M+1$) stations, including station $X$, are known.
# 
# *Procedure*<br>
# - If the normal annual precipitations at various stations are within about 10\% of the normal annual precipitation at station X then the station-average method (arithmetic mean) is sufficient to estimate $P_x$. Thus,
# $P_x = \frac{1}{M}(P_1 + P_2 + \dots + P_M)$
# - If the normal annual precipitations vary considerably then $P_x$ is estimated by weighing the precipitation at various stations by the ratios of normal annual precipitations. This method, known as the normal ratio method, gives $P_x$ as
# $P_x = \frac{N_x}{M}(\frac{P_1}{N_1} + \frac{P_2}{N_2} + \dots + \frac{P_M}{N_M})$

# ## Example
# The **normal** annual rainfall at stations A, B, C and D in a basin are 80.97, 67.59, 76.28 and 92.01 cm respectively. In 1985, the station D was inoperative and the stations A, B and C recorded annual precipitation of 91.11, 72.23 and 79.89 cm respectively. Estimate
# the rainfall at station D in that year
# 
# > Using ENGR 1330 methods, a rudimentary python program could be:

# In[1]:


# Missing Precipitation Estimation
def station_average(precip_known):
    ''' precip_known is known stations data as a list'''
    how_many = len(precip_known)
    station_average = sum(precip_known)/float(how_many)
    return station_average
def normal_ratio(precip_known,normal_all):
    ''' precip_known is known stations data as a list
        normal_all is all stations normal rainfall depths
        missing station is assumed last element in normal_all list'''
    how_many = len(precip_known)  
    nr = [0 for i in range(how_many)]
    for i in range(how_many):
        nr[i]=precip_known[i]/normal_all[i]
    normal_average = (sum(nr)/float(how_many))*normal_all[-1]
    return normal_average


# In[2]:


# Input Data
precip_known = [91.11, 72.23, 79.89]
normal_all = [80.97, 67.59, 76.28, 92.01] 
# Find differences for normal values
diff = [0 for i in range(len(normal_all)-1)]
for i in range(len(diff)):
    diff[i]=normal_all[-1]-normal_all[i] # raw difference assume last entry is missing station
percent_max = 100.0*max(diff)/normal_all[-1]
if percent_max <=10.0:
    missing_pee = station_average(precip_known)
    print("Use Station Average Method")
    print("Missing Depth : ",round(missing_pee,2)," cm")
else:
    missing_pee = normal_ratio(precip_known,normal_all)
    print("Use Normal Ratio Method")
    print("Missing Depth : ",round(missing_pee,2)," cm")


# ### Readings
# 1. [PAULHUS, J. L. H. , and M. A. KOHLER. "INTERPOLATION OF MISSING PRECIPITATION RECORDS". Monthly Weather Review 80.8 (1952): 129-133.](http://54.243.252.9/ce-5361-webroot/3-Readings/NormalRatioMethod/mwr-080-08-0129.pdf)
# 2. [Missing Rainfall Data Replacement Techniques](http://54.243.252.9/ce-5361-webroot/3-Readings/MissingRainfallData/MissingRainfallData.pdf)

# 

# In[ ]:




