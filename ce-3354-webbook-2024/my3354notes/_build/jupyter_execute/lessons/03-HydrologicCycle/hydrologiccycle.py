#!/usr/bin/env python
# coding: utf-8

# # 3. Hydrologic Cycle
# 
# :::{admonition} Course Website
# [Link to Course Website](http://54.243.252.9/ce-3354-webroot/)
# :::
# 
# 

# ---
# ## Readings
# 1. [Gupta, R.S., 2017. Hydrology and Hydraulic Systems, pp 39-46](https://www.waveland.com/browse.php?t=384)
# 
# 2. [Hydrologic cycle (USGS)](https://www.usgs.gov/special-topics/water-science-school/science/fundamentals-water-cycle).
# 
# 4. [Cleveland, T.G. (2017) Engineering Hydrology *Lecture Notes from 2017*](http://54/243.252.9/ce-3354-webroot/1-Lectures-2017/Lecture02.pdf)
# 
# 1. [Ojha, Chandra & Berndtsson, R. & Bhunya, P.K.. (2008). Engineering Hydrology. Chapter 1 (Local Copy from https://www.researchgate.net/publication/264895381_Engineering_hydrology)](http://54.243.252.9/ce-3354-webroot/3-Readings/EngineeringHydrology/EngineeringHydrology-11-33.pdf)  
# 
# 1. [Chow, V.T., Maidment, D.R., Mays, L.W., 1988, Applied Hydrology:  New York, McGraw-Hill. **pp. 1-12** ](http://54.243.252.9/ce-3354-webroot/3-Readings/CMM1988/Applied%20Hydrology%20VT%20Chow%201988.pdf) 
# 
# 2. Brutsaert,  W.  2005.  Hydrology  :   An  Introduction  (8th  printing),  Cambridge  University Press. NewYork.
# 
# 3. [Dooge, J.C.I. 1973. Linear Theory of Hydrologic Systems. ARS Technical Bulletin No. 1468.US Department of Agriculture, Washington, D.C. **pp. 1-40**](http://54.243.252.9/ce-3354-webroot/3-Readings/LS1973/linear-systems-hydrology-dooge.pdf) 
# 
# 4. [Richard H. McCuen, Peggy A. Johnson, Robert M. Ragan, 2002. Highway Hydrology; Hydraulic  Design  Series  Number  2,  Second  Edition.  Federal  Highway  Administration,  National Highway Institute, 4600 North Fairfax Drive, Suite 800, Arlington, Virginia 22203. **pp. 1-1 to 1-9**](http://54.243.252.9/ce-3354-webroot/3-Readings/FHWAHighwayHydrology/FHWA-NHI-02-001.pdf) 
# 
# 5. [Definitions  from various sources](http://54.243.252.9/ce-3354-webroot/3-Readings/HydrologyDefinitions/hydrology-define.pdf)
# 
# 6. [Wisler, C.O, and Brater, E.F. 1949. "Hydrology" John Wiley and Sons, New York **pp. 1-14**](http://54.243.252.9/ce-3354-webroot/3-Readings/OlderHydrologyDescription/reading-definition-hydrology.pdf) 
# 
# 7. [McCuen XXXX. Hydrologic Analysis and Design ... **pp. 2-12** ](http://54.243.252.9/ce-3354-webroot/3-Readings/McCuen-WaterBudget/mccuen-reading-water-budget.pdf)
# 
# 8. [Heath, R.C., 1983. Basic ground-waterhydrology: U.S. Geological Survey Water-SupplyPaper 2220, **pp. 1-5**](http://54.243.252.9/ce-3354-webroot/3-Readings/USGS-WSP2020-GroundwaterHydrology/usgs-wsp-2020.pdf) 
# 
# 9. [Viessman,W., Knapp, J.W., Lewis, G. L., and Harbaugh, T.E. 1977. "Groundwater Hydrology – Chapter 8" in *Introduction to Hydrology* 2ed. IEP Publishers, New York, **pp. 291-342**](http://54.243.252.9/ce-3354-webroot/3-Readings/Groundwater-Viessman/GroundwaterHydrology.pdf) 
# 
# 10. [Wisler, C.O, and Brater, E.F. 1949. "Hydrology" John Wiley and Sons, New York **pp. 198-272**](http://54.243.252.9/ce-3354-webroot/3-Readings/Groundwater-Wisler&Brater/Groundwater-Wisler.pdf) 
# 

# ## Videos
# 
# 3. [Hydrologic Cycle (NSF) - YouTube Video](https://www.youtube.com/watch?v=al-do-HGuIk)
# 2. [Hydrologic Cycle (YouTube)](https://www.youtube.com/watch?v=Eok9VYfesOk&list=PLXLUpwDRCVsSSeyKWT03rLb6X9DbqHsSX&index=1)
# 3. [What is Hydrology? (YouTube)](https://www.youtube.com/watch?v=AlwMqDUKV1U)
# 4. [Hydrologic Water Balance (YouTube)](https://www.youtube.com/watch?v=7fdwXS9q2uo)
# 5. [Earth's Water Budget (YouTube)](https://www.youtube.com/watch?v=2oKYXKKf28g)
# 
# 
# 3. [Runoff (YouTube)](https://www.youtube.com/watch?v=SjWEtgVV-l8&list=PLXLUpwDRCVsSSeyKWT03rLb6X9DbqHsSX&index=5)  MOVE TO CORRECT LESSON

# ## Outline
# - Surface and Groundwater Concepts
# - Hydrologic Cycle
# - Water Budget

# ---
# # Surface and Groundwater Hydrology Concepts
# 
# ## What is hydrology?
# - Study of the occurrence, circulation, storage, and distribution of surface and groundwater on the Earth.
# - Engineering hydrology is the quantification of amounts of water at various locations (spatially) as a function of time (temporally) for surface water applications.
# 
# ## What is a watershed (catchment)?
# Here are a couple of definitions of watersheds.
# 
# - Topographic area that collects and discharges surface streamflow through one outlet or mouth (pour point)
# - The area on the surface of the Earth that drains to a specific location
# - In groundwater a similar concept is called a groundwater basin – only the boundaries can move depending on relative rates of recharge and discharge 
# 
# The topographic definition omits that there could be subsurface sewer systems that can cross topographic boundaries.   It’s a big deal in urban areas.
# 
# ## What is a hydrologic system?
# A hydrologic system is just a collection of parts that interact.   
#  
# - A hydrologic system is simply the collection of connected components that form the <strong>hydrologic cycle</strong>
# - These components can be grouped into subsystems, treated separately, and the results combined according to interactions between the subsystems (CMM pg 5) 
# 
# Like in fluid mechanics, the system has boundaries (the control volume) and fluxes into/out of the boundaries.   
# The entire planet is usually considered a closed system (hydrologically) and only the energy fluxes cross the boundary.   
# At more practical scales (parking lot) the mass fluxes matter a lot.  
# 
# <!-- ### What is the hydrologic cycle?
# Here is a typical diagram depicting the hydrologic cycle.  
# 
# ![](hydrologic_cycle.png)
# 
# The driving force for the cycle (not shown) is solar energy that provides the energy to vaporize liquid water that then rises into clouds, moves onshore, and rains (or snow, sleet, $\dots$.  and other forms of <strong>precipitation</strong>)
# A portion of the rain becomes runoff, another portion returns to the atmosphere as evaporation, another portion infiltrates into the ground and becomes groundwater.
# 
# The surface water system would be the part of the diagram that lies above the plane defined by the ocean and infiltration line.
# The subsurface system is the part that is below this plane.
# 
# Expressed as a simple system diagram it would be depicted in the figure below
# 
# ![](system_diagram.png) -->

# ## Hydrologic Cycle
# 
# The water, or hydrologic, cycle describes the journey of water as water molecules make their way from the Earth’s surface to the atmosphere and back again, in some cases to below the surface. This gigantic system, powered by energy from the Sun, is a continuous exchange of moisture between the oceans, the atmosphere, and the land.
# A typical diagram depicting the hydrologic cycle is shown below.
# 
# ![](hydrologic_cycle.png)
# 
# The driving force for the cycle is solar energy that provides the energy to vaporize liquid water that then rises into clouds, moves onshore, and rains (or snow, sleet, $\dots$.  and other forms of <strong>precipitation</strong>)
# A portion of the rain becomes runoff, another portion returns to the atmosphere as evaporation, another portion infiltrates into the ground and becomes groundwater.
# 
# A more detailed accounting of the precipitation is as follows:
# 
# 1. A portion known as interception is retained on buildings, vegetation, and other surfaces that eventually evaporates - the remaining quantity is called **effective precipitation**
# 
# :::{note}
# Excess precipitation is a similar concept.  When discussing rainfall-runoff processes using some model (i.e. unit hydrograph methods), the quantity that becomes runoff is called excess precipitation.  The terms are frequently used interchangeably.
# :::
# 
# 2. Some of the effective precipitation also evaporates directly.
# 3. Another portion of effective precipitation **infiltrates** into the ground - a portion of infiltrated water returns to the atmosphere via transpiration, the remainder either percolates deeper into the ground or is incorporated in the vegetative biomass.
# 4. The water that percolates deeper into the ground becomes **recharge** to the groundwater system, and may appear at some point as **baseflow** in streams.
# 5. If the precipitation exceeds the combined evaporation and infiltration puddles form in small depressions on the land surface - this is called depression storage.
# 6. After the depressions are filled they join and a continuous film of water can begin to flow over the surface to a stream channel.  This portion that can flow is called the **excess precipitation** (see the note above), and the flow is called the **direct runoff**.
# 7. Runoff occurs when the film of water begins to move - water in this film is said to be in **detention storage**, and evaporation occurs from this compartment too. When precipitation ceases, the water in detention storage eventually joins the stream channel.
# 8. The destination of all streams is open bodies of water such as lakes, seas, and oceans which are subject to substantial evaporation.
# 9. The evaporation and tanspiration from all these sources combine and carry moisture back into the atmosphere which condenses and repeats the cycle.
# 

# ---
# ## Hydrologic Balance 
# 
# ### Water Budget
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

# ### Surface Hydrologic System
# 
# Here is the surface water system broken into its own sub-system.
# 
# ![](surface_system_diagram.png)
# 
# Notice the dashed line is the boundary – exactly like a control volume in fluids.
# 
# ### Surface Water Budget
# 
# From the surface water system diagram, appropriate budget components are:
# 
# - Inflows:  Rainfall; Surface water from outside boundary, recharge from Groundwater.
# - Outflows: Evapotranspiration; Surface water leaving boundary; Infiltration to groundwater.
# - Storage:  Water levels in lakes, rivers, ponds within the boundary; water stored on leaves and other surfaces.

# ### Sub-surface Hydrologic System
# 
# Here is the sub-surface water system broken into its own sub-system.
# 
# ![](subsurface_system_diagram.png)
# 
# Notice the dashed line is the boundary – exactly like a control volume in fluids.
# 
# ### Sub-surface Water Budget
# 
# From the sub-surface water system diagram, appropriate budget components are:
# 
# - Inflows:  Groundwater flow from outside boundary; Recharge from surface system (via infiltration)
# - Outflows: Groundwater flow out of the boundary; Discharge (pumping; springs) to surface system
# - Storage:  Water levels in aquifers within the boundary

# ### Combined Hydrologic System
# Here are the two systems “combined.”
# Communication is by the two shaded paths on the figure. 
# 
# ![](combined_system_diagram.png)
# 
# Loss from the surface system becomes gain to the ground system.
# Loss from the ground system becomes gain to the surface system.

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
# 
# If we wish an ability to repeat such computations a lot (maybe we own the reach and want to charge our customers for water use) we could apply ENGR-1330 methods as below to explore different inflow and outflow conditions

# In[4]:


# prototype function
def newS(t0,t1,I0,I1,O0,O1,S0):
    Ibar = 0.5*(I0 + I1)
    Obar = 0.5*(O0 + O1)
    dsdt = Ibar - Obar
    dsdt = dsdt*3600/43560 # convert to correct units
    deltat = t1-t0
    DS   = dsdt*deltat
    newS   = S0+DS
    return(newS)
# input values
t0 = 0 # hrs
t1 = 2 # hrs
I0 = 375 # cfs
I1 = 600 # cfs
O0 = 563 # cfs
O1 = 675 # cfs
S0 = 55.3 # acre-ft
# echo inputs
print("Begin Time",t0," hours")
print("End Time",t1," hours")
print("Inflow at Begin Time",I0," cfs")
print("Inflow at End Time",I1," cfs")
print("Outflow at Begin Time",O0," cfs")
print("Outflow at End Time",O1," cfs")
print("Storage at Begin Time",S0," acre-feet")
S1   = newS(t0,t1,I0,I1,O0,O1,S0) # get new storage
# output results
print("Storage at End Time",round(S1,2)," acre-feet")
