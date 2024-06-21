#!/usr/bin/env python
# coding: utf-8

# # Rational Equation (Rainfall-Runoff) Model

# ## Background
# 
# The rational method is probably applied the most often by hydraulic and drainage engineers to estimate design discharges for small drainage areas. These design discharges are used to size a variety of drainage structures for small undeveloped and developed watersheds throughout the United States.
# 
# The rational method (Kuichling 1889) is expressed as,
# 
# $Q_p = m_0 C_{std} iA $ 
# 
# where 
# - $Q_p$ is peak discharge **at some point where flow is concentrated** (an inlet to a storm sewer, a culvert, an outlet from a small watershed, ... )
# - $m_0$ is a dimensional conversion factor ($\frac{1}{360} = 0.00278$ in SI units; $1.008$ in English units).
# - $C_{std}$ is a rational runoff coefficient (dimensionless) determined by the land-use characteristics in the watershed, 
# - $A$ is drainage area (hectares or acres), and
# - i is average intensity of rainfall ($mm/h$ or $in/h$) of a specified frequency (probability) for a duration equal to a characteristic time, $T_c$, of the drainage area. 
# 
# In the U.S., the customary units for the rational method are cubic feet per second (cfs) for $Q$, inches per hour (in/hr) for $i$, and acres for $A$. To be dimensionally consistent, a conversion factor of 1.0083 should be included to *convert* acre-inches per hour into cubic feet per second; however, this factor is generally neglected.
# 
# In this document, $C_{std}$ is the standard rational runoff coefficient that relates the ratio of input volume rate $iA$ to the output volume rate $Q_p$.
# 
# For development of the rational method, it is assumed that:
# 
# 1. The discharge concentrates/collects at the point of interest
# 1. The rainfall is uniform over the drainage area,
# 2. The peak rate of runoff can be reflected by the rainfall intensity averaged over a time period equal to the characteristic time3 of the drainage area,
# 3. The relative frequency (probability) of runoff is the same as the relative frequency (probability) of the rainfall used in the equation4,
# 4. The above formula implies that the peak discharge occurs when the entire area is contributing flow to the drainage outlet, that is, the peak flow will occur at the characteristic time Tc after the start of uniform rainfall. A uniform rainfall of a longer duration than Tc will not produce a greater peak flow but will only lengthen the discharge period, and
# 5. All runoff generation processes are incorporated into the runoff coefficient.
# 
# The conceptual runoff generation mechanism is illustrated in the Figure below for a continuous rainfall where discharge at the point of interest (watershed outlet) increases until an equilibrium value is reached where the excess rainfall rate and the discharge per unit area become equal. This figure in particular illustrates the fifth assumption, that is that rainfall over a period longer than $T_c$ has no effect on the discharge in the rational method model.
# 
# ![](RationalMethodConceptualProcess.png)
# 
# For small urban drainage designs, such as storm drains, the rational method is the common method for peak flow estimation in the United States (McPherson, 1969) despite criticism for over-simplified assumptions. The widespread use of the rational method can be explained by its simplicity, entrenchment in practice, extensive coverage in the literature, and lack of comparable simple-to-use alternatives (Haan and others, 1994).
# 
# The applicable area (over which the method can be applied) is generally restricted to less than one square mile (e.g. FHWA (1980)), and in urban jurisdictions to areas to less than 20 acres (Poertner, 1974), yet the idea of a runoff coefficient could certainly be extended to large basins 
# 
# :::{note}
# In this context these coefficients are not the same as the rational runoff coefficient, hence the use of the jargon "rational runoff coefficient"). 
# :::
# 
# From inspection of the equation, it is evident that $C$ is an expression of proportionality between rainfall intensity and peak discharge (flow rate). The theoretical range of values for $C$ is between 0 and 1. The typical whole watershed $C$ values (that is, $C$ values representing the integrated effects of various surfaces in the watershed and other watershed properties) are listed for different general land-use conditions in various design manuals and textbooks.
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
# 3. [Kuichling, E. (1889). “The relation between the rainfall and the discharge of sewers in populous areas.” Trans. ASCE, 20(1), 1–56. ](http://54.243.252.9/ce-3354-webroot/ce-3354-webroot-2024/3-Readings/kuichling89-c.pdf)
# 
# 4. Gupta pp. 711-724

# In[ ]:





# In[ ]:




