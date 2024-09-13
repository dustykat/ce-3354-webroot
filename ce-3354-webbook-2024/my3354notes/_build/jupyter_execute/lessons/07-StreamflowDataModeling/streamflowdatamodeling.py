#!/usr/bin/env python
# coding: utf-8

# # 7. Streamflow Data Sources and Estimation

# :::{admonition} Course Website
# [Link to Course Website](http://54.243.252.9/ce-3354-webroot/)
# :::
# 
# 

# ---
# ## Readings
# 
# 1. [Chow, V.T., Maidment, D.R., Mays, L.W., 1988, Applied Hydrology:  New York, McGraw-Hill. **pp. 1-12** ](http://54.243.252.9/ce-3354-webroot/3-Readings/CMM1988/Applied%20Hydrology%20VT%20Chow%201988.pdf) 
# 
# 1. [Cleveland, T. G. (2017) *Engineering Hydrology Notes to Accompany CE 3354 (Bulletin 17B 1 )*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/1-Lectures-2017/Lecture07.pdf)
# 
# 2. [Cleveland, T. G. (2017) *Engineering Hydrology Notes to Accompany CE 3354 (Bulletin 17B 2)*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/1-Lectures-2017/Lecture08.pdf)
# 
# 3. [See pp. 33-39 CMM for explaination of Manning’s equation](http://54.243.252.9/ce-3354-webroot/3-Readings/CMM1988/)
# 
# 4. [See 7-31 TxDOT HDM for a description of slope-area (slope-conveyance) method](http://54.243.252.9/ce-3354-webroot/3-Readings/TXDOT-HYDM-2014/txdot-hdm-2014.pdf)
# 
# 44. [Develop a Generalized Skew Update and Regional Study of Other Measures of Distribution Shape for Texas Flood Frequency Analyses (Project Sumary Report)](https://library.ctr.utexas.edu/hostedpdfs/texastech/psr/0-6977-s.pdf)
# 
# 5. [Generalized Skew Update and Regional Study of Distribution Shape for Texas Flood Frequency Analyses](https://dataverse.tdl.org/dataset.xhtml?persistentId=doi:10.18738/T8/SVLCOQ)
# 
# 6. [England, J.F. Jr., Cohn, T.A., Faber, B.A., Stedinger, J.R., Thomas Jr., W.O., Veilleux, A.G., Kiang, J.E., and Mason, R.R.Jr., 2018, Guidelines for Determining Flood Flow Frequency—Bulletin 17C: U.S. Geological Survey Techniques andMethods, book 4, chap. B5, 146 p.,](https://doi.org/10.3133/tm4B5)
# 
# 4. [Jamie Chan (2014) Learn Python in One Day and Learn It Well. LCF Publishing. Kindle Edition. ](http://www.learncodingfast.com/python)
# 
# 5. [Grus, Joel. Data Science from Scratch: First Principles with Python. O'Reilly Media. Kindle Edition. ](http://safaribooksonline.com)
# 
# 6. [Christian, B, and Griffiths Tom (2016) Algorithms to live by: The computer science of human decisions. Henry Holt and Company, ISBN 9781627790369 (hardcover)|ISBN 9781627790376 (electronic book)](https://www.amazon.com/Algorithms-Live-Computer-Science-Decisions/dp/1627790365)
# 
# 7. https://www.amazon.com/Distributional-Statistics-Environment-Statistical-Computing/dp/1463508417
#     
# 9. https://www.astroml.org/book_figures/chapter3/fig_gamma_distribution.html
# 
# 10. https://www.inferentialthinking.com/chapters/10/Sampling_and_Empirical_Distributions.html
# 
# 11. https://www.inferentialthinking.com/chapters/15/Prediction.html

# ## Videos
# 
# 1. [Collecting water data for the U.S.](https://www.youtube.com/watch?v=g_s_toqrYVM)
# 2. [Hydroacoustics for Collecting Streamflow Data](https://www.youtube.com/watch?v=usCTuMnXGQE)
# 3. [How to look at and download streamflow data from the USGS NWIS website](https://www.youtube.com/watch?v=FeRzzQA0I7k)
# 4. [Surface Water Data of any location of the World for free ](https://www.youtube.com/watch?v=NKsE06fvF10)
# 5. [Precipitation Runoff Modeling System (PRMS) Streamflow Modules ](https://www.youtube.com/watch?v=OAozlSQ_fIg)
# 6. [Improved process based streamflow simulation through ensemble and stochastic data driven approaches](https://www.youtube.com/watch?v=aXq-QnYYc74)
# 7. [Hydrology - Statistical Hydrology 2 (go to time stamp 47:00 to get to regionalization) ](https://www.youtube.com/watch?v=ERSBlzcbHjs&t=11s)
# 8. [StreamStats: Determining Magnitude and Frequency of Floods in California (Specific to California, but nice discussion on regionalization)](https://www.youtube.com/watch?v=wG-F5fZFOhw&t=297s)
# 9. [Watershed Delineation and TR-55 for runoff hydrograph](https://www.youtube.com/watch?v=pzpfCvNBXI0&list=PLQv9IPdrtoKgxLQih9UXNbFqXLeJvKEaz&index=29)
# 19. [PeakFQ (Version 7.1) Flood-Frequency Analysis Demo](https://www.youtube.com/watch?v=w-j2S3APUgk)
# 21.  [CE 3354 Demonstrate PeakFQ using Beargrass Creek Data](https://youtu.be/sm2-4AI6WU8 )
# 10. [Bulletins 17B and 17C 1](https://www.youtube.com/watch?v=yfs3oaF2F-w)
# 11. [Bulletins 17B and 17C 2](https://www.youtube.com/watch?v=yfs3oaF2F-w)
# 11. [Bulletins 17B and 17C 3](https://www.youtube.com/watch?v=cfaVjfms9ss)
# 11. [Regional Skew 1](https://www.youtube.com/watch?v=NI9Ui4x_HJk)
# 12. [HEC-SSP Bulletin 17C Flood Frequency Analysis Tutorial](https://www.youtube.com/watch?v=Wc0qaDaBjFE)
# 13. [Index Flood Regionalization Pt I](https://www.youtube.com/watch?v=7psZWEhm4Kw)
# 13. [Index Flood Regionalization Pt II](https://www.youtube.com/watch?v=De4o8S2ohLA)
# 14. [Index Flood Regionalization Pt III](https://www.youtube.com/watch?v=hjdnlbxrje8)
# 15. [Index Flood Regionalization Pt IV](https://www.youtube.com/watch?v=8HkztqnptIA)
# 16. [Uncertainty in Frequency Estimates 1](https://www.youtube.com/watch?v=3Qtep3SdzDw)
# 17. [Uncertainty in Frequency Estimates 2](https://www.youtube.com/watch?v=qyJSiWXd5fc)
# 18. [Uncertainty in Frequency Estimates 3](https://www.youtube.com/watch?v=86QY-5bH6sA)
# 21. [0-6977 Training Video for Gage 08148500](https://youtu.be/R_nSTyMnlsE )
# 22. [0-6977-Prototype-Remote-Tools-Intro](https://youtu.be/y_vK3sWqnHw )
# 23. [0-6977 Training Video for Gage 08167000 using Fig 4.6](https://youtu.be/YQ1YJFUrwYE )
# 24. [0-6977 Training Video for Gage 08080750](https://youtu.be/ZUztiBLWFVs )
# 
# 
# 
# 

# ## Outline
# - Streamflow Measurement
# - Streamflow (gage) Data
# - Estimation of Streamflow
#  - Watershed Characteristics
#  - Regional Regression Equations
#  - B17C
# ---

# ## Streamflow Measurement
# 
# Streamflow is measured by a variety of gaging technologies.  
# 
# - Continuous record (usually stage, then rated to produce discharge)
#    - Located at control section if possible
# 
# - Crest-Stage (captures peak stage)
#    - Uses slope-area to estimate discharge
#    - Post-event site visit required to survey debris-line as independent check of estimate
# 
# **Continuous gages** use some kind of stilling well, and transducers to measure stage and send to satellite. During visits, a nearby staff gage is read to independently validate the transducer readings
# 
# ![](continuousgage.png)
# 
# **Crest-Stage** gagues usually consist of a vertical pipe with holes in bottom – becomes a stilling well.
# Inside a staff gage and small amount of cork “flour” records water surface elevation.
# - A hydrographer visits site routinely (and after major events) and records cork elevation and re-sets gage.
# - The elevations are marked on a staff inside the pipe with pencil (and dated)
# - Slope area method between several nearby pipes is used to estimate discharge
# 
# ![](creststagegage.png)
# 
# ### Slope Area Method
# 
# Application of Manning’s equation, using the slope of the water surface as the friction slope, and the stage geometry at measured cross sections.
# 
# $$Q=\frac{1.49}{n}~A~R^{2/3}~S^{1/2}$$
# 
# Recall the factor 1.49 is for US Customary units, 1.0 is used if terms are expressed in SI units.
# 
# - [See pp. 33-39 CMM for explaination of Manning’s equation](http://54.243.252.9/ce-3354-webroot/3-Readings/CMM1988/)
# - [See 7-31 TxDOT HDM for a description of slope-area (slope-conveyance) method](http://54.243.252.9/ce-3354-webroot/3-Readings/TXDOT-HYDM-2014/txdot-hdm-2014.pdf)
# - [MEASUREMENT OF PEAK DISCHARGE by the SLOPE AREA METHOD](https://pubs.usgs.gov/twri/twri3-a2/pdf/twri_3-A2_a.pdf)
# - [Theory of the Slope-Area Method (Video)](https://www.youtube.com/watch?v=5Rqy8_ZOHZw)
# - [Slope Area Calculator](http://54.243.252.9/toolbox/swhydraulics/SlopeAreaSI/SlopeAreaSI.html)
# - [slopearea.sdsu.edu ](https://ponce.sdsu.edu/slope_area_method.php)

# ## Streamflow Data
# 
# Data sources for streamflow include:
# - USGS NWIS (Website)
# - IBWC
# - Older “paper-based” records
# - Local gage networks
# 
# Illustrative example using USGS NWIS
# 
# - Navigate to landing page for state of interest
# 
# ![](query-nwis.png)
# 
# 
# - Locate site of interest, or something stupid close
# 
# ![](nwis-buffalo.png)
# 
# - Download desired record(s)
# 
# ![](nwis-buffalo2.png)
# 
# - Typical file structure 
# 
# ![](nwis-buffalo3.png)

# ## Watershed Characteristics
# 
# One tool in applied hydrology is to relate measurable watershed properties to streamflow discharge.  
# 
# What characteristics influence runoff?
# - Where you are
# - How large an area
# - Gradient
# 
# ![](devilsriver.png)
# 
# More detailed list might include:
# - Width, shape
# - Elevation: minimum, maximum + slope
# - Roughness: Channels, overbanks
# - Geology and soils
# - Climate
# - Vegetation
# - Land use, including urbanization and imperviousness
# - Controls: Dams, gates, diversions, channel rectification
# 
# This is part of the motivation for learning how to delineate a watershed.
# 
# Supporting data sources include:
# - USGS quadrangle maps
# - Aerial photos
# - Satellite imagery
# - NRCS soil surveys
# - Field surveys
# - Previous investigations
# 
# ![](nrcs-soilsmap.png)
# 

# ## Regional Regression Equations
# 
# Where sufficient data exist, one technique for gross estimates of streamflow based largely on watershed area, rainfall input, and location are regional regression equations.  These exist in some fashion for each state in the USA, and most terrortories (Puerto Rico, Guam ...).  They probably exist for many other countries, and are all obtained in a similar fashion.
# 
# The equations are constructed by first fitting an appropriate probability distribution to observations at a gaged location (station flood frequency). Then the station flood frequency curves are used as surrogate observations (at a specified AEP) to relate discharge to select geomorphic variables:
# 
# $$(\bar Q_{AEP} -\beta_0 - \beta_1 A - \beta_2 S - \beta_3 MAP \dots)^2= \bar \epsilon$$
# 
# The “betas” are obtained by trying to make “epsilon” small, the AREA, SLOPE, and other watershed characteristics are the explainatory variables.
# 
# The resulting equations are typically expressed in a power-law form (rather that the linear combination above) for actual application
# 
# $$Q_{AEP,\text{Estimate}} = \beta_0 (\text{AREA})^{\beta_1} (\text{SLOPE})^{\beta_2} (\text{MAP})^{\beta_3}$$
# 
# For example in Texas the following guidance is found in Chapter 4 of the Texas Hydraulics Manual:
# 
# ![](THMregression.png)
# 
# The actual equations in current use are
# 
# ![](RegressionEquations.png)
# 
# Two needed input values are the mean annual precipitation (MAP) and the Omega-EM factor both of which are mapped and available on the almighty internet
# 
# - [Texas Mean Annual Precipitation](http://onlinemanuals.txdot.gov/txdotmanuals/hyd/images/Fig4-6.png)
# - [Texas Omega-EM Map](http://onlinemanuals.txdot.gov/txdotmanuals/hyd/OmegaEM_black_cropped.pdf)
# 
# Using the table above and the known equation structure it is fairly straightforward to create a tool for routine use in either a spreadsheet form or in python
# 
# - [Texas Regression Equation Spreadsheet](http://54.243.252.9/ce-3354-webroot/ce3354book/lessons/lesson05/TexasRegionalRegressionTool.xlsx)
# - [On-Line Texas Regression Equation Tool](http://54.243.252.9/toolbox/hydrology/TXRegression/TXRegression.html)
# 
# Illustrative example for the Hardin Branch location (near Eden Texas).  
# 
# Apply the Regression Equations for the Hardin Branch Watershed – provide a comparative estimate to help guide the project
# 
# - AREA = 17 sq. mi.
# - MAP = 23 inches/year
# - OmegaEM = 0.345
# - Slope = 0.0048
# 
# 
# Below is result using the spreadsheet tool 
# ![](texasregional.png)
# 
# And the on-line web interface
# ![](texasregionalonline1.png)
# 
# and the on-line results
# ![](texasregionalonline2.png)

# ## Gage Transposition Approach
# 
# A related (to regression methods) method that is often quite useful is a [Gage Transposition Approach](https://onlinemanuals.txdot.gov/TxDOTOnlineManuals/TxDOTManuals/hyd/statistical_analysis_of_stream_gauge_data.htm#i1106111).
# 
# If gauge data are not available at the design location, discharge values can be estimated by transposition if a peak flow-frequency curve is available at a nearby gauged location. This method is appropriate for hydrologically similar watersheds that differ in area by less than 50 percent, with outlet locations less than 100 miles apart.
# 
# An estimate of the desired AEP peak flow at the ungauged site is provided by <br>
# 
# $Q_1 = Q_2(\frac{A_1}{A_2})^{0.5}  $<br>
# 
# Where:<br>
# 
# - $Q_1$ = Estimated AEP discharge at ungauged watershed 1
# - $Q_2$ = Known AEP discharge at gauged watershed 2
# - $A_1$ = Area of watershed 1
# - $A_2$ = Area of watershed 2
# 
# Transposition of peak flow is demonstrated with the following example. A designer requires an estimate of the 1% AEP streamflow at an ungauged location with drainage area of 200 square miles. A nearby (within 100 miles) stream gauge has a hydrologically similar drainage area of 450 square miles. The 1% AEP peak streamflow at the gauged location is 420 cfs based on the peak flow-frequency curve developed for that location. Substituting into Equation 4-10 results in 280 cfs as an estimate of the 1% AEP peak discharge at the ungauged location:
# 
# If flow-frequency curves are available at multiple gauged sites, Equation 4-10 can be used to estimate the desired peak AEP flow from each site. Then, with judgment and knowledge of the watersheds, those estimates could be weighted to provide an estimate of the desired AEP flow at the ungauged location. This process should be well documented.
# 
# Design of a storage facility, such as a detention pond, may require estimates of AEP flows for longer durations. If a flow-frequency curve for longer flow duration is available at a nearby gauged location, then the following equation, based on an analysis of mean-daily flows , may be used for transposition:
# 
# $Q_1 = Q_2(\frac{A_1}{A_2})^{0.9}  $<br>
# 
# :::{note} 
# This section is largely based upon [Asquith, W.H., Roussel, M.C., and Vrabel, Joseph, 2006, Statewide analysis of the drainage-area ratio method for 34 streamflow percentile ranges in Texas: U.S. Geological Survey Scientific Investigations Report 2006–5286, 34 p.,1 appendix.](https://pubs.usgs.gov/sir/2006/5286/pdf/sir2006-5286.pdf).  A key observation is that the transposition is a power-law model to relate known to unknown locations, and the power ranges from 1/2 to nearly 1. 
# :::

# ## Flood Frequency Analysis (B17C)
# 
# Flood hydrology is typically studied using the annual peak streamflow data collected by the U.S. Geological Survey (USGS) at streamgages. Hydraulic design engineers need standard of practice guidance for various tasks involving the analysis and application peak streamflow information. Analyses of this information materially influences bridge design, operational safety of drainage infrastructure, flood-plain management, and other decisions affecting society.
# 
# Bulletin 17B was the standard of practice for decades, recently superceded by Bulletin [17C](https://pubs.usgs.gov/tm/04/b05/tm4b5.pdf).  These and similar tools relate certain statistical metrics (mean, variance, and skew) to a prescribed probability distribution function (Log-Pearson Type III) to extrapolate (predict) the magnitude of rare (low probability) events to inform engineering design.
# 
# Tasker and Stedinger (1986) developed a weighted least squares (WLS) procedure for estimating regional skewness coefficients based on sample skewness coefficients for the logarithms of annual peak-streamflow data. Their method of regional analysis of skewness estimators accounts for the precision of the skewness estimator for each streamgage, which depends on the length of record for each streamgage and the accuracy of an ordinary least squares (OLS) regional mean skewness. These methods automated much of B17B process and were incorporated into software used for streamgage analysis.  
# Recent updates to B17B in terms of software improvements and different handling of gage statistics (in particular EMA) are incorporated into the current tool [B17C](https://pubs.usgs.gov/tm/04/b05/tm4b5.pdf)
# 
# :::{admonition} Summary
# - B17C is a report containing methods for estimating magnitudes of rare events
# - The methods are incorporated into software products such as [PeakFQ 7.3](https://pubs.usgs.gov/tm/2006/tm4b4/tm4b4.pdf) and [HEC-SSP](https://www.hec.usace.army.mil/software/hec-ssp/)
# 
# Software is employed because the Pearson Type III distribution is  applied to model streamflow, precipitation extremes, and flood frequency because it can accommodate the **skewness** (3rd moment) observed in these datasets. For example, the Log-Pearson Type III distribution, where data is logarithmically transformed, is used by the U.S. Geological Survey (USGS) for flood frequency analysis, helping hydrologists estimate the probability of extreme flood events (e.g., 100-year floods).
# 
# By adjusting parameters such as mean, variance, and skewness, Pearson distributions can fit a wide range of data types - but the fitting itself is complex and requires a lot of tedious computations - just the thing for a computer program to do the heavy lifting.  The programs above replace older tabular methods that were prone to calculation errors when done by hand, and interpretation errors from by-hand plotting of the results.
# :::
# 
# ### Illustrative Example using Beargrass creek
# 
# Demonstrate using Bearcreek as an example.  Beargrass creek is not a real site, therefore is not in the NWIS database, so we have to modify the file to be readable in PeakFQ.
# 
# A modified version is at [BearGrass-B17B.txt](http://54.243.252.9/ce-3354-webroot/ce3354book/lessons/lesson05/BearGrass-B17B.txt)
# 
# A fully provisioned Windows Implementation of B17C is located at:
# 
# - server_name: **kittyinthewindow.ddns.net**
# - user_name: **texas-skew**
# - passwd: **peakfq73$hare**
# 
# Users must access using Remote Desktop Protocol (Built into Windows, Apple Store has a free Mac application)
# 
# - [Video to Demo PeakFQ on Beargrass Creek (YouTube)](https://youtu.be/sm2-4AI6WU8)
# 
# In class access [Brady Creek](https://waterdata.usgs.gov/nwis/inventory?agency_code=USGS&site_no=08145000) (close to Hardin Creek)

# ## Flow Duration Curves
# 
# The [flow-duration curve](https://pubs.er.usgs.gov/publication/wsp1542A) is a cumulative frequency curve that shows the percent of **time** specified discharges were equaled or exceeded during a given period. 
# It combines in one curve the flow characteristics of a stream throughout the range of discharge, without regard to the sequence of occurrence. If the period upon which the curve is based represents the long-term flow of a stream, the curve may be used to predict the distribution of future flows for water- power, water-supply, and pollution studies. 
# 
# [OSU Flow Duration Curve Mechanics](https://streamflow.engr.oregonstate.edu/analysis/flow/index.htm)
