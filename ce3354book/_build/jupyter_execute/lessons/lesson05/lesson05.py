#!/usr/bin/env python
# coding: utf-8

# # Streamflow Data Modeling
# 
# 

# ## Streamflow Measurement

# ## Flood Frequency Analysis (B17C)
# 
# Flood hydrology is typically studied using the annual peak streamflow data collected by the U.S. Geological Survey (USGS) at streamgages. Hydraulic design engineers need standard of practice guidance for various tasks involving the analysis and application peak streamflow information. Analyses of this information materially influences bridge design, operational safety of drainage infrastructure, flood-plain management, and other decisions affecting society.
# 
# Bulletin 17B was the standard of practice for decades, recently superceded by Bulletin [17C](https://pubs.usgs.gov/tm/04/b05/tm4b5.pdf).  These and similar tools relate certain statistical metrics (mean, variance, and skew) to a prescribed probability distribution function (Log-Pearson Type III) to extrapolate (predict) the magnitude of rare (low probability) events to inform engineering design.
# 
# Tasker and Stedinger (1986) developed a weighted least squares (WLS) procedure for estimating regional skewness coefficients based on sample skewness coefficients for the logarithms of annual peak-streamflow data. Their method of regional analysis of skewness estimators accounts for the precision of the skewness estimator for each streamgage, which depends on the length of record for each streamgage and the accuracy of an ordinary least squares (OLS) regional mean skewness. These methods automated much of B17B process and were incorporated into software used for streamgage analysis.  
# Recent updates to B17B in terms of software improvements and different handling of gage statistics (in particular EMA) are incorporated into the current tool [B17C](https://pubs.usgs.gov/tm/04/b05/tm4b5.pdf)
# 
# *Summary*
# 
# - B17C is a report containing methods for estimating magnitudes of rere events
# - The methods are incorporated into software products such as [PeakFQ 7.3](https://pubs.usgs.gov/tm/2006/tm4b4/tm4b4.pdf) and [HEC-SSP](https://www.hec.usace.army.mil/software/hec-ssp/)
# 
# 
# 

# ## Flow Duration Curves

# ## Regional Regression Equations

# ## References
# 
# 1. [Cleveland, T. G. (2017) *Engineering Hydrology Notes to Accompany CE 3354 (Bulletin 17B)*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/1-Lectures-2017/Lecture07.pdf)
# 
# 2. [Cleveland, T. G. (2017) *Engineering Hydrology Notes to Accompany CE 3354 (Bulletin 17B)*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/1-Lectures-2017/Lecture08.pdf)
# 
# 3. [Generalized Skew Update and Regional Study of Distribution Shape for Texas Flood Frequency Analyses](https://dataverse.tdl.org/dataset.xhtml?persistentId=doi:10.18738/T8/SVLCOQ)

# In[ ]:




