#!/usr/bin/env python
# coding: utf-8

# # Precipitation over an Area
# 
# The measurement techniques described here have all concentrated on measuring rainfall at a precise location (or at least over an extremely small area).  In reality, the hydrologist needs to know how much 
# precipitation has fallen over a far larger area, usually 
# a catchment. To move from point measurements to 
# a spatially distributed estimation it is necessary to 
# employ some form of spatial averaging. The spatial 
# averaging must attempt to account for an uneven 
# spread of rain gauges in the catchment and the various factors that we know influence rainfall distribution 
# (e.g. altitude, aspect and slope). A simple arithmetic 
# mean will only work where a catchment is sampled 
# by uniformly spaced rain gauges and where there is 
# no diversity in topography. If these conditions were 
# ever truly met then it is unlikely that there would be 
# more than one rain gauge sampling the area. Hence 
# it is very rare to use a simple averaging technique.
# There are different statistical techniques that 
# address the spatial distribution issues, and with the 
# growth in use of Geographic Information Systems (GIS) it is often a relatively trivial matter to 
# do the calculation. As with any computational task 
# it is important to have a good knowledge of how 
# the technique works so that any shortcomings are 
# fully understood. Three techniques are described 
# here: Thiessen’s polygons, the hypsometric 
# method and the isohyetal method. These methods are explored further in a Case Study on p. 40.
# 
# ## Thiessen’s polygons
# Thiessen was an American engineer working around 
# the start of the twentieth century who devised a 
# simple method of overcoming an uneven distribution of rain gauges within a catchment (very much 
# the norm). Essentially Thiessen’s polygons (Thiessen 
# 1911) attach a representative area to each rain gauge. 
# The size of the representative area (a polygon) is based 
# on how close each gauge is to the others surrounding 
# it, but all points within a polygon are closer to its rain 
# gauge than any of the other rain gauges.
# Polygons are drawn by connecting the nearest rain 
# gauges to each other by lightly drawn lines. The perpendicular bisector of each connecting line is then 
# found, and these are extended to where they intersect 
# with other perpendicular bisectors. The boundaries 
# of the polygons are therefore equidistant from each 
# gauge (see Figure 2.13). Once the polygons have 
# been drawn, the area of each polygon surrounding a 
# rain gauge is found. The spatially averaged rainfall 
# (R) is calculated using Form
# 
# HHHHHHHHHHHHH
# 
# he polygon surrounding rain gauge i, and A is the 
# total catchment area (ai
# /A is therefore the proportion of the catchment occupied by each polygon, 
# and the set of these for a catchment are known as 
# Thiessen coefficients).
# The areal rainfall value using Thiessen’s polygons is a weighted mean, with the weighting being 
# based upon the size of each representative area 
# (polygon). This technique is only truly valid where 
# the topography is uniform within each polygon so 
# that it can be safely assumed that the rainfall distribution is uniform within the polygon. This would 
# suggest that it can only work where the rain gauges are located initially with this technique in mind 
# 
# ## Hypsometric method
# Since it is well known that rainfall is positively 
# influenced by altitude (i.e. the higher the altitude 
# the greater the rainfall) it is reasonable to assume 
# that knowledge of the catchment elevation can be 
# brought to bear on the spatially distributed rainfall estimation problem. The simplest indicator 
# of the catchment elevation is the hypsometric (or 
# hypsographic) curve. This is a graph showing the 
# proportion of a catchment above or below a certain 
# elevation. The values for the curve can be derived 
# from maps using a planimeter or using a digital 
# elevation model (DEM) in a GIS.
# The hypsometric method of calculating spatially 
# distributed rainfall then calculates a weighted 
# average based on the proportion of the catchment 
# between two elevations and the measured rainfall 
# between those elevations (Equation 2.2).
# 
# (2.2)
# where rj
#  is the average rainfall between two contour intervals, ai
#  is the area between those contours 
# (derived from the hypsometric curve), and A is the 
# total catchment area. So ai
# /A is again the proportion 
# of the catchment, but this time on the basis of the 
# area between the contours rather than each polygon, 
# as was the case in the previous method. The rj
#  value 
# may be an average of several rain gauges where there 
# is more than one at a certain contour interval. This 
# is illustrated in Figure 2.14 where the shaded area 
# (a3) has two gauges within it. In this case the rj
#  value 
# will be an average of r4 and r5.
# Intuitively this is producing representative areas 
# for one or more gauges based on contours and spacing, rather than just on the latter as for Thiessen’s 
# polygons. There is an inherent assumption that 
# elevation is the only topographic parameter affecting rainfall distribution (i.e. slope and aspect are ignored). It also assumes that the relationship 
# between altitude and rainfall is linear, which is not 
# always the case and warrants exploration before 
# using this technique
# 
# ## Isohyetal method
# 
# Where there are a large number of gauges within 
# a catchment the most obvious weighting to apply 
# on a mean is based on measured rainfall distribution 
# rather than on surrogate measures as described above. 
# In this case a map of the catchment rainfall distribution can be drawn by interpolating between the 
# rainfall values, creating a smoothed rainfall surface. 
# The traditional isohyetal method involved drawing 
# isohyets (lines of equal rainfall) on the map and calculating the area between each isohyet. The spatial 
# average could then be calculated by Equation 2.3:
# R r a
# A i
# n
# j i = 
# 
# 
# 
# 
# 
# 
# 
# 
#  =
# ∑1
# (2.3
# 
# where ai
#  is the area between each isohyet and ri
#  is the 
# average rainfall between the isohyets. This technique 
# is analogous to Figure 2.14, except in this case the 
# contours will be of rainfall rather than elevation.

# ## Areal Reduction Factors
# 
# Areal reduction factors (ARFs) are used in precipitation modeling to account for the spatial variability of rainfall across a region. Precipitation is not uniformly distributed over an area, and ARFs help adjust point rainfall measurements to better represent the average precipitation for a larger region.
# 
# In precipitation modeling, meteorologists often collect rainfall data from specific points, such as weather stations. However, this point data may not accurately reflect the variability of precipitation over a broader area. ARFs are applied to these point measurements to estimate the average precipitation over a larger spatial scale.
# 
# The factors influencing areal reduction include topography, land use, and other geographical features that affect how rainfall is distributed across an area. By applying ARFs, modelers can better capture the spatial patterns of precipitation, improving the accuracy of rainfall estimates for hydrological and environmental studies. This consideration is crucial for various applications, such as flood risk assessment, water resource management, and climate modeling.

# ### Related References
# 1. [Areal-Reduction Factors for the Precipitation
# of the 1-Day Design Storm in Texas USGS WRI 99-4267](https://pubs.usgs.gov/wri/wri99-4267/pdf/wri99-4267.pdf)

# ## Radar Precipitation Estimation
# 
# Radar rainfall estimates involve using weather radar systems to measure precipitation over a given area. These estimates are valuable for various applications, including weather forecasting, hydrological modeling, and flood management. Unlike point measurements from rain gauges, radar provides spatially continuous information about precipitation distribution.
# 
# Radar systems emit radio waves that interact with precipitation particles in the atmosphere. By analyzing the returned signals, meteorologists can estimate the intensity and location of rainfall across a region. However, radar data may still contain uncertainties and errors that need to be addressed.
# 
# To improve the accuracy of radar rainfall estimates, meteorologists often employ various correction techniques. One common method is gauge adjustment, where radar data are calibrated using ground-based rain gauge measurements. Another approach involves applying quality control measures to filter out artifacts and errors in the radar signal.
# 
# Additionally, radar-based estimates may be adjusted using gauge-to-radar ratios to better represent ground-level precipitation. These ratios help account for potential biases in the radar measurements, ensuring that the radar-derived rainfall values align more closely with **ground truth** observations.
# 
# Radar rainfall estimates provide valuable information about precipitation patterns over a wide area, but correction and adjustment methods are required to maintain accuracy and reliability for applications in meteorology and hydrology.

# In[ ]:




