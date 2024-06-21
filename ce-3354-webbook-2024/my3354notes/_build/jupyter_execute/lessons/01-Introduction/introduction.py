#!/usr/bin/env python
# coding: utf-8

# # 1. Introduction

# 

# :::{admonition} Course Website
# [Link to Course Website](http://54.243.252.9/ce-3354-webroot/)
# :::
# 
# 

# ---
# ## Readings
# 
# 1. [Ojha, Chandra & Berndtsson, R. & Bhunya, P.K.. (2008). Engineering Hydrology. Chapter 1 (Local Copy from https://www.researchgate.net/publication/264895381_Engineering_hydrology)](http://54.243.252.9/ce-3354-webroot/3-Readings/EngineeringHydrology/EngineeringHydrology-11-33.pdf)  
# 
# 1. [Chow, V.T., Maidment, D.R., Mays, L.W., 1988, Applied Hydrology:  New York, McGraw-Hill. **pp. 1-12** ](http://54.243.252.9/ce-3354-webroot/3-Readings/CMM1988/Applied%20Hydrology%20VT%20Chow%201988.pdf) 
# 
# 2. Brutsaert,  W.  2005.  Hydrology  :   An  Introduction  (8th  printing),  Cambridge  University Press. NewYork.
# 
# 3. [Dooge, J.C.I. 1973. Linear Theory of Hydrologic Systems. ARS Technical Bulletin No. 1468.US Department of Agriculture, Washington, D.C. **pp. 1-40**](http://54.243.252.9/ce-3354-webroot/3-Readings/LS1973/linear-systems-hydrology-dooge.pdf) 
# 
# 4. [Richard H. McCuen, Peggy A. Johnson, Robert M. Ragan, 2002. Highway Hydrology; Hydraulic  Design  Series  Number  2,  Second  Edition.  Federal  Highway  Administration,  National Highway Institute, 4600 North Fairfax Drive, Suite 800, Arlington, Virginia 22203. **pp. 1-1 to 1-9**](http://54.243.252.9/ce-3354-webroot/3-Readings/FHWAHighwayHydrology/FHWA-NHI-02-001.pdf) 
# 
# 5. [Definitions  from various sources](http://54.243.252.9/ce-3354-webroot/3-Readings/HydrologyDefinitions/hydrology-define.pdf)
# 
# 6. [Wisler, C.O, and Brater, E.F. 1949. "Hydrology" John Wiley and Sons, New York **pp. 1-14**](http://54.243.252.9/ce-3354-webroot/3-Readings/OlderHydrologyDescription/reading-definition-hydrology.pdf) 
# 
# 7. [McCuen XXXX. Hydrologic Analysis and Design ... **pp. 2-12** ](http://54.243.252.9/ce-3354-webroot/3-Readings/McCuen-WaterBudget/mccuen-reading-water-budget.pdf)
# 
# 8. [Heath, R.C., 1983. Basic ground-waterhydrology: U.S. Geological Survey Water-SupplyPaper 2220, **pp. 1-5**](http://54.243.252.9/ce-3354-webroot/3-Readings/USGS-WSP2020-GroundwaterHydrology/usgs-wsp-2020.pdf) 
# 
# 9. [Viessman,W., Knapp, J.W., Lewis, G. L., and Harbaugh, T.E. 1977. "Groundwater Hydrology – Chapter 8" in *Introduction to Hydrology* 2ed. IEP Publishers, New York, **pp. 291-342**](http://54.243.252.9/ce-3354-webroot/3-Readings/Groundwater-Viessman/GroundwaterHydrology.pdf) 
# 
# 10. [Wisler, C.O, and Brater, E.F. 1949. "Hydrology" John Wiley and Sons, New York **pp. 198-272**](http://54.243.252.9/ce-3354-webroot/3-Readings/Groundwater-Wisler&Brater/Groundwater-Wisler.pdf) 
# 

# ## Videos
# 
# 

# ## Outline
# - Course Resources
# - Essential Knowledge, Skills, and Abilities for Practical Engineering Hydrology
# - Surface and Groundwater Hydrology Concepts

# ## Course Resources
# - [Syllabus](http://54.243.252.9/ce-3354-webroot/0-Syllabus/)
# 
# - Software 
# 
# - Tour of Blackboard:
# 

# ---
# 
# ## Essential Knowledge, Skills, and Abilities for Practical Engineering Hydrology
# 
# ChatGPT 4.0 beta suggests the list below as the most important (highest probability in its database) topics in the currect practice of Hydrology and Hydraulics:
# 
# - Hydrological Processes: Understanding of various hydrological processes such as precipitation, evaporation, infiltration, runoff, and groundwater flow.
# - Hydrological Models: Knowledge of hydrological modeling techniques including statistical methods, deterministic models, and numerical simulations.
# - Watershed Dynamics: Understanding of watershed characteristics, behavior, and dynamics.
# - Hydraulic Structures: Knowledge of design and function of hydraulic structures such as dams, weirs, culverts, channels, and stormwater management systems.
# - Hydrological Data Collection: Familiarity with methods for collecting and analyzing hydrological data, including gauge stations, streamflow measurements, and rainfall data.
# - GIS and Remote Sensing: Proficiency in Geographic Information Systems (GIS) and remote sensing techniques for spatial analysis and mapping of hydrological features.
# - Regulatory Requirements: Understanding of relevant regulations and guidelines governing water resources management and environmental protection.
# - Climate Change Impacts: Awareness of how climate change can affect hydrological processes and water resource management strategies.
# - Software Proficiency: Familiarity with hydrological modeling software such as HEC-HMS</font>, HEC-RAS, SWMM, and MODFLOW.
# - Erosion and Sediment Transport: Knowledge of erosion processes and sediment transport mechanisms in rivers and streams.
# 
# <!-- When further questioned (by modifying the input prompt somewhat, and adjusting the "temperature" parameter in the prediction engine) six broad categories of essential skills a Civil Engineer needs to practice engineering hydrology are identified as:
# 
# **1. Hydrological Analysis and Modeling**
# 
# - Knowledge:Hydrological analysis and modeling are at the core of engineering hydrology. This involves understanding and simulating the water cycle, including rainfall, snowmelt, river flows, and groundwater movement. Hydrologists use complex mathematical models to predict how water moves through the environment. These models help in designing effective flood control systems, predicting droughts, and managing water supplies. By accurately simulating hydrological processes, engineers can plan for various scenarios and develop solutions that mitigate the impacts of extreme weather events.
# - Skills : Proficiency in using hydrological models (e.g. HEC-HMS,SWMM) to simulate water flow,precipitation, and runoff.
# - Ability : The ability to interpret model outouts regarding the movement, distribution, and quality of water within the Earth's atmosphere and surface to make informed decisions regarding water availability, managing water resources, and designing hydraulic structures.
# 
# **2. Data Collection and Analysis**
# - Knowledge: In engineering hydrology, data is paramount. Hydrologists collect data from a variety of sources, such as weather stations that measure rainfall, stream gauges that monitor river levels, and remote sensing satellites that provide imagery of large areas. Once collected, this data needs to be meticulously analyzed to identify trends, understand patterns, and validate models. High-quality data analysis ensures that predictions and designs are based on reliable information, which is critical for making informed decisions about water management and infrastructure development.
# - Skills: Proficiency in gathering and analyzing data from various sources, such as weather stations, stream gauges, and remote sensing technologies.
# - Ability: The ability to manage and analyze large datasets including precipitation, streamflow, and soil moisture data in order to generate reliable inputs for understanding hydrological processes, validating models, and making informed decisions.
# 
# **3. Understanding of Hydrological Processes**
# - Knowledge: A deep understanding of hydrological processes is essential for any hydrologist. This includes knowledge of how water interacts with the environment through processes like precipitation, evapotranspiration (the combination of evaporation and plant transpiration), infiltration into the soil, surface runoff, and groundwater flow. By understanding these processes, hydrologists can predict how changes in climate, land use, and vegetation will affect water availability and quality. This knowledge is crucial for developing strategies to manage water resources sustainably and protect against water-related hazards. Knowledge of fluid mechanics and hydraulic principles to design and evaluate water conveyance systems such as channels, culverts, and stormwater management systems. Knowledge of environmental regulations and guidelines related to water resources.
# - Skills:  Proficiency with tools such as HEC-RAS and SWMM for river and streamflow analysis.  Deep knowledge of processes like precipitation, evapotranspiration, infiltration, runoff, and groundwater flow.
# - Ability: Apply the knowledge to make informed predictions and and decisions under different environmental conditions. Conduct impact assesssments to evaluate the effects of projects on hydrological bejavior and aquatic ecosystems.
# 
# **4. Geographical Information Systems (GIS) and Remote Sensing**
# - Knowledge: GIS and remote sensing technologies are powerful tools in the field of hydrology. GIS allows hydrologists to create detailed maps and spatial analyses that show how water moves across different landscapes. Remote sensing, on the other hand, provides data from satellites and aircraft that can monitor large and inaccessible areas. Together, these tools enable the study of watershed characteristics, land use impacts, and temporal changes in water bodies. They are essential for tasks such as flood mapping, drought assessment, and habitat conservation.
# - Skills: Using GIS and remote sensing tools to analyze spatial and temporal patterns in hydrology; delineate watersheds; construct digital elevation models (DEM) of watersheds; determine land cover type to inform hydrologic models.
# - <font color = 'red'>Ability: Apply the technology for mapping watersheds, analyzing land use impacts, and monitoring changes in water bodies.</font>
# 
# **5. Computer Programming and Software Proficiency**
# - Knowledge: Modern hydrology relies heavily on computer programming and specialized software. Hydrologists use programming languages like Python, MATLAB, and R to develop custom models, automate data analysis, and perform complex simulations. Proficiency with hydrological software such as HEC-HMS (Hydrologic Modeling System), SWAT (Soil and Water Assessment Tool), MODFLOW (a groundwater flow model), and SWMM (Storm Water Management Model) and the EU and Asian equivalents is also essential. These tools allow for detailed analysis of hydrological systems and enable the integration of various data sources into cohesive models, enhancing the accuracy and efficiency of hydrological studies.
# - Skills: Programming skills and software proficiency to facilitate efficient data analysis, model customization, and automation of repetitive tasks.
# - Ability: Ability to use programming languages (like Python or MATLAB) and hydrological software (such as HEC-HMS, SWAT, or MODFLOW).  Use of tools to refactor data files to meet project and model needs, and prepare presentation exhibits for reports.
# 
# 
# **6. Project Management and Communication**
# - Knowledge: Hydrological projects require strong project management skills. This includes planning, organizing, and overseeing projects to ensure they are completed on time and within budget. Hydrologists must coordinate with other engineers, scientists, policymakers, and the community to achieve project goals. Effective communication is crucial, as hydrologists must present complex technical information in a clear and understandable manner to stakeholders. This ensures that the implications of their findings are understood and can inform decision-making processes, ultimately leading to better water management practices.
# - Skills: Competence in managing projects, including planning, budgeting, and coordinating with stakeholders, as well as effectively communicating findings.  Completion of assigned tasks in a timely fashion. 
# - Ability: Apply project management principles so that hydrological studies and projects are completed on time and within budget.  Employ clear communication methods (presentations, reports, graphical exhibits) so that results are understood and used appropriately by decision-makers and the public.
# 
# These 6 essential topics equip hydrologists to tackle the complex challenges of managing water resources in a sustainable and efficient manner.
# 
# This course has a substantial emphasis on selected topics in categories 1-4; categories 5 and 6 are largely experience based; category 5 is also a moving target.   -->

# ---
# ## Surface and Groundwater Hydrology Concepts
# 
# ### What is hydrology?
# - Study of the occurrence, circulation, storage, and distribution of surface and groundwater on the Earth.
# - Engineering hydrology is the quantification of amounts of water at various locations (spatially) as a function of time (temporally) for surface water applications.
# 
# ### What is a watershed (catchment)?
# Here are a couple of definitions of watersheds.
# 
# - Topographic area that collects and discharges surface streamflow through one outlet or mouth (pour point)
# - The area on the surface of the Earth that drains to a specific location
# - In groundwater a similar concept is called a groundwater basin – only the boundaries can move depending on relative rates of recharge and discharge 
# 
# The topographic definition omits that there could be subsurface sewer systems that can cross topographic boundaries.   It’s a big deal in urban areas.
# 
# ### What is a hydrologic system?
# A hydrologic system is just a collection of parts that interact.   
#  
# - A hydrologic system is simply the collection of connected components that form the <strong>hydrologic cycle</strong>
# - These components can be grouped into subsystems, treated separately, and the results combined according to interactions between the subsystems (CMM pg 5) 
# 
# Like in fluid mechanics, the system has boundaries (the control volume) and fluxes into/out of the boundaries.   
# The entire planet is usually considered a closed system (hydrologically) and only the energy fluxes cross the boundary.   
# At more practical scales (parking lot) the mass fluxes matter a lot.  
# 
# ### What is the hydrologic cycle?
# Here is a typical diagram depicting the hydrologic cycle.  
# 
# ![](hydrologic_cycle.png)
# 
# The driving force for the cycle (not shown) is solar energy that provides the energy to vaporize liquid water that then rises into clouds, moves onshore, and rains (or snow, sleet, $\dots$.  and other forms of <strong>precipitation</strong>)
# A portion of the rain becomes runoff, another portion returns to the atmosphere as evaporation, another portion infiltrates into the ground and becomes groundwater.
# 
# The surface water system would be the part of the diagram that lies above the plane defined by the ocean and infiltration line.
# The subsurface system is the part that is below this plane.
# 
# Expressed as a simple system diagram it would be depicted in the figure below
# 
# ![](system_diagram.png)

# ---
# ## Hydrologic Balance 
# 
# ### Water Budget
# The water budget, or <strong>hydrologic balance</strong> is simply the expression of the conservation of mass in hydrologic terms for a hydrologic system.  
# Generally it is expressed as a rate (or volume) balance.
# The hydrologic equation is the fundamental tool in hydrology to describe amounts of water in storage in different compartments at different scales.  
# 
# The equation expressed in “words” is
# 
# Rate of inflow - Rate of outflow =  Rate of change of storage + Rate of internal mass generation.
# 
# Symbolically it is exrepssed as:
# 
# $$ \frac{dI}{dt} - \frac{dO}{dt} = \frac{dS}{dt} + \frac{dG}{dt}$$
# 
# where
# 
# $I$ is inflow volume, $O$ is outflow volume, $S$ is storage volume (i.e. within a watershed), and $G$ is generated volume.
# $G$ is generally zero, but is included to be consistent with the balance equations you have learned elsewhere (i.e. environmental engineering, chemistry, $\dots$)

# ### Surface Hydrologic System
# 
# Here is the surface water system broken into its own sub-system.
# 
# ![](surface_system_diagram.png)
# 
# Notice the dashed line is the boundary – exactly like a control volume in fluids.
# 
# ### Surface Water Budget
# 
# From the surface water system diagram, appropriate budget components are:
# 
# - Inflows:  Rainfall; Surface water from outside boundary, recharge from Groundwater.
# - Outflows: Evapotranspiration; Surface water leaving boundary; Infiltration to groundwater.
# - Storage:  Water levels in lakes, rivers, ponds within the boundary; water stored on leaves and other surfaces.

# ### Sub-surface Hydrologic System
# 
# Here is the sub-surface water system broken into its own sub-system.
# 
# ![](subsurface_system_diagram.png)
# 
# Notice the dashed line is the boundary – exactly like a control volume in fluids.
# 
# ### Sub-surface Water Budget
# 
# From the sub-surface water system diagram, appropriate budget components are:
# 
# - Inflows:  Groundwater flow from outside boundary; Recharge from surface system (via infiltration)
# - Outflows: Groundwater flow out of the boundary; Discharge (pumping; springs) to surface system
# - Storage:  Water levels in aquifers within the boundary

# ### Combined Hydrologic System
# Here are the two systems “combined.”
# Communication is by the two shaded paths on the figure. 
# 
# ![](combined_system_diagram.png)
# 
# Loss from the surface system becomes gain to the ground system.
# Loss from the ground system becomes gain to the surface system.

# In[ ]:




