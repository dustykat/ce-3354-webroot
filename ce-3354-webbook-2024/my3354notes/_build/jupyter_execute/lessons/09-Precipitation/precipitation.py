#!/usr/bin/env python
# coding: utf-8

# # 8. Precipitation, Hyetographs, Design Storms

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
# 
# 13. [PAULHUS, J. L. H. , and M. A. KOHLER. "INTERPOLATION OF MISSING PRECIPITATION RECORDS". Monthly Weather Review 80.8 (1952): 129-133.](http://54.243.252.9/ce-5361-webroot/3-Readings/NormalRatioMethod/mwr-080-08-0129.pdf)
# 
# 14. [Missing Rainfall Data Replacement Techniques](http://54.243.252.9/ce-5361-webroot/3-Readings/MissingRainfallData/MissingRainfallData.pdf)
# 
# 15. [Areal-Reduction Factors for the Precipitation of the 1-Day Design Storm in Texas USGS WRI 99-4267](https://pubs.usgs.gov/wri/wri99-4267/pdf/wri99-4267.pdf)

# ## Videos
# 
# 1. [Engineering Hydrology-Precipitation](https://www.youtube.com/watch?v=BB7g_uK-zsg)
# 2. [How do we get Rain, Hail, Freezing Rain, Sleet & Snow? (YouTube)](https://www.youtube.com/watch?v=1wreQRWF1FM)
# 3. [Types of precipitation explained (YouTube)](https://www.youtube.com/watch?v=Lw6AWVCdEtM)
# 4. [Methods of Finding Average Rainfall (YouTube)](https://www.youtube.com/watch?v=U8AAU19CgB0)
# 5. [Rainfall Statistics, Intensity-Duration-Frequency (IDF) Curves - Part 1](https://www.youtube.com/watch?v=JXSwKmfMZJo)
# 6. [Rainfall Statistics, How to Interpret Intensity-Duration-Frequency (IDF) Curves - Part 2](https://www.youtube.com/watch?v=Ui-VYSB9nOY)
# 7. [IDF Curves (YouTube)](https://www.youtube.com/watch?v=VV00CaM48f8)
# 8. [NRCS 24-h Rainfall Distribution (YouTube)](https://www.youtube.com/watch?v=wdb13pFhp-0)
# 9. [Dimensionless Hyetograph for Design Storm Modeling (YouTube Animation)](https://www.youtube.com/watch?v=BbvOmP3lQio)
# 10. [NRCS/SCS Design Storms (YouTube)](https://www.youtube.com/watch?v=RFWtqkUZjRg&t=2601s)
# 11. [Areal extent of rainfall/how to measure rainfall/rainfall radar/rainfall measurement ](https://www.youtube.com/watch?v=Smg_c93luwQ)
# 12. [Weather Radar 101](https://www.youtube.com/watch?v=qhXj3s9qwTE)
# 

# ## Outline
# 
# 1. What is precipitation
# 2. Point precipitation 
#   1. Probability estimation Modeling
#   2. Design Storms
# 3. Areal precipitation
#   1. ARF approach
#   2. Radar rainfall

# ## Description
# 
# Precipitation is the water which falls from the atmosphere in either liquid or solid form. It results from the condensation of moisture in the atmosphere due to cooling of a parcel of air. The most common cause of cooling is dynamic or adiabatic lifting of the air. Adiabatic lifting means that a
# given parcel of air is caused to rise with resultant cooling and possible condensation into very small cloud droplets. If these droplets coalesce and be-
# come of sufficient size to overcome the air resistance, precipitation in some form results.
# 
# Surface water hydrology really begins before the precipitate hits the ground.  The form of precipitate is important (rain, sleet, hail, or snow).  For example it takes about 10 inches of snow to produce the same water as 1 inch of rain.  Other factors of importance are the size of the area over which the precipitation falls, the intensity of the precipitation, and its duration.
# 
# ![](hc-precip.png)
# 
# Once the precipitation hits the ground several things can happen.  It can evaporate immediately, especially if the surface is hot, and relatively impervious.  If the surface is dry and/or porous, the precipitate may infiltrate into the ground or may just wet the surface.   The process of just wetting leaves and blades of grass is called interception.  Some of the infiltrated water is returned to the atmosphere by transpiration by plants.  Collectively the return to the atmosphere is called evapotranspiration.  The precipitate may be trapped in small depressions (puddles).  It may remain in these puddles until it evaporates or until the depressions fill and overflow.  Finally it may run off directly to the nearest stream or lake to become surface water.  The four “processes” (evapotranspiration, infiltration, interception, and depression storage) that reduce the amount of precipitation available for direct runoff are collectively called abstractions.  In drainage engineering, the loss model is how we account for these processes.

# ## Forms of Precipitation
# 
# Precipitation occurs in various forms. Rain is precipitation that is in the liquid state when it reaches the earth. 
# ![](rainfall.png)<br>
# Snow is frozen water in a crystalline state, while hail is frozen water in a 'massive' state. <br>
# ![](snowfall.png)<br>
# Sleet is melted snow which is an intermixture of rain and snow. Of course, precipitation that falls to earth in the frozen state cannot become part of the runoff process until thawing and melting occur. Much of the precipitation that falls in mountainous areas and in the northerly latitudes falls in frozen form and is stored as snowpack or ice until warmer temperatures prevail.
# 
# [Rain, Sleet, or Snow (YouTube Video)](https://youtu.be/cYjOEQhA_RI)

# ### Types of Precipitation (by Origin)
# Precipitation can be classified by the origin of the lifting motion which
# causes the preci pi ta ti on. Each type is characterized by different spatial
# and temporal rainfall regimens. There are three major types of storms which
# can be classified as follows:
# 1. **Convective Storms.**  Convective storms are atmospheric disturbances characterized by strong upward movement of air. They occur when warm, moist air rises, cools, and condenses, forming clouds and often leading to precipitation. <!--The two primary types of convective storms are thunderstorms and tornadoes. Thunderstorms are typically composed of cumulonimbus clouds and are accompanied by lightning, thunder, heavy rain, and sometimes hail. They form when warm, moist air rises rapidly, creating instability in the atmosphere. Tornadoes, on the other hand, are rapidly rotating columns of air that extend from a thunderstorm to the ground. They form within severe thunderstorms and can cause significant damage due to their strong winds.--> 
# 2. **Orographic Storms.**  Orographic storms, also known as orographic precipitation or orographic lifting, occur when air is forced to rise over elevated terrain, such as mountains or hills. As the air moves upward, it cools and condenses, leading to cloud formation and precipitation. <!-- This process happens on the windward side of the mountain, where moist air is lifted and cooled, often resulting in increased rainfall or snowfall.The lifting of air over the terrain causes the moisture in the air to condense and form clouds. As the air continues to rise, it cools further, leading to more significant precipitation on the windward side of the mountain. The leeward side, or the "rain shadow" side, tends to experience drier conditions as the air descends and warms, having already released much of its moisture on the windward side.-->
# 3. **Cyclonic Storms.**  Cyclonic storms, also known as cyclones or hurricanes (depending on the region), are powerful low-pressure systems characterized by rotating winds and organized thunderstorms. These storms typically form over warm ocean waters, where moist air rises and creates an area of low pressure.  As the warm air rises, it cools and condenses, forming clouds and releasing heat energy that fuels the storm's development. <!--The Earth's rotation causes the system to spin, creating a circular pattern of winds. In the Northern Hemisphere, cyclonic storms rotate counterclockwise, while in the Southern Hemisphere, they rotate clockwise.  Cyclonic storms go through various stages of development, starting as tropical disturbances and progressing into tropical depressions, tropical storms, and finally, reaching hurricane or typhoon status, depending on their location. They are categorized by their sustained wind speeds, with hurricanes or typhoons reaching higher wind velocities.  These storms can cause extensive damage due to their strong winds, heavy rainfall, storm surges, and potential for flooding. Proper forecasting and preparedness are crucial in regions prone to cyclonic storms to mitigate their impact on communities and infrastructure.-->

# ### Convective Storms
# Precipitation from convective storms results as warm moist air rises from
# lower elevations into cooler overlying air as shown below. 
# 
# ![](convectivestorm.png)
# 
# The characteristic form of convective precipitation is the summer thunderstorm. The surface of the earth is warmed considerably by mid-to late afternoon of a summer day, the surface imparting its heat to the adjacent air. The warmed air begins rising through the overlying air, and if proper moisture content conditions are met (condensation level), large quantities of moisture will be condensed from the rapidly rising, rapidly cooling air. The rapid condensation may often result in huge quantities of rain from a single thunderstorm spawned by convective action, and very large rainfall rates are quite common beneath slowly moving thunderstorms.
# 
# ### Orographic Storms
# 
# Orographic precipitation results as air is forced to rise over a fixed position geographic feature such as a range of mountains. The characteristic precipitation patterns of the Pacific coastal states are the result of significant orographic influences. Mountain slopes that face the wind (windward) are much wetter than the opposite (leeward) slopes. In the Cascade Range in Washington and Oregon, the west-facing slopes may receive upwards of 100 inches (254 cm) of precipitation annually, while the east facing slopes, only a few miles away over the crest of the mountains, receive on the order of 20 inches (51 an) of precipitation annually.
# 
# ![](orographicstorm.png)
# 
# ### Cyclonic Storms
# 
# Cyclonic precipitation is caused by the rising or lifting of air as it converges on an area of low pressure. Air moves from areas of higher pressure
# toward areas of lower pressure. In the middle latitudes, cyclonic storms generally move from west to east and have both cold and warm air associated with them. These mid-latitude cyclones are sometimes called extra-tropical cyclones or continental storms. Continental storms occur at the boundaries of air of significantly different temperatures. A disturbance in the boundary between the two air parcels can grow, appearing as a wave as it travels from west to east along the boundary. Generally, on a weather map, the cyclonic storm will appear as shown in below with two boundaries or fronts developed.
# 
# ![](frontalstorm.png)
# 
# One has warm air being pushed into an area of cool air, while the other has cool air pushed into an area of warmer air. This type of air movement is called a front; where warm air is the aggressor it is a warm front, and where cold air is the aggressor it is a cold front. The precipitation associated with a cold front is usually heavy and covers a relatively small area, whereas the precipitation associated with a warm front is more passive, smaller in quantity, but covers a much larger area, as pictured below. 
# 
# ![](midlatstorm.png)
# 
# Tornadoes and other **violent** weather phenomena are associated with cold fronts.

# ## Precipitation Variables of Interest
# 
# There are several variables of interest:
# 
# 1. Intensity: how hard it rains (a rate)
# 2. Duration: how long it rains at any given intensity (a time)
# 3. Frequency: how often it rains at any given intensity and duration (a probability)
# 4. Spatial Distribution: the rainfall depth over an area (a surface/volume)
# 5. Temporal Distribution: the time series of rainfall depth over an area (or point).  The point feature is called a *hyetograph*.
# 
# Rainfall probabilities are expressed as a combination of frequency (probability), depth, and duration. The inclusion of depth and duration reflects that different “storms” can produce the same total depth, but deliver that depth over much different times 
# 
# :::{note}
# A slow gentle rain for a long time versus a hard rain for a short time can have the same total depth, but vastly different hydrologic impact
# :::

# ## Depth-Duration-Frequency
# 
# - Depth of rainfall is the accumulated depth (in a gage) over some time interval.
# - Duration is that time interval.
# - Frequency is the probability (like AEP) of observing the depth over the given duration.
# 
# ![](DDFcurve.png)

# An alternate to DDF is to present the magnitude as an intensity (a rate). The intensity is the ratio of an accumulated depth to some averaging time, usually the duration.
# 
# $$ i_{avg}=\frac{D}{T_C}$$
# 
# where $D$ is the depth, and $T_C$ is the averaging time
# 
# 
# :::{note}
# Intensity is NOT the instantaneous rainfall rate.  
# 
# >The symbol $T_C$ represents the [time of concentration](https://en.wikipedia.org/wiki/Time_of_concentration) for a watershed, **if** the averaging time happens to coincide with the time needed for water to flow from the most remote point in a watershed to the watershed outlet; otherwise its just an arbitrary averaging time.
# :::
# 
# Intensity is related to depth and duration.   
# 
# ![](intensityExample.png)
# 
# The intensity is the ratio of depth to a particular duration.  For example, if the duration or averaging time is 12 hours and the accumulated depth for 12 hours is 70 mm (about 3 inches), then the average rate is 70mm/12hours = 5.8 mm/hour.  This average rate, if applied over 12 hours will produce the depth of 70mm.
# 
# Conversion from Depth-Duration to Intensity-Duration is obtained by the ratio of depth to duration
# 
# $$ i_{avg}=\frac{D}{T_C}$$
# 
# Conversion from Intensity-Duration to Depth-Duration is obtained by multiplication
# 
# ## Intensity-Duration-Frequency
# 
# The family of curves that depicts the relationship between the intensity, duration, and frequency of precipitation at a point is a fundamental part of the rational equation method for storm water drainage design.
# 
# ![](IDFcurves.png)
# 
# Conversion from Depth-Duration to Intensity-Duration is obtained by the ratio of depth to duration
# 
# $$ i_{avg}=\frac{D}{T_C}$$
# 
# Conversion from Intensity-Duration to Depth-Duration is obtained by multiplication
# 
# $$ D = i_{avg}*{T_C}$$

# <!-- ## References
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
# 10. [Williams-Sether, T., Asquith, W.H., Thompson, D.B., Cleveland, T.G., and X. Fang. 2004. ``Empirical, Dimensionless, Cumulative-Rainfall Hyetographs for Texas.'' U.S.Geological Survey Scientific Investigations Report 2004-5075, 138p. ](http://54.243.252.9/ce-3354-webroot/3-Readings/EmpiricalHyetographs/sir2004-5075.pdf)
# 
# 11. [hec19](https://www.fhwa.dot.gov/engineering/hydraulics/pubs/hec/hec19.pdf)
# 
# 12. [McCabe, K. (2022) "Rain, sleet or snow?" Royal Meterological Society](https://www.rmets.org/metmatters/rain-sleet-or-snow)
# 
# 13. [PAULHUS, J. L. H. , and M. A. KOHLER. "INTERPOLATION OF MISSING PRECIPITATION RECORDS". Monthly Weather Review 80.8 (1952): 129-133.](http://54.243.252.9/ce-5361-webroot/3-Readings/NormalRatioMethod/mwr-080-08-0129.pdf)
# 
# 14. [Missing Rainfall Data Replacement Techniques](http://54.243.252.9/ce-5361-webroot/3-Readings/MissingRainfallData/MissingRainfallData.pdf)
# 
# 15. [Areal-Reduction Factors for the Precipitation of the 1-Day Design Storm in Texas USGS WRI 99-4267](https://pubs.usgs.gov/wri/wri99-4267/pdf/wri99-4267.pdf) 
# -->

# ## Design Storms
# 
# A design storm is a theoretical or hypothetical weather event used by engineers, urban planners, and hydrologists as a standard to simulate and predict the potential impact of extreme weather conditions on a particular area. It is employed in the design and planning of various structures and systems to ensure they can withstand or manage the expected stresses caused by intense rainfall or other weather-related factors.

# ## Design Storm Characteristics
# 
# The characteristics of a design storm typically include:
# 
# - Intensity: The rate of rainfall or snowfall during the storm, often measured in inches per hour or millimeters per hour.
# - Duration: The period over which the intense rainfall or weather event persists, often measured in hours.
# - Frequency: Often associated with a particular return period (e.g., 10-year storm, 50-year storm, 100-year storm), representing the average time interval between occurrences of storms of similar magnitude.
# 
# For instance, a 100-year design storm doesn't mean it occurs once every century; rather, it indicates that there's a 1% chance of this intensity of storm happening in any given year.
# 
# Design storms are used in various engineering and urban planning scenarios, such as:
# 
# - Hydraulic Design: Designing stormwater drainage systems, sewers, culverts, and other structures to handle anticipated water flow during extreme weather events.
# - Floodplain Management: Assessing the potential impact of flooding and creating regulations for construction in flood-prone areas.
# - Infrastructure Design: Designing bridges, dams, and other structures to withstand the forces exerted by extreme weather conditions.
# 
# These storms are not exact events that have occurred in the past; rather, they're created based on statistical analyses of historical weather data to provide a standard for planning and design purposes. They assist in creating structures and systems that can manage the potential stress of extreme weather events, ensuring safety and functionality within the built environment.
# 
# Design storms are statistical models of such temporal behavior and are used in hydrologic models when hydrographs need to be generated

# ## Rainfall Distributions
# 
# - Rainfall distributions represent temporal patterns of a storm.
# - A rainfall distribution is also called a hyetograph.
# - Rainfall distributions are used when we need to estimate an entire hydrograph.

# :::{admonition} Discrete Data Analysis
# 
# The Figure below is a representation of some continuous process.  To extract values by measurements only occurs at discrete points in time. These samples are reconstructed in a variety of ways to restore the original representation.
# 
# ![width="400"](data_repr.png)
# 
# 
# Real data are always some kind of discrete sample
# 
# - The “pulse” type is typical – and is called incremental data.
# - For instance, incremental rainfall would be the catch over some time interval ($\Delta t$ in the figure)
# - An alternative way to represent the data is with a cumulative representation (which is the running sum of the incremental data)
# 
# The Figure below depicts the relationship between incremental and cumulative representations. Each “block” represents the amount of rainfall for the time interval
# - The collection of blocks is called “incremental” rainfall (red)
# - The running sum of the blocks is the cumulative distribution (blue)
# 
# A particular block is indicated with a height of about one, and time duration also one.  If for instance the block represents a depth the implication is that after one hour (from time 4 to 5 in the drawing) the depth added to some location is one unit. 
# 
# ![width="400"](incr-cum-repr.png)
# 
# 
# If these are watershed inches, then the drawing sugests that from hour zero to one, zero inches of precipitation occur, from hour one to two, about 1/4 inch; from hour 2 to 3, about 0.4 inch; from hour 3 to 4, about 0.7 inch; and hour 4 to 5; 1 inch; and so on.  If we tabulated the information we would have
# 
# |Time| Incremental Depth (Red)| Accumulated Depth (Blue)|
# |---:|---:|---:|
# |0|0.00|0.00|
# |1|0.25|0.00|
# |2|0.40|0.25|
# |3|0.70|0.65|
# |4|1.00|1.35|
# |5|0.50|2.35|
# 
# Accumulating (running sum) the incremental is called “aggregation” (or just plain numerical integration); Differencing the cumulative is called “disaggregation.” For practical application its often handy to zero pad the leading and trailing edges so don’t have to worry about forward/backward differencing issues.  
# 
# **Computational Thinking (ENGR-1330) - Accumulation**
# 
# Consider the need to accumulate data such as:
# 
# |Time (hours)| Incremental Depth (inches)| Accumulated Depth (inches)|
# |---:|---:|---:|
# |0|0.121||
# |1|0.121||
# |2|0.132||
# |3|0.154||
# |4|0.165||
# |5|0.187||
# |6|0.198||
# |7|0.242||
# |8|0.297||
# |9|0.374||
# |10|0.594||
# |11|4.708||
# |12|1.199||
# |13|0.528||
# |14|0.374||
# |15|0.286||
# |16|0.253||
# |17|0.209||
# |18|0.176||
# |19|0.154||
# |20|0.132||
# |21|0.132||
# |22|0.132||
# |23|0.132||
# |24|0.000||
# 
# Our goal is to complete the last column, in this case its relatively straight forward because the time spacing is uniform.  The approach is to perform numerical integration using rectangular panels looking backward in time.
# 
# $$acc_{i}=inc_{i-1}+acc_{i-1}$$
# 
# :::

# In[1]:



time=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
increment=[0.121,0.121,0.132,0.154,0.165,0.187,0.198,0.242,0.297,0.374,0.594,4.708,1.199,0.528,0.374,0.286,0.253,0.209,0.176,0.154,0.132,0.132,0.132,0.132,0]
accumulate=[0 for i in range(len(time))]

for i in range(1,len(time)):
    accumulate[i] = accumulate[i-1]+increment[i-1]


import matplotlib.pyplot as plt # the python plotting library
plottitle ='Precipitation for Somewhere USA ' 
mydata = plt.figure(figsize = (10,5)) # build a square drawing canvass from figure class
plt.plot(time, increment, c='red',drawstyle='steps') # step plot
plt.plot(time, accumulate, c='blue',drawstyle='steps') # step plot
plt.xlabel('Time (hours)')
plt.ylabel('Depth (inches)')
plt.legend(['Incremental Depth','Accumulated Depth'])
plt.title(plottitle)
plt.show()


# When the time spacing is non-uniform, the numerical integration using rectangular panels looking backward in time is complicated by the various time increments.  The listing below is a FORTRAN script to process such situations it should be relatively easy to port the script to python, fix the file reading structure and then have a pretty general tool.  
# 
# ```
# c program to interpolate rain and runoff data into one minute increments 
#       program interpolate 
#       parameter(maxrow=10000)
#       implicit real*8 (a-h,o-z)
#       dimension etime(maxrow)
#       dimension acc_wtd_value(maxrow)
#       character*255 content
# c
# c read data file
# c
#         itdata=0
#         do 2001 irain=1,maxrow,1
#          read(unit=*,fmt='(a)',end=2002)content
#          if(content(1:1) .eq. '#' .or.
#      1      content(2:2) .eq. '#' .or.
#      3      content(3:3) .eq. '#'      )then
#           write(*,9001)content(1:80)
#          else
# c
# c should be datastream here use a formatted read
# c
#           itdata=itdata+1
#           read(content,*)etime(itdata),acc_wtd_value(itdata)
#          end if
#  2001   continue
#         write(*,*)'end of file -- reset array sizes'
#         go to 666
#  2002   continue
# c
# c end of file read
# c
# c
# c now interpolate, use real values loop indices
# c
#       do 3001 idx=2,itdata
#        slope=acc_wtd_value(idx)-acc_wtd_value(idx-1)
#        slope=slope/(etime(idx)-etime(idx-1))
#        do 3002 rtime=etime(idx-1),etime(idx)-1.0,1.0
#         value=acc_wtd_value(idx-1)+slope*(rtime-etime(idx-1))
#         write(*,9002)rtime,value
#  3002  continue
#  3001 continue
#   666 stop
#  9001 format(a80)
#  9002 format(2(g12.6,2x))
#       end
# ```
# 
# :::{admonition} To do:
# Port above FORTRAN to python, modify file management for general use.  Recall python cannot use floats as indices, so the loop processing needs rewrite.  Include an example.
# :::
# 

# ### Design Distributions
# Distributions from historical storms are analyzed to generate statistical **models** of rainfall – these models are called **design storms**. Design storm distributions are typically represented as dimensionless hyetographs
# 
# Some often used models are:
# 
# - NRCS Type Storms (24 hour, 6 hour) 
# - Empirical Texas Hyetographs (TxHYETO-2015)
# 

# ## NRCS (SCS) Rainfall Type Curves
# 
# SCS(1973) analyzed DDF curves to develop dimensionless rainfall temporal patterns called type curves for four different regions in the US. SCS type curves are in the form of percentage mass (cumulative) curves based on 24-hr rainfall of the desired frequency. Intended for use with the SCS Curve Number runoff generation model!
# 
# Location selects the type curve
# 
# ![](scsLocation.png)
# 
# The 24-hour precipitation depth of desired frequency is specified (NOAA Atlas 14), then the SCS type curve is rescaled (multiplied by the known number) to get the time distribution. 
# 
# ![](TCforRescale.png)
# 
# A tabular representation is
# 
# ![](TCtabular.png)
# 
# A simple script to dimensionalize is listed below (along with the plotting script)

# In[2]:


# SCS Type Curves

hour = [0,2,4,6,7,8,8.5,9,9.5,9.75,10,10.5,11,11.5,11.75,12,12.5,13.0,13.6,14,16,20,24]
type1 = [0,0.035,0.076,0.125,0.156,0.194,0.219,0.254,0.303,0.362,0.515,0.583,0.624,0.654,0.669,0.682,0.706,0.727,0.748,0.767,0.83,0.926,1]
type1A = [0,0.05,0.116,0.206,0.268,0.425,0.48,0.52,0.55,0.564,0.577,0.601,0.624,0.645,0.655,0.664,0.683,0.701,0.719,0.736,0.8,0.906,1]
type2 = [0,0.022,0.048,0.08,0.098,0.12,0.133,0.147,0.163,0.172,0.181,0.204,0.235,0.283,0.357,0.663,0.735,0.772,0.799,0.82,0.88,0.952,1]
type3 = [0,0.02,0.043,0.072,0.089,0.115,0.13,0.148,0.167,0.178,0.189,0.216,0.25,0.298,0.339,0.5,0.702,0.751,0.785,0.811,0.886,0.957,1]

t24  =[]
for i in range(len(hour)):
    t24.append(hour[i]/24.0)

# dimensionalize

Ptotal = 10.0
T1D =[0 for i in range(len(hour))]
T1AD =[0 for i in range(len(hour))]
T2D =[0 for i in range(len(hour))]
T3D =[0 for i in range(len(hour))]
for i in range(len(hour)):
    T1D[i]=Ptotal*type1[i]
    T1AD[i]=Ptotal*type1A[i]
    T2D[i]=Ptotal*type2[i]
    T3D[i]=Ptotal*type3[i]
#plot

import matplotlib.pyplot as plt # the python plotting library
plottitle ='SCS Rainfall Type Curves for Total Depth =' + str(Ptotal) +' inches'
mydata = plt.figure(figsize = (10,5)) # build a square drawing canvass from figure class
plt.plot(hour, T1D, c='blue') # step plot
plt.plot(hour, T1AD, c='cyan') # step plot
plt.plot(hour, T2D, c='orange') # step plot
plt.plot(hour, T3D, c='red') # step plot
#plt.plot(time, accumulate, c='blue',drawstyle='steps') # step plot
plt.xlabel('Time (hours)')
plt.ylabel('Depth (inches)')
plt.legend(['Type 1','Type 1A','Type 2','Type 3'])
plt.title(plottitle)
plt.show()


# A variant for 6-hour durations is
# 
# ![](SCS6hr.png)
# 
# Using the type curves is straightforward
# 
# 1. Use NOAA Atlas 14, TP-40, or other defendable source to set total depth, P for the 24 hour storm (or 6 hour storm)
# 2. Pick appropriate SCS type curve (location).
# 3. Multiply (rescale) the type curve with P to get the design mass curve.
# 
# If you need incremental values, differencing the rescaled mass curve can be used to develop the design hyetograph.
# 
# ---

# ## Texas Empirical Hyetograph-Based Design Storms
# 
# Alternative to SCS Type Curves for use in **Texas** are the [Texas Empirical Hyetographs](http://54.243.252.9/ce-3354-webroot/3-Readings/EmpiricalHyetographs/sir2004-5075.pdf)
# - Based on Texas data.
# - Reflects “front loading” observed in many real storms.
# - Rescales both time and depth.
# 
# ![](texashyetograph.png)
# 
# The authors suggest use of the 50th percentile curve (median storm).  
# 
# ::{note}
# The 90th percentile is appropriate for high consequence of failure targets (hospitals, sewage treatment plants, water treatment plants, nuclear power plants, thermal power plants, airports,...)
# :::
# 
# - Multiply the time axis by the storm duration.
# - Multiply the depth axis by the storm depth.
# - Result is a design storm for given duration and AEP.

# ## Historical Observations
# 
# The design storms are created from statistical models of observations. 
# 
# Incorporating observed precipitation data offers a faithful representation of actual weather patterns and variability, capturing nuances that statistical design storm models may overlook. By using observed data, engineers can better assess real-world risks, enhancing the reliability and precision of infrastructure designs and flood mitigation strategies. Additionally, observed precipitation data provide valuable insights into localized climatic trends and extreme weather events, enabling proactive adaptation measures to address changing environmental conditions effectively.
# 
# At times, there might be motivation to study the source observations - so how to obtain data is important.  There are likely multiple sources of data - here we will examine just a few.
# 
# ### NCDC
# 
# This is the easiest, and may suffice in many situations.  The National Climatic Data Center maintains historical records of climate related data - in some locations over a century of data exist.  Using our study area, and current online tools one can find gages near the study site. 
# 
# :::{important}
# The study area referred to above is Caprock Canyon SP, not the Hardin Branch area, methods are the same; I already had figures available so choose to go with them instead of recreate for Hardin Branch.
# :::
# 
# [https://www.ncei.noaa.gov/maps/daily/](https://www.ncei.noaa.gov/maps/daily/) will navigate to the NCDC server where daily data are available.  The landing page will look something like:
# 
# ![](ncdc-landing-page.png)

# I have already located our study site - so I'll just zoom in.  In the figure our area is the small yeller rectangles in West Texas.  Zoomed into a useful scale:
# 
# ![](ncdc-zoom-area.png)
# 

# We will select gages by drawing a polygon around them - the one gage close to the study site would be awesome, but it has a really short record, so we will get nearby gages and use some algorithm to map the records to the study site.  To draw the polygon, use the tool on the layers panel, then choose polygon and draw the outline.
# 
# ![](ncdc-polygon-area.png)

# Now we can examine the gages - notice the Caprock Canyon SP gage only has a 3 year record, so alone kind of useless. But the other two extend the historical range considerably.  Next we can add these to the cart for delivery.  
# 
# :::{note}
# The delivery requires added information which will be demonstrated in class, plus we will grab some additional gages for trying to estimate depth over our study area using some averaging techniques. 
# - [Missing Rainfall Data Replacement Techniques](http://54.243.252.9/ce-5361-webroot/3-Readings/MissingRainfallData/MissingRainfallData.pdf)
# - [Normal Ratio Method](http://54.243.252.9/ce-5361-webroot/3-Readings/NormalRatioMethod/mwr-080-08-0129.pdf)
# :::
# 
# Once the request is built the NCDC will send a link to a file for you to download.  In secure systems, you have to edit the link by-hand to defeat the anti-Soviet intrusion software - again will demonstrate as needed.
# 
# The data file itself looks like (click on the link in class):
# 
# [3594221.csv](http://54.243.252.9/ce-5361-webroot/ce5361book/lessons/04precipitation/3594221.csv)
# 

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
# Some representative methods are discribed in:
# 
# 1. [PAULHUS, J. L. H. , and M. A. KOHLER. "INTERPOLATION OF MISSING PRECIPITATION RECORDS". Monthly Weather Review 80.8 (1952): 129-133.](http://54.243.252.9/ce-5361-webroot/3-Readings/NormalRatioMethod/mwr-080-08-0129.pdf)
# 
# 2. [Missing Rainfall Data Replacement Techniques](http://54.243.252.9/ce-5361-webroot/3-Readings/MissingRainfallData/MissingRainfallData.pdf)
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

# In[3]:


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


# In[4]:


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


# ## Precipitation over an Area
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

# <!-- ## Thiessen’s polygons
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
# suggest that it can only work where the rain gauges are located initially with this technique in mind -->
# 
# ### Approximation of Distributed Precipitation Data from Point Gage Data
# A watershed is the area of land where all of the water that is under it or drains off of it goes into the same place. First consider a location where streamflow can be observed, call this location the outlet. Precipitation falls upstream of this location and is the source of runoff past the outlet. If a unit of precipitation falls upstream of the outlet and eventually drains past the outlet, the area defined by all such locations is called the drainage area to the outlet, and this area is the watershed. The concept also applies in groundwater with the area called a basin, or capture zone, depending on context.  In water budget studies and in unit hydrograph analysis the volume of precipitation is as important as the rate and spatial distribution. Missing data are often a problem and either kriging or simple arithmetic interpolation is used to supply estimates of rainfall at a gage location that has missing data. Kriging is probably a more defendable approach but is probably too complicated for manual or small project application.
# The entire volume of rainfall applied to an entire basin is called the precipitation volume. If the basin area normalizes this volume the resulting value is called the effective uniform depth (EUD). There are several methods to compute EUD: arithmetic mean, theissen polygon network, iso-heyetal method. Mean area precipitation and effective uniform depth are for all practical purposes the same concept.
# 
# ![](arealfrompoint.png)
# 
# :::{note}
# The figures above are from author's notes circa 2002; the original source files (MS Word) are unreadable with modern software, fortunately a PDF copy remains!  It's the source of the figures.
# :::

# ### Arithmetic Mean
# The arithmetic mean method simply computes the mean value of all the rain gage catches (depths) and assigns this value as the average uniform depth over the watershed. To determine rainfall volume, multiply this depth by the area.
# The formula for average depth (precipitation) is simply,
# 
# $$\bar P = \frac{1}{n} \sum_{i=1}^{n} {P_i}$$
# 
# In this example the result is 88.4 mm over the entire watershed.
# 
# The total volume in cubic meters is the product of the average depth and the watershed area converted into cubic meters. The watershed area is 16 $km^2$. Thus the total volume of precipitation over the watershed is $1.41 \times 10^6~m^3$. We will compare this volume to the other ways of estimated distributed rainfall depths.

# ### Polygon weighted methods.
# The polygon methods divide the watershed into subareas and assign depths at gages to each sub area, compute the total volume (sum of all sub-area volumes), then divide by the watershed area to determine an area-weighted average. Thiessen polygons (nearest neighbor approach) are the most common division scheme. Thiessen weights are reported in most USGS data.
# 
# :::{admonition} Thiessen’s polygons
# Thiessen was an American engineer working around the start of the twentieth century who devised a 
# simple method of overcoming an uneven distribution of rain gauges within a catchment (very much 
# the norm). Essentially Thiessen’s polygons (Thiessen 1911) attach a representative area to each rain gauge. 
# The size of the representative area (a polygon) is based on  how close each gauge is to the others surrounding it, but all points within a polygon are closer to its rain gauge than any of the other rain gauges.
# Polygons are drawn by connecting the nearest rain gauges to each other by lightly drawn lines. The perpendicular bisector of each connecting line is then found, and these are extended to where they intersect 
# with other perpendicular bisectors. The boundaries of the polygons are therefore equidistant from each gauge. Once the polygons have been drawn, the area of each polygon surrounding a 
# rain gauge is found. The areal rainfall value using Thiessen’s polygons is a weighted mean, with the weighting being 
# based upon the size of each representative area (polygon). This technique is reliable where the topography is uniform within each polygon so that it can be safely assumed that the rainfall distribution is uniform within the polygon. 
# :::
# 
# To determine Thiessen polygons we first draw segments joining each gage.
# 
# ![](theissenpoly1.png)
# 
# Now locate bisectors along each segment.
# 
# ![](theissenpoly2.png)
# 
# Draw perpendicular bisectors at each location, mark each side with nearest gage name.
# 
# ![](theissenpoly3.png)
# 
# Locate intersections of nearest neighbor boundaries, and mark interfaces.  Measure areas within watershed assigned to each gage. The Theissen weight is the ratio of the gage assigned area and the watershed area. Once either the watershed areas are known, or the Theissen weights are known the uniform precipitation depth can be computed as
# 
# :::{note}
# Section incomplete - example at [Link to Example](http://54.243.252.9/ce-3354-webroot/ce-3354-webbook-2024/my3354notes/lessons/09-Precipitation/cive6361_week_002 _A.pdf)
# :::

# <!--## Hypsometric method
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
# using this technique -->
# 
# <!--## Isohyetal method
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
# contours will be of rainfall rather than elevation.-->

# ## Areal Reduction Factors
# 
# Areal reduction factors (ARFs) are used in precipitation modeling to account for the spatial variability of rainfall across a region. Precipitation is not uniformly distributed over an area, and ARFs help adjust point rainfall measurements to better represent the average precipitation for a larger region.
# 
# In precipitation modeling, meteorologists often collect rainfall data from specific points, such as weather stations. However, this point data may not accurately reflect the variability of precipitation over a broader area. ARFs are applied to these point measurements to estimate the average precipitation over a larger spatial scale.
# 
# The factors influencing areal reduction include topography, land use, and other geographical features that affect how rainfall is distributed across an area. By applying ARFs, modelers can better capture the spatial patterns of precipitation, improving the accuracy of rainfall estimates for hydrological and environmental studies. This consideration is crucial for various applications, such as flood risk assessment, water resource management, and climate modeling.

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
