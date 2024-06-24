#!/usr/bin/env python
# coding: utf-8

# # 15. Unit Hydrographs - II (Synthesis)
# 
# Synthesis does not use rainfall-runoff data.
# 
# - Uses measurements on the watershed to postulate parameters of a parametric unit hydrograph.
# 
# ## Parametric Unit Hydrographs (in HEC-HMS)
# 
# HEC-HMS has several different UH models available (eg. NRCS DUH, Clark, etc.).
# These models are described by “parameters” 
# - NRCS (Tp or Tc)
# - Clark (Tc, R)
# Selection of the parameters selects the shape of the UH and the time base (or time to peak).
# The analyst can also enter an empirical (user specified) unit hydrograph.
# 
# Useful parametric models along with their parameters include:
# 
# - NRCS DUH : Tlag (Timing only)
# - Clark : Tc, and R (Timing and a storage-delay)
# - Snyder : Tlag, Cp (Timing and a peak rate factor)
# - Gamma : (User-Specified) Tc, K (Timing and a shape factor)
# 
# :::{note}
# Aalysis uses data (rainfall and runoff observations) to develop unit hydrograph models. Choices include:
# 
# Follow FHWA methods 
# - Essentially back-substitution or OLS
# 
# Use HEC-HMS and parametric UH, adjust values of parameters to fit observed runoff
# - Less tedious than back-substitution or OLS
# 
# Use HEC-HMS and a user supplied UH, adjust values of UH ordinates (and re-scale to maintain a unit response) to fit observed runoff
# - Less tedious than back-substitution or OLS
# :::
# 
# ## Example
# 
# Work the example(s) below:
# 
# [Cleveland, T. G. (2017) *Surface Water Hydrology Notes (Unit-Hydrographs in HEC-HMS) to accompany CE-3354*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering. Go to Slide 32](http://54.243.252.9/ce-3354-webroot/1-Lectures-2017/Lecture14.pdf)
# 
# A fully provisioned Windows Implementation of HEC-HMS is located at:
# 
# - server_name: **kittyinthewindow.ddns.net**
# - user_name: **texas-skew**
# - passwd: **peakfq73$hare**
# 
# Users must access using Remote Desktop Protocol (Built into Windows, Apple Store has a free Mac application).
# 
# Example powerpoint [DES-606-EX6](http://54.243.252.9/ce-3354-webroot/ce3354book/lessons/lesson10/Example6.ppt)
# 
# Data Files for Examples:
# 
# 1. [Example7.xls (Same as in Notes Above)](http://54.243.252.9/ce-3354-webroot/ce3354book/lessons/lesson10/Example7.xls)
# 1. [Precipitation data for Ash Creek 1972 5 October Storm (Elapsed time)](http://54.243.252.9/ce-3354-webroot/ce3354book/lessons/lesson10/RAIN-19721005-RR.xls)
# 2. [Runoff data for Ash Creek 1972 5 October Storm (Elapsed time)](http://54.243.252.9/ce-3354-webroot/ce3354book/lessons/lesson10/FLOW-19721005-RR.xls)
# 3. [Initial Abstraction - Constant Loss Worksheets](http://54.243.252.9/ce-3354-webroot/ce3354book/lessons/lesson10/InitialAbstractionConstantLossModel.xls)
# 4. [Ash Creek 1978 21 May Storm](http://54.243.252.9/ce-3354-webroot/ce3354book/lessons/lesson10/STA08057320_HECHMSFORMAT_1978-0521.xls)
# 
# ## References
# 
# 1. Gupta pp 343-372
# 
# 
# 
# 

# In[ ]:




