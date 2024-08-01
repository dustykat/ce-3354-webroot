#!/usr/bin/env python
# coding: utf-8

# # 5. Watersheds

# :::{admonition} Course Website
# [link to course webhost](http://54.243.252.9/)
# :::
# 
# 

# ## Readings
# 
# 1. [Baraka, M. 2024, Watershed Delineation in QGIS: A Summary Guide](http://54.243.252.9/ce-5361-webroot/3-Readings/Hydrology_GIS_part1.pdf)
# 1. [Brutsaert, W., 2005, Hydrology: An Introduction. Cambridge University Press](https://www.amazon.com/Hydrology-Introduction-Wilfried-Brutsaert/dp/0521824796/ref=sr_1_1?crid=26239UVBUDNRC&keywords=hydrology+an+introduction+brusehart&qid=1697843874&sprefix=hydrology+an+introduction+brusehart%2Caps%2C84&sr=8-1)
# 2. [Chow, V.T., Maidment, D.R., Mays, L.W., 1988, Applied Hydrology.  New York, McGraw-Hill. ](http://54.243.252.9/ce-5361-webroot/3-Readings/01CMM1988/Applied%20Hydrology%20VT%20Chow%201988.pdf) 
# 1. [Watersheds - McCuen](http://54.243.252.9/ce-3354-webroot/3-Readings/McCuen-Watersheds/McCuen-Watersheds.pdf)
# 2. [How to Delineate a Watershed](http://54.243.252.9/ce-3354-webroot/3-Readings/NewHampshire-Watersheds/Topowatershed.pdf)
# 3. [How To Measure Path](http://54.243.252.9/ce-3354-webroot/3-Readings/HowToMeasurePath/HowToMeasurePath.pdf)
# 6. [Numerical Planimetry](http://54.243.252.9/ce-3354-webroot/3-Readings/NumericalPlanimetry/)
# 4. [How to Interpret Topographic Maps](http://54.243.252.9/ce-3354-webroot/3-Readings/UsingTopographicMaps/Pages%20from%20USAF-Survival-Manual-644.pdf)
# 5. [Cleveland, T. G. (2020) *Surface Water Hydrology Notes (Watersheds) to accompany CE-5361*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/1-Lectures-2020/lesson04/Lesson04.pdf)
# 6. [Cleveland, T. G. (2017) *Engineering Hydrology Notes (Hydrologic Data; Watershed Delineation) to accompany CE-3354*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/1-Lectures-2017/Lecture03.pdf)
# 7. [Cleveland, T. G. (2017) *Engineering Hydrology Notes (Watershed Metrics) to accompany CE-3354*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/ce-3354-webbook-2024/my3354notes/lessons/05-Watersheds/Lesson04.pdf)
# 8. [Florida Delineation Training Watershed (png)](http://54.243.252.9/ce-3354-webroot/1-Lectures-2017/Florida-Training-Watershed.png) Right-Click "Save As..."
# 9. [Texas Delineation Training Watershed (png)](http://54.243.252.9/ce-3354-webroot/1-Lectures-2017/Texas-Training-Watershed.png) Right-Click "Save As..."
# 
# <hr>
# 

# ## Videos
# 
# 1. [What is a Watershed? (YouTube)](https://www.youtube.com/watch?v=QOrVotzBNto)
# 2. [What is a Watershed?-Illustrated (YouTube)](https://www.youtube.com/watch?v=w58XwzVcBFM)
# 3. [Why Watersheds Matter (YouTube)](https://www.youtube.com/watch?v=Om-eJBt9WvQ)
# 4. [Watershed Delineation Example (YouTube)](https://www.youtube.com/watch?v=ajF0DsuuY4k)
# 5. [Manual Watershed Delineation (USGS)](https://www.youtube.com/watch?v=RxO2814piio)
# 6. [Watershed Delineation using ArcGIS (YouTube)](https://www.youtube.com/watch?v=v3Ajg6W8Rj8)
# 7. [Watershed Delineation using qGIS (YouTube)](https://www.youtube.com/watch?v=2fvy9xtAHc4)
# 8. [How to Delineate a Watershed in qGIS (YouTube)](https://www.youtube.com/watch?v=CE7zZCkFbg4)
# 9. [Watershed Delineation and Metrics](https://www.youtube.com/watch?v=qzKS8n8RrdE)
# 10. [Measuring Area](https://www.youtube.com/watch?v=pDFystIDxn0)
# 13. [Watershed Characteristics](https://www.youtube.com/watch?v=wSvFrX48JOo)
# 11. [Manual Delineation](https://www.youtube.com/watch?v=cZBKrc6_B-E)
# 12. [Delineate Hardin Branch Watershed in QGIS (ES-2 Solution)](https://youtu.be/e1AbKqlHaow)
# 
# 

# ## Outline
# 
# 1. What are watersheds?
# 2. Delineation Concepts
#   1. By-hand (obsolete practice)
#   2. Using GIS tools (current practice)
# 3. Watershed metrics
#   1. Area
#   2. Slope
#   3. Main Channel metrics
#   4. Land use and vegetative cover types

# ## What are Watersheds?
# 
# A watershed is the area of land that drains all the streams and rainfall to a common outlet such as the outflow of a reservoir, mouth of a bay, or any point along a stream channel (this outlet is called a pour-point in GIS-speak). The term “watershed” is often used interchangeably with “drainage basin,” which may make the concept easier to visualize. 
# 
# :::{note}
# A common outlet implies that the various discharges have concentrated into a a definable conduit (as opposed to sheet or overland distributed flow).  The distributed flows are part of the watershed, but at times make engineering analysis at smaller scales challenging as no single control point exists.
# :::
# 
# A watershed can encompass a small area of land that drains into a trickling creek. It can encompass multiple states in the Midwest, all draining into the Mississippi River. Or it can encompass multiple countries draining into the Atlantic Ocean. No matter where you are standing or sitting right now, you are in a watershed. 
# 
# Water is constantly in motion, be it via ocean currents, precipitation, or slowly moving through underground aquifers. Any given watershed is part of the larger whole of our global water supply.
# 
# Smaller watersheds can make up larger watersheds. The Mississippi River has many tributaries (each of which has its own watershed), and in turn empties into the Gulf of Mexico, which connects to the Atlantic Ocean. The U.S. Geological Survey delineates our nation’s watersheds as “Hydrologic Units,” which are assigned hydrologic unit codes. These can range in scale  from expansive water resource regions covering millions of square miles down to tiny local tributary systems. There are 90,000 hydrologic unit codes  designated nationwide. 

# Some more compact definitions of a watershed include:
# 
# - Topographic area that collects and discharges surface streamflow through one outlet or mouth (pour point)
# - The area on the surface of the Earth that drains to a specific location
# - In groundwater a similar concept is called a groundwater basin – only the boundaries can move depending on relative rates of recharge and discharge 
# 
# The topographic definition omits that there could be subsurface sewer systems that can cross topographic boundaries.   
# It’s a big deal in urban areas.
# 
# Consider the artist rendering of a watershed
# 
# ![](watershed.png)
# 
# Large watersheds are comprised of smaller interconnected watersheds, thus in the rendering watershed B is a part of watershed A.
# 

# ## Delineation Concepts
# 
# Watershed delineation is a fundamental process in hydrology and environmental science that involves defining the boundaries of a drainage area or catchment. It identifies the geographic area from which all precipitation and surface runoff flow into a single outlet, typically a river, stream, or lake.
# 
# This analytical method is typically employed:
# 
# 1. By-hand and/or semi-automated using digital maps (obsolete, but viable for small areas)
# 2. Fully-automated using digital elevation data and geographic information systems (GIS) (current practice)
# 
# In all the cases above the goal is to trace the flow of water and determine the contributing area to a specific point of interest. 
# 
# Watershed delineation plays a crucial role in various applications, including flood management, water resource planning, and environmental conservation, by providing a spatial framework to understand and manage water-related processes within a defined geographic region.
# 

# # Delineation (by Hand)
# 
# <hr><hr>
# 
# ## Readings 
# 1. [How to Delineate a Watershed](http://54.243.252.9/ce-3354-webroot/3-Readings/NewHampshire-Watersheds/Topowatershed.pdf)
# 2. [Cleveland, T. G. (2017) *Engineering Hydrology Notes (Hydrologic Data; Watershed Delineation) to accompany CE-3354*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/1-Lectures-2017/Lecture03.pdf)
# 
# <hr>

# ### Step 1.  Map of area of interest
# 
# Identify the pour point. 
# 
# ![](pourpoint.png)

# ### Step 2.  Superimpose a Grid
# 
# While not strictly necessary its helpful.  The grid serves two purposes, first a reference system and as a raster representation of the watershed (albeit at a coarse resolution) 
# 
# ![](gridoverlay.png)

# ### Step 3.  Cell Elevations
# 
# Use the grid to estimate average elevations in a grid cell, you use this information to help locate the boundary.  Water flows from high to low elevation.  Starting from the outlet work uphill until have high point, if its downhill as you cntinue in one direction beyond the point, its possibly the boundary (you are identifying "ridgeline" features).
# 
# Simultaneously identify internal water flow paths, these help identify the ridgeline features.
# 
# ![](estimatecellelev.png)

# ### Step 3.  Draw/Refine Boundary Estimates
# 
# Using the grid to estimate average elevations in a grid cell, you locate the coarse resolution boundary.  Water flows from high to low elevation.  Using the internal water flow paths, move upgradient along these paths to refine the boundary delineation.
# 
# ![](drawboundary.png)

# ### Step 4.  Tidy up Boundary
# 
# Tidy up your boundary and declare victory!
# 
# ![](completed-delineation.png)

# # Delineation (by GIS)
# 
# <hr><hr>
# 
# ## Readings 
# 1. [Baraka, M. 2024, Watershed Delineation in QGIS: A Summary Guide](http://54.243.252.9/ce-5361-webroot/3-Readings/Hydrology_GIS_part1.pdf)
# 
# <hr>

# ## Florida Watershed GIS Workflow
# Here we do step-by-step example of the previous watershed(s).  The steps are those outlined in  [Baraka, M. 2024, Watershed Delineation in QGIS: A Summary Guide](http://54.243.252.9/ce-5361-webroot/3-Readings/Hydrology_GIS_part1.pdf)
# 
# [Florida Watershed Workflow Notes (PDF)](http://54.243.252.9/ce-3354-webroot/ce-3354-webbook-2024/my3354notes/lessons/05-Watersheds/QGISWorkflowFlorida.pdf)

# ## Watershed Metrics (General Concepts)
# 
# Now that the watershed is identified and demarked we can measure a few commonly used and important physical properties.  These measurements are used are to characterize the fundamental unit in surface water hydrology which is the watershed.
# 
# - A watershed is defined as the area on the surface of the earth that drains to a specific location.
# 
# A minimal description of watershed properties must include:
# - Area
# - Main channel length
# - Slope (requires the specification of path), The MCS is usually reported as is the average slope (highest point on the boundary to the pour point).  The transverse slope is often reported too.
# - Soil permeability
# - \%-impervious (developed)

# ### Measuring Area
# 
# - If the grid cells used in delineation are all squares, one can count the squares contained in the watershed, multiply by the per-cell area and have a good estimate of the watershed area.
# 
# - If using GIS there is usually an area measurement tool; one can use it, or use the Ones raster mask information to count squares and convert into useful values

# ### Measuring Length(s) 
# 
# Similar to area, you can count cells along a path and multiply the count by the length of a cell side, or the cell diagonal (depends on how many diagonal moves you need to make) to obtain a length.  Or use software (Acrobat Pro, AutoCAD, Engauge, ArcGIS, QGIS, .... ) to make the measurements.

# ### Estimating Slope(s)
# 
# Slope estimates require two components
# 1. A path with a length ($S$)
# 2. The change in elevation along the path ($\Delta z$)
# 
# The dimensionless slope is simply the ratio of the two $\frac{\Delta z}{S}$.  Percent slope is the dimensionless slope multiplied by 100.
# Sometimes slope is expressed in units of $\frac{ft}{mi}$ or $\frac{m}{km}$, while meaningful these will have to be converted into dimensionless or \%-slope for most hydrologic computations.

# ### Estimating Soil Properties
# 
# Subjective when using paper maps, but reasonable values can be inferred from soil maps - either paper-based or electronic [Web Soil Survey](https://websoilsurvey.sc.egov.usda.gov/App/HomePage.htm)
# 
# ![](websoilsurvey.png)
# 
# :::{note}
# There is a GIS plug-in that can directly access the USDA database.
# :::

# ### Estimating \%-Impervious
# 
# This is subjective, but one reasonable approach is using Google Earth
# 1. Find the area of interest
# 2. Select a viewing height (needs to be same for all areas if you are going to have to scroll)
# 3. Put a grid on the screen (physical grid on see‐thru plastic, or use a china marker and draw on the screen)
# 4. Count concrete vs not concrete – relative ratio is a useable estimate of the \% impervious
# 
# :::{note}
# This would be a good task to hand off to a machine learner model.  Take the area of interest, capture an image, have the ML model count pixels that are NOT CONCRETE (brown, green, .....).
# 
# Land use coverages are available in GIS that could be used.
# :::

# ## USGS StreamStats
# 
# In many states one could also use an on-line tool called [StreamStats](https://streamstats.usgs.gov/ss/)
# 
# For example a culvert on Snake Creek in Oklahoma can be examined and will produce the delineation below
# 
# ![](snakecreek.png)
# 
# Once the watershed is defined, download the shapefile(s) into your GIS and proceede with your remaining hydrological tasks.
# 

# In[ ]:




