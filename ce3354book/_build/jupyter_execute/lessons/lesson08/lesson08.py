#!/usr/bin/env python
# coding: utf-8

# # Infiltration Models
# 
# Examination of various process models at
# 
# [Cleveland, T. G. (2020) *Surface Water Hydrology Notes (Infiltration) to accompany CE-5361*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/1-Lectures-2020/lesson07/Lesson07.pdf)
# 
# ## HEC-HMS Loss Models
# 
# >A sub**basin** element conceptually represents infiltration, surface runoff, and
# subsurface processes interacting together, the actual infiltration calculations are
# performed by a loss method contained within the subbasin. A total of twelve different
# loss methods are provided. Some of the methods are designed primarily for
# simulating events while others are intended for continuous simulation. All of the
# methods conserve mass. That is, the sum of infiltration and precipitation left on the
# surface will always be equal to total incoming precipitation.
# 
# >The inputs for each loss method are presented on a separate Component Editor
# from the subbasin element editor. The "Loss" editor is always shown next to the
# "Subbasin" editor. If the kinematic wave transform method is selected, there may be
# two loss editors, one for each runoff plane. The information shown on the loss editor
# will depend on which method is currently selected
# 
# A fully provisioned Windows Implementation of HEC-HMS is located at:
# 
# - server_name: **kittyinthewindow.ddns.net**
# - user_name: **texas-skew**
# - passwd: **peakfq73$hare**
# 
# Users must access using Remote Desktop Protocol (Built into Windows, Apple Store has a free Mac application).
# 
# - Use the Hardin Creek Project to explore different loss models.
# 
# Recomended Loss models for semester project are CN model or Green-Ampt.  These are easiest to parameterize from available data sources for the project and should be adequate for the problem statement.
# 
# 

# ## References
# 
# 1. [Cleveland, T. G. (2020) *Surface Water Hydrology Notes (Infiltration) to accompany CE-5361*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/1-Lectures-2020/lesson07/Lesson07.pdf)
# 2. [Green-Ampt Spreadsheet (Excel)](http://54.243.252.9/ce-3354-webroot/1-Lectures-2020/lesson07/ce5361_green_ampt.xlsx) Right-Click "Save As..."
