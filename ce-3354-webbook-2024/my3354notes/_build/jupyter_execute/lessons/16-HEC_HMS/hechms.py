#!/usr/bin/env python
# coding: utf-8

# # 16. HEC-HMS 

# :::{admonition} Course Website
# [Link to course website](http://54.243.252.9/)
# :::
# 
# 

# ## Readings
# 
# 1. [Chow, V.T., Maidment,D.M., and Mays, L.W. (1998) Applied Hydrology, McGraw Hill, (Read pages 26 to 31; 416 to 423)](http://54.243.252.9/ce-3354-webroot/3-Readings/CMM1988/) 
# 2. [Cleveland, T. G. (2017) *Engineering Hydrology Notes (Introduction to HEC-HMS) to accompany CE-3354*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/1-Lectures-2017/Lecture09.pdf)
# 3. [Cleveland, T. G. (2022) *Engineering Hydrology Notes to Accompany CE 3354 (Introduction to HEC-HMS; Ash Creek Dallas HEC-HMS Example)*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/ce-3354-webbook-2024/my3354notes/lessons/16-HEC_HMS/Lesson09ug.pdf)
# 2. [HEC-HMS User Manual 3.5](http://54.243.252.9/ce-3354-webroot/3-Readings/HEC-HMS-Documentation/HEC-HMS_Users_Manual_3.5.pdf)
# 3. [HEC-HMS Applications Guide](http://54.243.252.9/ce-3354-webroot/3-Readings/HEC-HMS-Documentation/HEC-HMS_Applications_Guide_March2008.pdf)
# 4. [HEC_HMS Quick Start Guide 3.5](http://54.243.252.9/ce-3354-webroot/3-Readings/HEC-HMS-Documentation/HEC-HMS_QuickStart_Guide_3.5.pdf)
# 5. [HEC-HMS Release Notes 3.5](http://54.243.252.9/ce-3354-webroot/3-Readings/HEC-HMS-Documentation/HEC-HMS_Release_Notes_3.5.pdf)
# 6. [HEC-HMS Technical Reference Manual](http://54.243.252.9/ce-3354-webroot/3-Readings/HEC-HMS-Documentation/HEC-HMS_TechnicalReferenceManual_(CPD-74B).pdf)
# 7. [NRCS TP-149 CN estimation](http://54.243.252.9/ce-3354-webroot/3-Readings/NRCS-CN-TP149/methodforestimat149kent.pdf)
# 9. [AshCreek Data (zip)](http://54.243.252.9/ce-3354-webroot/ce3354book/lessons/lesson06.1/AshCreekData.zip)

# ## Videos
# 
# There are a lot of videos on YouTube suitable for self-training to use HEC-HMS (non-gridded).  The gridded HMS is a more advanced exercise (you have to have GIS skills first) and is the obvious extension of lumped (non-gridded) models -- but outside the course scope.
# 
# 1. [How to install HEC-HMS (YouTube)](https://www.youtube.com/watch?v=hCbTpNzInpQ)
# 2. [HEC-HMS Overview (YouTube)](https://www.youtube.com/watch?v=0JvoJPDPKSk)
# 3. [HEC-HMS Building a Basin Model (YouTube)](https://www.youtube.com/watch?v=E2nIwH2NbOc&list=PLH7yUh2l8q9WnSFbyKB4oIIGHMgfMaWCv&index=2)
# 4. [HEC-HMS Building a Meterological Model (YouTube)](https://www.youtube.com/watch?v=dzOZQpj7PSg&list=PLH7yUh2l8q9WnSFbyKB4oIIGHMgfMaWCv&index=3)
# 5. [HEC-HMS Running a Simulation (YouTube)](https://www.youtube.com/watch?v=U-TIoKYFCrw&list=PLH7yUh2l8q9WnSFbyKB4oIIGHMgfMaWCv&index=4)
# 6. [HEC-HMS Results Interpretation (YouTube)](https://www.youtube.com/watch?v=WwmzAqer6GU&list=PLH7yUh2l8q9WnSFbyKB4oIIGHMgfMaWCv&index=5)
# 7. [HEC-HMS Simulation Types (YouTube)](https://www.youtube.com/watch?v=rwXwY7heaLQ&list=PLH7yUh2l8q9WnSFbyKB4oIIGHMgfMaWCv&index=6)
# 

# ## Outline
# 
# 1. About HEC-HMS
# 2. Installation
# 

# ## About HEC-HMS
# 
# [HEC-Hydrologic Modeling System (HMS)](https://www.hec.usace.army.mil/software/hec-hms/)  the U.S. Army Corps of Engineers’ software package for modeling the complete hydrologic processes of dendritic watershed systems. The software includes many traditional hydrologic analysis procedures such as event infiltration, unit hydrographs, and hydrologic routing. HEC-HMS also includes procedures necessary for continuous simulation including evapo-transpiration, snowmelt, and soil moisture accounting. Advanced capabilities are also provided for gridded runoff simulation using the linear quasi-distributed runoff transform (ModClark). Supplemental analysis tools are provided for model optimization, forecasting streamflow, depth-area reduction, assessing model uncertainty, erosion and sediment transport, and water quality. The software and documentation are available free of charge.
# 
# :::{note}
# Some of the stated capabilities above are marketing BS, but the software is a widely used tool.  A practicing Civil and Enviornmental Engineer would be expected to be proficient in HEC-HMS and/or SWMM
# 
# Proficiency in HEC-HMS involves:
# 
# - Understanding of Hydrologic Processes:
# <br>A solid grasp of hydrologic principles and processes, such as rainfall-runoff relationships, loss models, baseflow separation, and channel routing.
# 
# - Model Development:
# <br>Ability to create and configure hydrologic models, including defining watershed boundaries, inputting hydrologic data (precipitation, temperature, etc.), and setting up sub-basins, reaches, junctions, and reservoirs.
# 
# - Selection and Application of Methods:
# <br>Knowledge of various computational methods available in HEC-HMS for different hydrologic processes, such as loss models (e.g., SCS Curve Number, Green-Ampt), transform methods (e.g., SCS Unit Hydrograph, Clark Unit Hydrograph), and routing methods (e.g., Muskingum, Kinematic Wave).
# 
# - Data Management:
# <br>Competence in importing and managing input data, such as time series data for precipitation, temperature, streamflow, and observed data for model calibration.
# 
# - Model Calibration and Validation:
# <br>Skill in calibrating the model parameters to match observed data, and validating the model's performance with different data sets to ensure its reliability.
# 
# - Simulation and Analysis:
# <br>Capability to run simulations, interpret results, and analyze hydrographs, peak flows, and flow volumes for different scenarios (e.g., different rainfall events or land-use changes).
# 
# - Advanced Features:
# <br>Familiarity with advanced features, such as simulating stormwater management practices, running continuous simulations, or using the software for flood forecasting.
# 
# - Troubleshooting and Problem-Solving:
# <br>Ability to identify and resolve issues related to model setup, data inconsistencies, and convergence problems.
# 
# - Documentation and Reporting:
# <br>Proficiency in documenting the modeling process, assumptions, and results, as well as preparing professional reports and presentations.
# 
# Being proficient in HEC-HMS means not only knowing how to use the software's interface but also understanding the underlying hydrologic concepts and methodologies, enabling effective and accurate hydrologic modeling and analysis.
# :::
# 
# ### History of HMS
# HMS Evolved from HEC-1 as part of a “new-generation” software emphasis circa 1990.  The main end-user result is an Integrated user interface to speed up data input and enhance output interpretation.  
# 
# ### Overview
# HMS is a complex and sophisticated tool:
# - Intended to be used by a knowledgeable and skilled operator
# - Knowledge and skill increase with use
# - The skills are perishable
# 
# ### Data management
# - Graphical User Interface (GUI)
# - Multiple input files
# - Multiple output files
# - Time-series in HEC-DSS
# 
# All files arranged in a **Project** which is the fundamental data organization structure 
# - Paths to individual files
# - Can compress and e-mail entire project folders and have them run elsewhere (assuming the files are stored in the folder in their entirety)
# 
# ### Hydrologic Conceptualization
# 
# Organizes precipitation, watershed interaction, and runoff into major elements
# - Basin model and sub-basin description
#  - Downstream connections: how the system components are interconnected
#  - Loss model: how rainfall is converted into excess rainfall
#  - Transformation model: how the excess rainfall is redistributed in time and moved to the hydrologically nearest outlet (unit hydrographs, routing elements ...)
# - Meterological model
#  - Raingage specifications and assignment to different sub-basins
#  - Time-series models: Supply input hyetographs; Supply observed hydrographs
# - Simulation control
#  - Supply instructions of what, when, how to simulate
#  
# In the end HEC-HMS is a Hydrologic Model and can estimate:
# - Peak Flows
# - Hydrographs
# 
# It can perform
# - Hydrograph Routing
#  - Stream reaches
#  - Reservoirs and detention basins
#  - Hydrograph lagging and attenuation
# - Sub-basin modeling (if appropriate)
# 
# Precipitation to Runoff
# - Abstractions
#  - Fraction of precipitation that does not contribute to runoff (and ultimately discharge)
# - Routing
#  - Watershed routing (unit hydrograph and similar concepts)
#  - Stream (Channel) routing
#  - Reservoir (Storage) routing

# ## Installation
# 
# Navigate to the HEC-HMS website, select software appropriate for your computer.  
# 
# ![](download-window.png)
# 
# <!--Apple users will choose the Linux versions and have to figure out an interface, or get a [CodeWeaver](https://www.codeweavers.com/) application layer, or get [Parallels](https://www.parallels.com/pd/general/?gclid=CjwKCAjw79iaBhAJEiwAPYwoCFORJ8sEPl3m0sP2EEj6TExbC4rKqt6LUsS22AVAmTK8PkgnfLqbkxoC_dcQAvD_BwE), or build a [Cloud Application](https://aws.amazon.com/free/compute/lightsail/?trk=56417dfe-8849-4622-bfa4-7ec30bd6f5a3&sc_channel=ps&s_kwcid=AL!4422!3!536323500429!e!!g!!aws%20lightsail&ef_id=CjwKCAjw79iaBhAJEiwAPYwoCKquJK3Cnwmaf8sZZURFgvZO3FdYDyiQufkvEyD4DGuUCtGIGII50BoC77EQAvD_BwE:G:s&s_kwcid=AL!4422!3!536323500429!e!!g!!aws%20lightsail)-->
# 
# :::{note}
# My copy of HEC-HMS is stored as a cloud application hosted on AWS.  It houses a fully provisioned Windows Implementation of HEC-HMS (and some other tools) and is located at:
# 
# - server_name: **kittyinthewindow.ddns.net**
# - user_name: **texas-skew**
# - passwd: **peakfq73$hare**
# 
# Users must access using [Remote Desktop Protocol](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-mac) (Built into Windows, Apple Store has a free Mac application).
# :::
# 
# For a typical winders machine:
# 1. Download an installer
# 2. Run the installer <br>
#   - Accept the defaults (otherwise YOYO!)
# 
# Upon sucessful install you should be able to select the program and launch it and get the control interface
# 
# To install supplied examples, navigate to the help tab (in the HMS interface) and select download examples
# 
# :::{note}
# Usually the above works, unless you try something fancy and are [clueless](https://www.imdb.com/title/tt0112697/).  If you cannot figure it out go [here](https://harri.com/mysubwaycareer)
# :::

# ### HEC-HMS Minimal Model
# 
# A minimal model consists of 
# 
# - Basin Model
# - Meteorological Model
# - Control Specifications
# 
# #### Basin Model Specification
# 
# For this example we will use the Hardin Creek basin which is about 17 square miles.  For the example we will neglect the reservoirs and model the whole thing as a single watershed.
# 
# To create a basin model, select Components from the menu then Basin Manager 
# 
# ![](hms-basinmanager.png)
# 
# As with most HMS creator dialogs, you next name the basin.
# 
# ![](hms-basinname.png)
# 
# #### Meterological Model Specification
# 
# To create a meterological model, select Components from the menu then Meterological Model Manager 
# 
# ![](hms-metmodel.png)
# 
# As with most HMS creator dialogs, you next name the model.
# 
# ![](hms-metmodelname.png)
# 
# #### Control Model Specification
# 
# The last component is the control specification model (with dates and times for the simulation period).  To create a control model, select Components from the menu then Control Model Manager 
# 
# ![](hms-controlspecs.png)
# 
# Then next name the model.
# 
# ![](hms-controlspecsname.png)
# 
# #### Parameterizing the models
# 
# Now that the pieces are built, we need to supply watershed and rainfall characteristics to the components for a useable model.  First we will simulate the entire watershed as a single basin, with CN=98, and all other watershed-based model components disabled (i.e. None)
# 
# First build the single **basin**
# 
# ![](hms-subbasinselect.png)
# 
# Then supply the inputs, first area and the CN model.  Disable all the remaining methods (choose --None--)
# 
# ![](hms-nwebasins1.png)
# 
# Then the CN parameters (same as in class)
# 
# ![](hms-nwebasins2.png)
# 
# Then supply the **meterological** model inputs, for the example we will use an SCS design storm, in HMS its called "hypothetical" storm.
# 
# ![](hms-hypothetical1.png)
# 
# Then be sure the correct basins are attached to the precipitation input signal
# 
# ![](hms-hypothetical2.png)
# 
# Next select the storm itself and supply model inputs
# 
# ![](hms-hypothetical3.png)
# 
# Now select the **control** specifications and provide needed time values (must be calendar/clock time, HMS does not easily handle elapsed times - you can use fake dates as needed)
# 
# ![](hms-control1.png)
# 
# Now one can select simulation run builder
# 
# ![](hms-sim1.png)
# 
# ![](hms-sim2.png)
# 
# ![](hms-sim3.png)
# 
# ![](hms-sim4.png)
# 
# Once these are complete select Finish and the run manager is loaded, next select the particular run to active the compute engine
# 
# ![](hms-sim5.png)
# 
# At this point it should be ready, this is a good time to save the project, then reload the saved project from the file menu. Now attempt to run the simulation by selecting the exploding raindrop!
# 
# ![](hms-sim6.png)
# 
# With some luck it works like
# 
# ![](hms-sim7.png)
# 
# With a suseccful run we can examine various output features - to complete this notebook section we will just use a default chart of runoff from the watershed.  Select the Results/Element_Graph to get:
# 
# ![](hms-sim8.png)
# 
# There are tutorials and examples in the User Manual for the software.

# ### HEC-HMS Multiple Elements 
# 
# This example uses data from [AshCreek Data (zip)](http://54.243.252.9/ce-3354-webroot/ce3354book/lessons/lesson06.1/AshCreekData.zip).  The .ZIP file is an old homework problem, learners had to convert the provided data files into a format that HEC-HMS could process then analyze the watershed and interpret results and answer some questions.  
# 
# :::{admonition}Problem_Statement
# **HEC-HMS Exercises**
# 
# In this folder are rainfall-runofff data for three storms on Ash Creek watershed in Dallas, Texas.  
# Included are some base maps to help locate the watershed.  
# The maps are simply PDF files and are not georeferenced, so other than pretty pictures the maps are useless.
# 
# Using HEC HMS model the Ash Creek Watershed using a loss model of your choice and a transformation model of your choice.  Model the watershed as a lumped system (one sub-basin, no routing).
# 
# (1) Estimate parameter values in the model without using the time-series data (synthetic hydrology).  Document how you make the estimates.
# 
# (2) Test your estimated with the 1973_0603 storm, how well did your synthetic approach perform.
# 
# (3) Use the 1973_0603 storm to "calibrate" your model.  Trial-and-error is appropriate, or you chould choose the internal calibration tools in HMS, also your choice.  Demonstrate the calibrated model by capturing the model output for the storm (i.e. a time series of computed and observed discharge).   Use the weighted accumulated precipitation is the input (since we don't have the raingage locations).
# 
# (4) Test the calibrated model with the other two storms (DO NOT CHANGE PARAMETERS IN THE MODEL).   Assess model performance with thses other two real storms.  What do you conclude?
# 
# (5) Now try to adjust the parameters to obtain a best "average" performance.  What do you conclude?
# 
# (6-8) Repeat steps 3-5 with the watershed subdivided into multiple sub-basins, with routing.    Use any subdivision scheme you think is appropriate, but use at least 3 sub-basins.
# 
# Did subdivision confer any performance advantage?   At what cost?
# 
# (9)  Presumably you represented the current conditions with some variable that reflects the land coverage.  Estimate the watershed response to the historical storms if the entire watershed is impermeable, and very smooth (low friction).
# 
# Prepare a brief report on the modeling effort, be sure to address each question above.  Due in 2 weeks.  
# 
# You will need to download the HEC-HMS user manual and do some reading in the manual as well as in the hydrology literature and textbook to complete this exercise.
# :::
Linear Quasi-Distributed Runoff Transform (ModClark) Model

The Linear Quasi-Distributed Runoff Transform, commonly referred to as the ModClark model, is an advanced method for simulating the transformation of rainfall into runoff within a watershed. It is an extension of the Clark Unit Hydrograph method, integrating the concepts of spatial variability and distributed hydrologic response.
Key Features:

    Spatial Variability: Unlike traditional lumped models that treat the watershed as a single unit, the ModClark model incorporates spatial variability by dividing the watershed into multiple grid cells. Each grid cell has unique hydrologic properties, allowing for a more detailed and realistic representation of the watershed's response to rainfall.

    Grid-Based Approach: The watershed is discretized into a grid, where each cell's excess rainfall is computed and routed to the watershed outlet. The routing is done using a combination of translation (movement of water from one cell to another) and storage (delays in flow due to channel and overland flow characteristics).

    Rainfall Distribution: The ModClark model can account for non-uniform rainfall distribution across the watershed. This is particularly useful for large or complex watersheds where precipitation may vary significantly in space.

    Time-Area Concept: The model employs a time-area histogram, similar to the Clark Unit Hydrograph method, to represent the travel time distribution of water from different parts of the watershed to the outlet. The time-area curve is derived from the grid structure and flow path characteristics.

    Linear Reservoir Concept: The model uses a linear reservoir approach to simulate storage and attenuation effects. The linear reservoir coefficient and time of concentration are key parameters that influence the shape and timing of the runoff hydrograph.

Applications:

The ModClark model is particularly useful in situations where spatial variability in rainfall and watershed characteristics play a significant role in the runoff response. It is often used for:

    Flood forecasting and floodplain management.
    Urban hydrology, where impervious surfaces and drainage networks create complex runoff patterns.
    Watershed management and planning, where detailed understanding of hydrologic processes is required.

Advantages:

    Enhanced Accuracy: By accounting for spatial variability and detailed hydrologic response, the ModClark model provides a more accurate representation of runoff generation and routing compared to lumped models.
    Flexibility: The model can be adapted to various scales and complexities of watersheds, making it a versatile tool for hydrologists.

Limitations:

    Data Requirements: The model requires detailed spatial data for accurate representation, including grid-based rainfall, land cover, and topography.
    Computational Demand: The grid-based approach and detailed routing can be computationally intensive, especially for large watersheds or long simulation periods.

In summary, the ModClark model is a powerful tool for hydrologic modeling, offering a quasi-distributed approach that captures the spatial heterogeneity of watersheds and improves the accuracy of runoff predictions.
# In[ ]:




