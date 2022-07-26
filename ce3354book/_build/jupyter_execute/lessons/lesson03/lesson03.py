#!/usr/bin/env python
# coding: utf-8

# 

# # Watersheds
# 
# Some definitions of a watershed include:
# 
# - Topographic area that collects and discharges surface streamflow through one outlet or mouth (pour point)
# - The area on the surface of the Earth that drains to a specific location
# - In groundwater a similar concept is called a groundwater basin – only the boundaries can move depending on relative rates of recharge and discharge 
# 
# The topographic definition omits that there could be subsurface sewer systems that can cross topographic boundaries.   
# It’s a big deal in urban areas.
# 
# [insert some images]

# ## Watershed Delineation
# 
# Identifies the boundaries of our hydrologic unit / area of study.
# - Need to interpret topographic maps (or DEM/DTM) to construct the boundary
# - Read “How to ...” on server (check the reading list below!)
# 
# ### By-hand steps to delineate a watershed
# 
# - Locate a pour point/point of interest
# - Superimpose a grid over the study area
#   – used to assign average elevations for demarking the boundary
# - Trace/outline the main path of the stream that you want to examine that flows to the pour point
# - Trace all perennial or influential tributaries
# - Locate the lowest point/outlet of the main stem and work uphill to identify the ridges and hill tops that divide the water from flowing into separate watersheds
#  - When in doubt, consider, where a drop of rain would go on different parts of study region
# 
# #### Locate a pour point/point of interest
# 
# ![](pourpoint.png)
# 
# #### Superimpose a grid over the study area
# 
# Used to assign average elevations for demarking the boundary, so the grid needs to be small enough to capture meaningful elevation change, but big enough that you can complete the task in your lifetime.
# 
# ![](gridoverlay.png)
# 
# #### Estimate Cell Elevations
# 
# Estimate the average elevations in each cell. Trace/outline the main path of the stream that you want to examine that flows to the pour point.  Trace all perennial or influential tributaries
# Locate the lowest point/outlet of the main stem and work uphill to identify the ridges and hill tops that divide the water from flowing into separate watersheds
# 
# ![](estimatecellelev.png)
# 
# #### Draw Boundary
# 
# Once the high points are identified, connect them and draw the watershed boundary.  You can now make measurements to determine area, lengths, and slopes.
# 
# ![](drawboundary.png)
# 
# ### Automated
# 
# Automated delineation essentially replicates these steps in a computer program. ArcGIS, QGIS and similar tools can perform a raster-based cell-by-cell flow accumulation calculation and when the "upstream" cell count gets smaller than some threshold, the program declares that to be a high point.  And draws the boundary.  
# 
# The automated tools are pretty good; fast; and less prone to interpretation - but you have to have the software and know how to use it.  
# 
# Manual methods and automated methods produce comparable results, but for large areas the automated methods are much faster. [Heitmuller et. al. 2006](http://54.243.252.9/ce-3354-webroot/3-Readings/SW-Geographer-2006/SW-Geographer-2006.pdf)
# 
# ### Stream Stats Tool
# 
# An on-line tool for use in many states is [StreamStats](https://streamstats.usgs.gov/ss/).  A good demonstration is to select a stream near Lawton Oklahoma and generate a watershed report.

# ## Watershed Metrics
# 
# ### Measuring Area
# ### Measuring Length(s) 
# ### Estimating Slope(s)

# 

# ## References
# 
# 1. [Cleveland, T. G. (2020) *Surface Water Hydrology Notes (Watersheds) to accompany CE-5361*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/1-Lectures-2020/lesson04/Lesson04.pdf)
# 2. [Cleveland, T. G. (2017) *Engineering Hydrology Notes (Hydrologic Data; Watershed Delineation) to accompany CE-3354*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/1-Lectures-2017/Lecture03.pdf)
# 3. [Cleveland, T. G. (2017) *Engineering Hydrology Notes (Watershed Metrics) to accompany CE-3354*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/1-Lectures-2017/Lecture04.pdf)
# 2. [Florida Delineation Training Watershed (png)](http://54.243.252.9/ce-3354-webroot/1-Lectures-2017/Florida-Training-Watershed.png) Right-Click "Save As..."
# 3. [Texas Delineation Training Watershed (png)](ce-3354-webroot/1-Lectures-2017/Texas-Training-Watershed.png) Right-Click "Save As..."
# 4. [Watersheds - McCuen](http://54.243.252.9/ce-3354-webroot/3-Readings/McCuen-Watersheds/McCuen-Watersheds.pdf)
# 5. [How to Delineate a Watershed](http://54.243.252.9/ce-3354-webroot/3-Readings/NewHampshire-Watersheds/Topowatershed.pdf)
# 6. [Numerical Planimetry](http://54.243.252.9/ce-3354-webroot/3-Readings/NumericalPlanimetry/)
# 7. [How To Measure Path](http://54.243.252.9/ce-3354-webroot/3-Readings/HowToMeasurePath/HowToMeasurePath.pdf)
# 8. [How to use Topographic Maps](http://54.243.252.9/ce-3354-webroot/3-Readings/UsingTopographicMaps/Pages%20from%20USAF-Survival-Manual-644.pdf)

# In[ ]:




