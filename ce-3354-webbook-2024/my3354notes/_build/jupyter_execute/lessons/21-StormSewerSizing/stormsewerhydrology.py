#!/usr/bin/env python
# coding: utf-8

# # 21. Storm Sewer Hydrology
# 
# :::{admonition} Course Website
# [Link to Course Website](http://54.243.252.9/ce-3354-webroot/)
# :::
# 
# 

# ## Readings
# 
# 1. [Gupta, R.S., 2017. Hydrology and Hydraulic Systems, pp. 46-59](https://www.waveland.com/browse.php?t=384)
# 
# 1. [Chow, V.T., Maidment,D.M., and Mays, L.W. (1998) Applied Hydrology, McGraw Hill, pp. 444-493](http://54.243.252.9/ce-3354-webroot/3-Readings/CMM1988/) 
# 
# 1. [Cleveland, T. G. (2017) *Surface Water Hydrology Notes (Channel Routing) to accompany CE-3354*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/1-Lectures-2017/Lecture18.pdf)
# 
# 1. [Routing (Hydrology) Wikipedia ](https://en.wikipedia.org/wiki/Routing_(hydrology))
# 
# 1. [Routing (Information) Wikipedia](https://en.wikipedia.org/wiki/Routing_Information_Protocol)

# ## Videos
# 
# 1. [Hydrograph Routing (YouTube)](https://www.youtube.com/watch?v=nzRG2uIMaTY)
# 2. [Reservoir Routing (YouTube)](https://www.youtube.com/watch?v=1mdtq7iJ_74&t=248s)
# 3. [Hydrologic Channel Routing (YouTube)](https://www.youtube.com/watch?v=HLSTZuEi5gg)
# 4. [Channel Routing (NCEES Training Video)](https://www.youtube.com/watch?v=Eb0BoxlxcQw&list=PLGCZ9gpx8QdsoFj-3qWS_7iq61WE4Yy9d)
# 5. [Reservoir Routing (NCEES Training Video)](https://www.youtube.com/watch?v=lkUEFtjQH6s&list=PLGCZ9gpx8QdsoFj-3qWS_7iq61WE4Yy9d)
# 6. [Flash Flood Videos (YouTube)](https://www.youtube.com/watch?v=u0-FLuwWhf4)
# 7. [Flash Flood near Sedona Az. (YouTube)](https://www.youtube.com/watch?v=Ipo0kwQQcgQ)

# ## Outline
# 
# 1. 

# ## A Rational Method for Storm Sewer Conduit Sizing 
# 
# The Rational Method is a widely used, straightforward approach for sizing storm sewer conduits and estimating stormwater runoff, particularly in urban drainage design. It is used to obtain initial estimates of conduit diameters, flowlines, and hydraulic grade lines for storm sewer systems. Although more advanced hydrologic models are available, the Rational Method remains popular for preliminary design due to its simplicity and ease of application, especially when dealing with small catchments.
# Overview of the Rational Method
# 
# The Rational Method estimates peak runoff from a given watershed using the formula:
# 
# $Q=CIA$
# 
# Where:
# 
# $Q$ = Peak runoff rate (cubic feet per second or cfs),
# $C$ = Runoff coefficient (dimensionless), representing the portion of rainfall that becomes surface runoff,
# $I$ = Rainfall intensity (inches per hour), determined based on the design storm and time of concentration for the watershed,
# $A$ = Drainage area (acres).
# 
# ### Steps for Storm Sewer Conduit Sizing Using the Rational Method
# 
# 1. Determine the Design Storm Event:
#     Identify the design storm return period (e.g., 5-year, 10-year, or 100-year storm) based on local regulations or standards. This helps establish the rainfall intensity (II) for the design.
# 
# 2. Estimate the Time of Concentration:
#     The time of concentration ($T_C$) is the time it takes for runoff to travel from the most distant point of the catchment to the outlet or point of interest. Several empirical methods (e.g., Kirpich’s equation) can be used to calculate this value.
# 
# 3. Select the Runoff Coefficient (C):
#     The runoff coefficient is chosen based on the land cover within the drainage area. For example, impervious surfaces (like pavement) will have a higher CC value (around 0.9), while pervious surfaces (like grassland) will have a lower value (around 0.2). Mixed land uses are weighted to determine an appropriate CC value for the entire catchment.
# 
# 4. Calculate Peak Runoff (Q):
#     Using the Rational Method equation, the peak runoff QQ is calculated by multiplying the runoff coefficient CC, the rainfall intensity II, and the drainage area AA.
# 
# 5. Conduit Sizing:
#     Once the peak runoff $Q_P$ is determined, the required diameter of the storm sewer conduit can be estimated using Manning’s equation for open channel flow, assuming the conduit is flowing full or partially full. Manning’s equation is:<br><br>
# $Q=\frac{1.49}{n}AR^{2/3}S_0^{1/2}$ <br><br>
# Where:
# - $Q$ = Discharge (cfs),
# - $n$ = Manning's roughness coefficient (dimensionless),
# - $A$ = Cross-sectional area of flow (square feet),
# - $R$ = Hydraulic radius (feet),
# - $S_0$ = Slope of the conduit (ft/ft).
# 
#     The required pipe diameter can be determined iteratively by solving Manning’s equation for AA and matching it with the calculated peak runoff $Q$.
# 
# 6. Hydraulic Grade Line (HGL) and Flowline:
#     The Hydraulic Grade Line (HGL) represents the level to which water would rise in open vertical tubes attached to the conduit. It is used to assess the system’s capacity to convey flow without excessive pressure buildup. The flowline refers to the bottom elevation of the pipe at various points along the system. These elevations are crucial for ensuring gravity flow and preventing backflow within the system.
# 
#     To approximate the HGL by hand, designers often check that the conduit slope and size provide sufficient capacity by comparing the HGL with the energy grade line (EGL), which accounts for both the potential and kinetic energy within the system. By adjusting the pipe size or slope, the designer ensures the HGL stays within acceptable bounds.
# 
# ### Advantages of the Rational Method
# 
# - Simplicity: The Rational Method is straightforward and can be applied manually without requiring complex computer simulations, making it useful for small drainage areas.
# - Preliminary Design: It provides a good starting point for conduit sizing, helping designers quickly estimate pipe diameters, slopes, and flowlines before conducting more detailed hydraulic analyses.
# - Applicability for Urban Settings: The method is particularly suited for urban environments with impervious surfaces, where runoff behavior is more predictable.
# 
# ### Limitations of the Rational Method
# 
# - Small Catchment Limitation: The Rational Method is typically recommended for small watersheds (less than 200 acres) because it assumes uniform rainfall distribution and runoff response, which may not hold in larger or more complex watersheds.
# - Peak Flow Only: It estimates only the peak runoff rate and does not provide information about the full runoff hydrograph (i.e., the variation of flow over time).
# - Constant Runoff Coefficient: The method assumes a constant runoff coefficient CC, which may vary during a storm event due to factors like soil saturation or changing land cover conditions.
# 
# ### Summary
# 
# The Rational Method provides a practical, by-hand approach for obtaining initial estimates of conduit diameters, flowlines, and hydraulic grade lines for storm sewer systems. It serves as a preliminary design tool, ensuring that designers can evaluate the capacity and size of storm sewer conduits before engaging in more sophisticated analyses, making it an essential tool in urban stormwater management.

# ## Conduit Design
# 
# Conduits are structures that convey water from one location to another.
# - Pipes
# - Culverts
# - Open Channels
# 
# Design task is to select size, material, and slope
# - STORM SEWER – USUALLY DESIRE TO OPERATE WITH FREE SURFACE (AS AN OPEN CHANNEL)
# - SANITARY SEWER – SIMILAR USUALLY WANT A FREE SURFACE
# - SIZE (DIAMETER) IS DICTATED BY
#   - FLOW REQUIRED
#   - BURIAL DEPTH RELATIVE TO DROP AVAILABLE
#   
# A GOOD PRELIMINARY DESIGN CAN BE OBTAINED USING A COMBINATION OF THE RATIONAL EQUATION AND MANNING’S EQUATION
# - DONE WITHOUT REGARD TO DOWNSTREAM BOUNDARY CONDITIONS 
# - NEEDS TO BE CHECKED USING A HYDRAULIC MODEL (LIKE SWMM)

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# ## End of File

# In[ ]:




