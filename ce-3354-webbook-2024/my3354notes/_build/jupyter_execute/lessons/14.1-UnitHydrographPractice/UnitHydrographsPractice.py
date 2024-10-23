#!/usr/bin/env python
# coding: utf-8

# # 14.1 Unit Hydrograph Workshop Exercise(s)
# 
# :::{admonition} Course Website
# [http://54.243.252.9/ce-3354-webroot/](http://54.243.252.9/ce-3354-webroot/)
# :::

# ## Readings
# 
# 1. [Gupta, R.S., 2017. Hydrology and Hydraulic Systems, pp. 337-361](https://www.waveland.com/browse.php?t=384)
# 
# 2. [Chow, V.T., Maidment,D.M., and Mays, L.W. (1998) Applied Hydrology, McGraw Hill, pp. 201-221](http://54.243.252.9/ce-3354-webroot/3-Readings/CMM1988/) 
# 
# 3. [McCuen, R.H., Johnson, P.A., and Ragan, R.M. (2002) Highway Hydrology. HDS-2 (2ed) FHWA-NHI-02-001 (Read Chapter 6, Section 6.1)](http://54.243.252.9/ce-3354-webroot/3-Readings/FHWAHighwayHydrology/FHWA-NHI-02-001.pdf)
# 
# 4. [Texas Hydraulic Design Manual (2014-1) Texas Department of Transportation. (2014) Hydraulic Design Manual (Read pages XX-X to XX-X)](http://54.243.252.9/ce-3354-webroot/3-Readings/TXDOT-HYDM-2014/txdot-hdm-2014.pdf)
# 
# 5. [Linear Theory of Hydrologic Systems Dooge, J.C. I. (1973) Linear Theory of Hydrologic Systems. USDA ARS Technical Bulletin No. 1468. (Read pages XXX to XXX)](http://54.243.252.9/ce-3354-webroot/3-Readings/LS1973/linear-systems-hydrology-dooge.pdf)
# 
# 6. [Cleveland, T. G. (2015) *Surface Water Hydrology Notes (Unit-Hydrographs Analysis) to accompany CE-3354*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/1-Lectures-2017/Lecture13.pdf)
# 
# 7. [Cleveland, T. G. (2017) *Surface Water Hydrology Notes (Unit-Hydrographs in HEC-HMS) to accompany CE-3354*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/1-Lectures-2017/Lecture14.pdf)

# ## Videos
# 
# 1. [Hydrographs](https://www.youtube.com/watch?v=FGdy_xIaH_Y)
# 2. [How to Interpret a Storm Hydrograph](https://www.youtube.com/watch?v=uWDP9vl13cU)
# 3. [Unit Hydrographs Part 1](https://www.youtube.com/watch?v=aDaOFf0IrTE)
# 4. [Unit Hydrographs Part 2](https://www.youtube.com/watch?v=4f6Hs666dUY)
# 5. [Baseflow Separation](https://www.youtube.com/watch?v=Qw_oPqPhJLs)
# 6. [Baseflow Recession and Hydrologic Equation](https://www.youtube.com/watch?v=olectEAy0Z8)
# 7. [Hydrograph Recession](https://www.youtube.com/watch?v=CykDj1SGGF8&list=PLOO0MwGL5EDLXNfeyRrsj9YZhYk-_BGmD&index=42)
# 8. [Unit Hydrograph and Proportionality](https://www.youtube.com/watch?v=XofeIB1v7s0)
# 9. [Design Storm Excess Precipitation Method](https://www.youtube.com/watch?v=Kr4jnIulaiU)
# 10. [S-Hydrograph (for Time-Shifting)](https://www.youtube.com/watch?v=wSvFrX48JOo)
# 

# ## Spreadsheets
# 
# Listed below are spreadsheets that implement simple UH examples.  They are Excel (circa 2009) spreadsheets, that work in current Excel, LibreOffice, and Numbers environments
# 1. [ExampleUH_BackSub1.xls](http://54.243.252.9/ce-3354-webroot/5-Spreadsheets/ExampleUH_BackSub1.xls)
# 2. [ExampleUH_BackSub2.xls](http://54.243.252.9/ce-3354-webroot/5-Spreadsheets/ExampleUH_BackSub2.xls)
# 3. [ExampleUH_LeastSquares.xls](http://54.243.252.9/ce-3354-webroot/5-Spreadsheets/ExampleUH_LeastSquares.xls)
# 4. [ExampleUH_TransferFn.xls](http://54.243.252.9/ce-3354-webroot/5-Spreadsheets/ExampleUH_TransferFn.xls)
# 5. [ExtendedBase_DifferentStorm.xls](http://54.243.252.9/ce-3354-webroot/5-Spreadsheets/ExtendedBase_DifferentStorm.xls)
# 6. [ExtendedBase.xls](http://54.243.252.9/ce-3354-webroot/5-Spreadsheets/ExtendedBase.xls)
# 

# ## Outline
# 
# - Exercise 1 Construct DRH graphically and/or using a spreadsheet
# - Exercise 2 Construct DRH using spreadsheet for several different conditions
# 
# ---

# Typical Workflow:
#     
# 1. UH is usually for 1-hr **excess precipitation**.  Check the stated duration of the input (not the time base of the hydrograph, thats a different beast)
# 2. Is the hyetograph in 1-hr increments?  
#   - Yes, proceed to step 3
#   - No, convert supplied hyetograph into equivalent 1-hr increments (or whatever is dictated by the UH), return to beginning step 2
# 3. Has the loss function been applied?
#   - Yes, proceed to step 4
#   - No, apply loss function to each hyetograph increment, return to beginning step 3
# 4. On suitable chart (or in a spreadsheet, or in a script) plot each increment's response onto the chart - remember to lag the responses consistent with the increment timing.
# 5. Add up the responses for each time of interest (vertical additions if you will).  This result is the direct runoff hydrograph (DRH).

# ## Exercise 1
# 
# Determine the direct runoff hydrograph resulting from the rainfall pattern in Figure P2-2(a) using the triangular 1-hr UH given in  Fig. P2-2(b)
# 
# ![](Raro001.png)

# ![](BlankChart.png)

# Here's a spreadsheet approach
# 
# ![](ss14.1-1.png)
# 
# 1. [14.1-Spreadsheet](http://54.243.252.9/ce-3354-webroot/ce-3354-webbook-2024/my3354notes/lessons/14.1-UnitHydrographPractice/UH-INCLASS.xlsx) Choose TabSheet 14.1-1
# 
# ---

# ## Exercise 2.
# 
# Consider the watershed below.  Area A and B are identical in size, shape, slope, and channel length. 1-hr UH are supplied fro natural and developed conditions for both areas.
# 
# ![](Watershed.png)  
# 
# 
# ![](UHTable.png)
# 
# Determine:
# 1. Assuming natural conditions for both areas determine the outflow at point 1 if 2.5 in.hr of rain falls for 2 hrs.  Total loss is 1 in.
# 2. Assume area B is fully developed, area A remains au naturel.  Determine the outflow at point 1 if 2.0 in/hr of **excess rain** falls for 1 hrs.  
# 3. Repeat the above for both areas fully developed.
# 
# 

# ![](BlankChart.png)

# ![](ss14.1-2a.png)

# ![](ss14.1-2b.png)

# ![](ss14.1-2c.png)

# 1. [14.1-Spreadsheet](http://54.243.252.9/ce-3354-webroot/ce-3354-webbook-2024/my3354notes/lessons/14.1-UnitHydrographPractice/UH-INCLASS.xlsx)  Choose TabSheets 14.1-2(a),(b), or (c)

# In[ ]:




