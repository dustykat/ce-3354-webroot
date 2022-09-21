#!/usr/bin/env python
# coding: utf-8

# # Rational Equation (Rainfall-Runoff) Model
# 
# A rainfall-runoff model is a mathematical model describing the rainfall–runoff relations of a rainfall catchment area, drainage basin or watershed. It produces a runoff hydrograph in response to rainfall inputs, represented by a hyetograph. In other words, the model calculates the conversion of rainfall into runoff.
# 
# A well known rainfall-runoff model is the Rational Equation model but it has limited applicability.
# 
# A slightly more general rainfall-runoff model is the linear reservoir, but it also has limited applicability.
# 
# :::{note}
# The limited appliciability is not problematic, and is intended to convey that you would use the model for situations where it is explicitly appropriate and recognize that outside its limits you are engaging in glorified guessing.
# :::
# 
# The rainfall-runoff model with a non-linear reservoir is considered more universally applicable, but still it holds only for catchments whose surface area is limited by the condition that the rainfall can be considered more or less uniformly distributed over the area. 
# 
# The maximum size of the watershed then depends on the rainfall characteristics of the region. When the study area is too large, it can be divided into sub-catchments and the various runoff hydrographs may be combined using flood routing techniques.
# 
# Rainfall-runoff models need to be calibrated before they can be used.

# ## The Rational Equation -- A simplistic method for small areas
# 
# The rational method likely is the applied method used most often by hydraulic and drainage engineers to estimate design discharges for small watersheds. These design discharges are used to size a variety of drainage structures for small undeveloped and developed watersheds throughout the United States.
# 
# The rational method (Kuichling 1889) computes the peak discharge, Qp (in $\frac{m^3}{s}$ in SI units or $\frac{ft^3}{s}$ in English units), using:
# 
# $$ Qp = m_0 CIA$$
# 
# where <br>$C$ = runoff coefficient (dimensionless), <br>$I$ = rainfall intensity
# ($mm/h$ or $in/h$) over a critical period of storm time (typically taken as the time of concentration, $T_ C$),<br>$A$ = drainage area (hectares or acres), and <br>$m_0$ = dimensional correction factor ($\frac{1}{360} = 0.00278$ in SI units; $1.008$ in English units).
# 
# From inspection of the equation, it is evident that $C$ is an expression of rate proportionality between rainfall intensity and peak discharge (flow rate). The theoretical range of values for $C$ is between 0 and 1. The typical whole watershed $C$ values (that is, C values representing the integrated effects of various surfaces in the watershed and other watershed properties) are listed for different general land-use conditions in various design manuals and textbooks.
# 
# An on-line $Q_p$ calculator has links to one such table. 
# 
# - [Rational Equation Model US Customary](http://54.243.252.9/toolbox/hydrology/RationalUS/RationalUS.html)
# - [Rational Equation Model SI](http://54.243.252.9/toolbox/hydrology/RationalSI/RationalSI.html)
# 
# The [Texas Hydraulic Design Manual](http://onlinemanuals.txdot.gov/txdotmanuals/hyd/rational_method.htm) contains a useful discussion on appliciability and use of the Rational Method in drainage design.

# ### Time of Concentration
# 
# The time of concentration is the crucial element of the Rational Equation (notably actually absent in an explicit sense from the equation).
# 
# - The value of $T_C$ is important in rational method for estimating rainfall intensity.
# - It is also used in many other hydrologic models to quantify the watershed response time.
# 
# Time of concentration $T_C$ is the time required for an entire watershed to contribute to runoff at the point of interest for hydraulic design. It is calculated as the time for runoff to flow from the most hydraulically remote point of the drainage area to the point under investigation.
# 
# Travel time and $T_C$ are functions of length and velocity for a particular watercourse.
# 
# - A long but steep flow path with a high velocity may actually have a shorter travel time than a short but relatively flat flow path.
# - There may be multiple paths to consider in determining the longest travel time.
# - The designer must identify the flow path along which the longest travel time is likely to occur.
# 
# Various Methods to Estimate $T_C$ include:
# 
# - [CMM pp. 500-501](http://54.243.252.9/ce-3354-webroot/3-Readings/CMM1988/) has several formulas.
# - [HDS-2 pp. 2-21 to 2-31](http://54.243.252.9/ce-3354-webroot/3-Readings/FHWAHighwayHydrology/FHWA-NHI-02-001.pdf) has formulas and examples.
# - [LS pp. 196-198](http://54.243.252.9/ce-3354-webroot/3-Readings/LS1973/linear-systems-hydrology-dooge.pdf) has several formulas.
# 
# Some simple useful methods are examined in
# 
# - [Cleveland, T. G. (2017) *Engineering Hydrology Notes to Accompany CE 3354 (Rational Equation, HEC-HMS)*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/1-Lectures-2017/Lecture09.pdf)  
# 
# The tools referenced in the above document are located below:
# 
# - NRCS Upland (uses the graph pg 720 of Gupta). [NRCS-Upland.xls](http://54.243.252.9/ce-3354-webroot/5-Spreadsheets/NRCS-Upland.xls); [NRCS-Upland.xlsx](http://54.243.252.9/ce-3354-webroot/5-Spreadsheets/NRCS-Upland.xlsx)
# - Kerby-Kirpich [Kerby-Kirpich.xls](http://54.243.252.9/ce-3354-webroot/5-Spreadsheets/KerbyKirpich-US.xls);[Kerby-Kirpich.xlsx](http://54.243.252.9/ce-3354-webroot/5-Spreadsheets/KerbyKirpich-US.xlsx)
# - NRCS Velocity [TXDOT-TIME-OF-CONCENTRATION-NRCS.xlsx](http://54.243.252.9/ce-3354-webroot/5-Spreadsheets/TXDOT-TIME-OF-CONCENTRATION-NRCS.xlsx)
# 
# 

# ## References
# 
# 1. [Cleveland, T. G. (2017) *Engineering Hydrology Notes to Accompany CE 3354 (Rational Equation, HEC-HMS)*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/1-Lectures-2017/Lecture09.pdf)
# 
# 1. [Subdivision of Texas Watersheds for Hydrologic Modeling](http://54.243.252.9/about-me-webroot/about-me/MyWebPapers/project_reports/0-5822-1/)
# 
# 2. [Rate-Based Estimation of the Runoff Coefficients for Selected Watersheds in Texas](http://54.243.252.9/ce-3354-webroot/3-Readings/RateBasedC/Rate-Based-C-Texas.pdf)
# 
# 3. Kuichling, E. (1889). “The relation between the rainfall and the discharge of sewers in populous areas.” Trans. ASCE, 20(1), 1–56.
# 
# 4. Gupta pp. 711-724
