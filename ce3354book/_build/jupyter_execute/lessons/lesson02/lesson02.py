#!/usr/bin/env python
# coding: utf-8

# # Hydrologic Cycle
# 
# The water, or hydrologic, cycle describes the journey of water as water molecules make their way from the Earth’s surface to the atmosphere and back again, in some cases to below the surface. This gigantic system, powered by energy from the Sun, is a continuous exchange of moisture between the oceans, the atmosphere, and the land.
# A typical diagram depicting the hydrologic cycle is shown below.
# 
# ![](hydrologic_cycle.png)
# 
# The driving force for the cycle is solar energy that provides the energy to vaporize liquid water that then rises into clouds, moves onshore, and rains (or snow, sleet, $\dots$.  and other forms of <strong>precipitation</strong>)
# A portion of the rain becomes runoff, another portion returns to the atmosphere as evaporation, another portion infiltrates into the ground and becomes groundwater.
# 
# 

# ## Water Budget Definition
# The water budget, or <strong>hydrologic balance</strong> is simply the expression of the conservation of mass in hydrologic terms for a hydrologic system.  
# Generally it is expressed as a rate (or volume) balance.
# The hydrologic equation is the fundamental tool in hydrology to describe amounts of water in storage in different compartments at different scales.  
# 
# The equation expressed in “words” is
# 
# Rate of inflow - Rate of outflow =  Rate of change of storage + Rate of internal mass generation.
# 
# Symbolically it is exrepssed as:
# 
# $$ \frac{dI}{dt} - \frac{dO}{dt} = \frac{dS}{dt} + \frac{dG}{dt}$$
# 
# where
# 
# $I$ is inflow volume, $O$ is outflow volume, $S$ is storage volume (i.e. within a watershed), and $G$ is generated volume.
# $G$ is generally zero, but is included to be consistent with the balance equations you have learned elsewhere (i.e. environmental engineering, chemistry, $\dots$)

# ## Water Budget Example 1
# Consider the following problem statement:
# 
# ![](BetswyCoedPrstate.png)
# 
# One way to answer the questions is to decompose the problem into a simpler construct, usually by sketching a diagram as shown below:
# 
# ![](BetswyCoedSketch.png)
# 
# Now we can simply assign the terms to the appropriate parts of the water balance equation and solve for unknown components such as:
# 
# ![](BetswyCoedSolve1.png)
# 
# For more utility we can use our Computational Thinking (ENGR-1330) skills and write a simple script to generalize the results and help with unit conversions

# In[1]:


# Water Budget Script - Example in WebBook
P = 254 # millimeters of rainfall 
ET = 85 # millimeters of evapotranspiration
I = 20 # millimeters of infiltration
DeltaS = 0 # millimeters of storage change

R = P - ET - I + DeltaS

print("Runoff = ",round(R,3),' watershed millimeters')


# Now to convert to other units as requested, we simply apply conversions as:

# In[2]:


def mm2m(mm):
    # convert mm into meters
    mm2m = mm/1000.0 # mm should be a float
    return(mm2m)

def sqkm2sqm(sqkm):
    # convert square kilometers into square meters
    sqkm2sqm = sqkm * 1.0e06 # sqkm should be a float
    return(sqkm2sqm)

def cum2liter(cum):
    # convert cubic meters into liters
    cum2liter = cum*1000.0 # cum should be a float
    return(cum2liter)

# now express result in useful units
area = 65 # area in sq. kilometers

WholeWatershedRunoff = mm2m(R)*sqkm2sqm(area)

print("Runoff = ",round(WholeWatershedRunoff,3),' cubic meters')

print("Runoff = ",round(cum2liter(WholeWatershedRunoff),3),' liters')


# Now estimate largest population this hydrology could support

# In[3]:


# Population supported at 160 L/day
litersPerDayPerPerson = 160
litersPer2months = litersPerDayPerPerson*2*30
# Assume all Runoff is Run through kidneys and colons
maxPeople = cum2liter(WholeWatershedRunoff)/litersPer2months
print("Maximum Population = ",maxPeople," if rainfall is firm")


# ---
# ## Water Budget Example 2
# 
# Consider the following problem statement:
# 
# At a particular time the storage in a river reach is 55.3 acre-ft.  At that instant, the inflow to the  reach is 375 cfs and the outflow is 563 cfs.  Two hours later, the inflow the inflow to the  reach is 600 cfs and the outflow is 675 cfs.
# 
# Estimate:
# - The change in storage over 2 hours.
# - The reach storage after 2 hours.
# 
# Solution:
# 
# ### Sketch the Situation
# 
# ![](river-reaches.png)
# 
# ### Governing Principles
# 
# Apply the water balance model:
# 
# $$ \frac{dI}{dt} - \frac{dO}{dt} = \frac{dS}{dt} + \frac{dG}{dt}$$
# 
# ### Analysis/Solution
# 
# Observe that there is no internal mass generated, so that term will vanish.  Discharge is changing over time, so we will have to choose how to cope with that, typically one chooses arithmetic means
# 
# $$ \frac{dI}{dt} = \frac{375+600}{2} = 487.5~\text{cfs} $$
# 
# $$ \frac{dO}{dt} = \frac{563+675}{2} = 619~\text{cfs} $$
# 
# Now we substitute into the equation and solve for the storage rate of change
# 
# $$ 487.5 - 619 = \frac{dS}{dt} = -131.5~\text{cfs}$$  
# 
# Observe this is a rate!  We will need to "integrate" to recover actual change
# 
# Now recover the estimated change in storage, and new storage value from the rate
# 
# $$ \Delta S = \frac{dS}{dt} \Delta t = -131.5~\text{cfs} \cdot 2~\text{hrs} = -263~\text{cfs-hr}$$  
# 
# A little unit conversion
# 
# $$ -263~\text{cfs-hr} \cdot \frac{3600~\text{sec}}{1~\text{hr}} \cdot \frac{1~\text{acre-ft}}{43,560~\text{ft}^3} = -21.73~\text{acre-ft}$$
# 
# Then apply definition of $\frac{dS}{dt} $ as
# 
# $$\frac{dS}{dt}~\approx~\frac{S_2-S_0}{\Delta t}$$
# 
# So the new storage volume is
# 
# $$S_2=S_0+\frac{dS}{dt} \Delta t= S_0 + \Delta S= 55.30 - 21.73 = 33.57~\text{acre-ft}$$
# 
# Now we can summarize the results
# 
# |Value|Amount|Unit|
# |:---|---:|:---|
# |$\Delta S$|-263|cfs-hr|
# |$S_2$|33.57|acre-ft|

# ## References
# 
# cite pages of textbook
# 
# links to other readings 
# 
# 1. [Hydrologic cycle (USGS)](https://www.usgs.gov/special-topics/water-science-school/science/fundamentals-water-cycle).
# 
# 2. [Hydrologic Cycle (NSF) - YouTube Video](https://www.youtube.com/watch?v=al-do-HGuIk)

# 

# 

# 
