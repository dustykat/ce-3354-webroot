#!/usr/bin/env python
# coding: utf-8

# # 18. Stream Routing
# 
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
# 1. [Cleveland, T. G. (2017) *Surface Water Hydrology Notes (Channel Routing) to accompany CE-3354*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/1-Lectures-2017/Lecture18.pdf)
# 
# 1. [Routing (Hydrology) Wikipedia ](https://en.wikipedia.org/wiki/Routing_(hydrology))
# 
# 1. [Routing (Information) Wikipedia](https://en.wikipedia.org/wiki/Routing_Information_Protocol)

# ## Videos
# 
# 1. [Hydrograph Routing (YouTube)](https://www.youtube.com/watch?v=nzRG2uIMaTY)
# 2. [Reservoir Routing (YouTube)](https://www.youtube.com/watch?v=1mdtq7iJ_74&t=248s)
# 3. [Hydrologic Channel Routing (YouTube)](https://www.youtube.com/watch?v=HLSTZuEi5gg)
# 4. [Channel Routing (NCEES Training Video)](https://www.youtube.com/watch?v=Eb0BoxlxcQw&list=PLGCZ9gpx8QdsoFj-3qWS_7iq61WE4Yy9d)
# 5. [Reservoir Routing (NCEES Training Video)](https://www.youtube.com/watch?v=lkUEFtjQH6s&list=PLGCZ9gpx8QdsoFj-3qWS_7iq61WE4Yy9d)
# 6. [Flash Flood Videos (YouTube)](https://www.youtube.com/watch?v=u0-FLuwWhf4)
# 7. [Flash Flood near Sedona Az. (YouTube)](https://www.youtube.com/watch?v=Ipo0kwQQcgQ)

# ## Outline
# 
# 1. What is Level Pool Routing applied to a stream reach?
#   - Example of Level Pool Routing in a stream
# 3.  Muskingum Routing Background [Chow, V.T., Maidment,D.M., and Mays, L.W. (1998) Applied Hydrology, McGraw Hill, pp. 257-260](http://54.243.252.9/ce-3354-webroot/3-Readings/CMM1988/) 
# 4.  Muskingum-Cunge Routing applied to a stream reach [Chow, V.T., Maidment,D.M., and Mays, L.W. (1998) Applied Hydrology, McGraw Hill, pp. 302-304](http://54.243.252.9/ce-3354-webroot/3-Readings/CMM1988/) 

# ## What is Level Pool Routing applied to a stream reach?
# 
# Level Pool Routing applied to a stream reach is a hydrologic technique used to estimate how a flood wave or flow pulse travels through a reach of a stream, treating the reach as if it behaves like a reservoir or a level pool. In this method, the storage in the stream reach is assumed to be a function of the water surface elevation, which is relatively constant across the reach at any given time, akin to the behavior of a reservoir.
# 
# The technique is based on the principle of mass conservation, described by the continuity equation:
# 
# $\Delta S = I - O$
# 
# Where:
# 
# $\Delta S$ is the change in storage, <br>
# $I$ is the inflow, and<br>
# $O$ is the outflow.<br>
# 
# In Level Pool Routing, the **storage-outflow** relationship is crucial, as it relates the storage in the reach to the outflow, often using a known empirical or analytical function derived from observations or topographic data. The method solves for the change in storage and computes the outflow from the reach at each time step, typically using iterative methods or graphical solutions.
# 
# Key Assumptions in Level Pool Routing for a Stream Reach:
# 
# - Uniform Water Surface Elevation: The water surface elevation across the stream reach is assumed to remain level, meaning that storage is dependent only on the depth of water in the reach, not the slope.
# - Quasi-Steady Flow Conditions: This method assumes **steady flow** within **each time** increment (...a sequence of steady states), focusing on the cumulative inflow and outflow over time.
# - Simplified Geometry: The stream reach is treated as having simplified geometry, often approximating a reservoir-like behavior, even though the reach may have some slope and varying channel shapes.
# 
# Application in Hydrologic Modeling:
# 
# - Flood Routing: Level pool routing is commonly used for flood routing when water storage effects dominate (such as wide floodplains or slow-moving rivers).
# - Dam Breach Modeling: It is also frequently applied in scenarios where the stream behaves similarly to a reservoir, such as when simulating the routing of a dam breach flood wave through a downstream reach.
# 
# Though Level Pool Routing is an approximation, it provides a simple and effective way to model stream reaches where the water movement is slow, and storage is a key factor in determining flow characteristics downstream.
# 
# The method is also known by the names Puls Routing, Modified Puls Routing, and/or Storage-Indication Method. It is typically used for rivers or streams with significant storage effects (e.g., where floodplains or reservoirs influence flow). This method is common in hydrologic models that simulate unsteady flow, such as during flood events, providing estimates of stream discharge at various points downstream.

# ## Stream Routing
# 
# Using the same development as reservoir routing, time averaged values are taken at the beginning and end of a useful time interval, and the first-order difference quotient is used to approximate the rate of change in storage.
# 
# The reach mass balance is then
# 
# $$\frac{I_t - I_{t-\Delta t}}{2} - \frac{O_t - O_{t-\Delta t}}{2} = \frac{S_t - S_{t-\Delta t}}{\Delta t}  $$
# 
# A stream may be comprised of many reaches, each treated as a reservoir-type element.
# 
# **Stream-reach hydraulics**, and **depth-area-storage** are used to build a storage-outflow function
# 
# 
# $$O = f(S)$$
# 
# Once we have that function, then build an auxiliary function (tabulation) called the storage-indication curve (function)
# 
# $$ O = g(\frac{2S}{\Delta t} +O) $$
# 
# where $g$ is some function.
# 
# Once have the storage-indication curve then can use the reach mass balance to estimate the numerical value of :
# 
# $$\frac{2S_t}{\Delta t} +O_t$$
# 
# Then use the storage-indication curve to find the value of outflow, subtract that from the result above, and now have both the end-of-interval outflow and storage.

# ### Prism and Wedge Storage
# 
# A channel reach diagram is shown below,  In Level Pool Routing the wedge storage is zero, X=0
# 
# ![](streamdiagram1.png)
# 
# :::{note}
# The Muskingum-Cunge Routing method relaxes the constraint on X and provides ways to estimate its value so that wedge storage can be modeled.
# :::
# 
# The storage in a reach can be estimated as the product of the average cross sectional area for a given discharge rate and the reach length. (This preserves the level pool assumption)
# 
# ![](storagediagram1.png)

# ### Approximating Ratings
# 
# A rating equation is prescribed at each cross section to determine the cross section areas for particular flow rates.
# 
# A simple approximation to construct ratings from cross section geometry is to assume normal flow in the channel, while not strictly correct it is a useful approximation
# 
# $Q = \frac{1.49}{n} \times A R^{2/3} S_0^{1/2}$
# 
# Use cross section geometry to find values for $A$, and $R$.
# 
# :::{note}
# The Manning's equation above is for US Customary system, for SI system the 1.49 is **replaced** with 1.0.
# :::
# 
# - Engineered cross sections almost exclusively use just a handful of convenient geometry (rectangular, trapezoidal, triangular, and circular).
# - Natural cross sections are handled in similar fashion as engineered, except numerical integration is used for the depth-area, topwidth-area, and perimeter-area computations.  In many instances a parabolic cross section is a decent natural channel approximation.

# ### Cross Section Geometries
# 
# Some common cross sections that can be used are the mighty **wrecked angle**.
# 
# ![](rectangle.png)
# 
# Another common shape is a **Trapezoidal** channel.
# 
# ![](trapezoid.png)
# 
# Various **Triangles** are special cases of a generic trapezoid.  These are tyopically called triangular swales and are easily created by a road grader or a buldozer.  Its also possible to construct with a box grader, but takes a somewhat skilled operater to do so.  (The road grader and buldozer takes skill too - the point is these are reasonably common constructed shapes)
# 
# ![](triangle.png)
# 
# The other common engineered shape is the **circle**, normally laid into a trench, then backfilled.
# 
# ![](circle.png)

# **Irregular** cross-sections are a bit more involved, but the general idea is the same as above shapes:
# 
# ![](irregular.png)
# 
# The designer will need to construct a **depth-area** table (or use software to do so) for each cross section
# 
# ![](area.png)
# 
# The designer will need to construct a **depth-topwidth** table (or use software to do so) for each cross section
# 
# ![](topwidth.png)
# 
# The designer will need to construct a **depth-perimeter** table (or use software to do so) for each cross section
# 
# ![](perimeter.png)
# 
# The flow direction also matters, especially in tidally influenced domains.  The global direction convention is "looking downstream."  In coastal areas downstream is from land to ocean.
# 
# ![](flowdirection.png)

# ## Computational Workflow
# 
# A known inflow hydrograph and initial storage condition is propagated forward in time to estimate the outflow hydrograph.
# - The choice of $\Delta t$ value should be made so that it is smaller than the travel time in the reach at the largest likely flow and smaller than about 1/5 the time to peak of the inflow hydrograph
# - HMS is supposed to manage this issue internally, if we roll-our-own, need to be cognizant of this important requirement for numerical stability.

# ## Illustrative Example
# 
# Consider a channel that is 2500 feet long, with slope of 0.09%, clean sides with straight banks and no rifts or deep pools. Manning’s $n$ is 0.030.
# 
# ![](channel.png)
# 
# The inflow hydrograph is triangular with a time base of 3 hours, and time-to-peak of 1 hour. The peak inflow rate is 360 cfs.
# 
# ![](hydrograph.png)
# 
# The computational "configuration" is input hydrograph => channel routing => output hydrograph.
# 
# ![](configuration.png)
# 
# Analyst Tasks:
# - Build a depth-storage table 
# - Build a depth-outflow table
#   - From 0-6 feet deep use Manning’s equation in variable-geometry conduit
# - Build the input hydrograph (make the picture into numb3rs). 
# - Build the routing table (apply the reach mass balance)
# 
# ### Depth-Storage Table
# 
# ![](depth-area-table.png)
# 
# ### Input Hydrograph Table
# 
# ![](hydrograph-table.png)
# 
# ### Storage-Discharge Table 
# 
# ![](storage-discharge-table.png)
# 
# ### Routing Table (Reach Mass Balance)
# 
# ![](routing-sheet.png)
# 
# Usuall useful to plot and interpret results
# 
# ### Results and Interpretation
# 
# ![](routed-result.png)

# ## Spreadsheet
# The spreadsheet used to construct the example above is [Stream_Storage_Routing.xls (Uses MACROS, must open using Excel for example to work)](http://54.243.252.9/ce-3354-webroot/ce-3354-webbook-2024/my3354notes/lessons/18-CatchmentRouting/Stream_Storage_Routing.xls)

# ## HEC-HMS Approach
# 
# Here is the same example using HEC-HMS to manage the data and computations.
# 
# **Create a Project**
# 
# Basin model has a:
# - source (entered as a time series)
# - reach element
# 
# ![](hms_generic.png)
# 
# ---
# 
# **Supply Storage-Discharge Table**
# 
# Entered as Paired-Data element
# 
# ![](hms_storage-discharge.png)
# 
# ---
# 
# **Supply a Meterological Model**
# 
# Required for simulation, but a null element
# 
# ![](hms_metmodel.png)
# 
# ---
# 
# **Supply Control Specifications**
# 
# ![](hms_controlspecs.png)
# 
# ---
# 
# **Interpret Results**
# 
# ![](hms-results.png)
# 
# ---
# ### Project File 
# 
# 1. [Puls Routing in a Stream.zip (zip file of entire HEC-HMS project)](http://54.243.252.9/ce-3354-webroot/ce3354book/lessons/lesson12/PulsRoutingInAStream.zip)

# ## Muskingum Routing
# 
# A method that includes consideration of wedge storage is Muskingum routing (Named after the [Muskingum River](https://en.wikipedia.org/wiki/Muskingum_River) in Ohio.
# 
# Muskingum routing is a storage-routing technique that is used to:
# - translate and attenuate hydrographs in natural and engineered channels
# - avoids the added complexity of hydraulic routing.
# 
# The method is appropriate for a stream reach that has approximately constant geometric properties.
# 
# ### Theory
# 
# At the upstream end, the inflow and storage are assumed to be related to depth by power-law models
# 
# $I= a y_u^n$ <br>
# $S_I = b y_u^m$ <br>
# 
# At the downstream end, the outflow and storage are also assumed to be related to depth by power-law models
# 
# $O= a y_d^n$ <br>
# $S_O = b y_d^m$ <br>
# 
# The depths at each end are rewritten in terms of the power law constants and the inflows
# 
# $S_I=\frac{bI^{m/n}}{a^{m/n}}$ <br>
# $S_O=\frac{bO^{m/n}}{a^{m/n}}$ <br>
# 
# Then one conjectures that the storage within the reach is some weighted combination of the section storage at each end (weighted average)
# 
# $S = wS_I + (1-w)S_O$<br>
# 
# The weight, $w$, ranges between 0 and 0.5.
# - When w = 0, the storage in the reach is entirely explained at the outlet end (like a level pool)
# - When w = 0.5, the storage is an arithmetic mean of the section storage at each end.
# 
# Generally the variables from the power law models are substituted
# 
# $K=\frac{b}{a^{m/n}}$, and <br>
# $z = m/n$<br>
# 
# And the routing model is expressed as
# 
# $S=K[wI^z + (1-w)O^z$
# 
# if $z$ is assumed to be unity the expression results in the form
# 
# $S=K[wI + (1-w)O]$
# 
# For most natural channels $w$ ranges between 0.1 and 0.3 and are usually determined by calibration studies
# 
# Muskingum-Cunge further refines the model to  relate the values of the weights to channel geometry, slope, and resistance features.  At this level of abstraction (Muskingum-Cunge) the model is nearly a hydraulic model.
# 
# :::{note}
# Muskingum-Cunge routing and the kinematic wave method are nearly identical because both techniques focus on approximating how flood waves propagate through a stream or channel, with a primary emphasis on downstream flow movement rather than complex backwater effects.
# 
# - Flow Assumption: Both methods are based on the assumption that the dominant flow process is advective transport, meaning the flow is driven primarily by the slope of the channel and the velocity of the water, with minimal consideration for upstream effects or changes in flow depth (e.g., backwater effects). This is why both methods work well for gradually varied flows in channels with relatively mild slopes.
# 
# - Linearization of Equations: Both Muskingum-Cunge and kinematic wave methods simplify the Saint-Venant equations (full dynamic wave equations). The kinematic wave neglects the inertia and pressure terms, reducing the complexity of the momentum equation to focus on gravity-driven flow. Similarly, Muskingum-Cunge introduces a finite difference approach to linearize and stabilize the continuity and momentum equations, which approximates flow movement without the need for solving the full dynamic equations.
# 
# - Numerical Similarities: The Muskingum-Cunge method uses a numerical scheme that results in flow propagation behavior closely resembling the kinematic wave model when applied to simple flow scenarios (such as uniform or steady-state conditions). The key difference is that Muskingum-Cunge includes a diffusive term, providing a slight smoothing of the flow, but under many conditions, this effect is minimal, making the two methods yield almost identical results.
# 
# Thus, both methods are used for streamflow routing in gradually varied flows where downstream propagation of flood waves dominates, and flow variations over time are smooth and predictable. The slight difference lies in Muskingum-Cunge's ability to account for limited diffusion, but this is often negligible in practical applications, making the two approaches nearly interchangeable.
# :::

# ## HEC-HMS Approach
# 
# Here is the same example using HEC-HMS and Muskingum-Cunge method of routing.
# 
# From hydrologic literature (Haan, Barfield,
# Hayes) a rule of thumb for estimating w and K is
# - Estimate celerity, $c$, from bankful discharge (or deepest discharge value)
# - Estimate K as ratio of reach length to celerity (units of time, essentially a reach travel time)
# - Estimate weight (w) as $w=\frac{1}{2}(1-\frac{q_0}{S_)cL})$
# 
# [MuskingumEstimator.xls](http://54.243.252.9/ce-3354-webroot/ce-3354-webbook-2024/my3354notes/lessons/18-CatchmentRouting/MuskingumEstimator.xls)
# 
# **Estimate Celerity**
# 
# ![](celerity.png)
# 
# **Apply estimates in Muskingum Method**
# 
# ![](hms_muskingum.png)
# 
# **Explore Different Settings**
# 
# ![](hms_mkgum01.png)
# 
# ![](hms_mkgum02.png)

# ## Muskingum-Cunge
# 
# Described in [Chow, V.T., Maidment,D.M., and Mays, L.W. (1998) Applied Hydrology, McGraw Hill, pp. 302-304](http://54.243.252.9/ce-3354-webroot/3-Readings/CMM1988/).  
# 
# Data needs are:
# - Cross section geometry (as paired-data)
# - Manning’s n in channel, left and right overbank
# - Slope
# - Reach length
# - Number of reaches (the program divides the reaches into sub-reaches for computation)
# 
# ![](glass-walls.png)
# 
# ![](hms_mcsetup.png)
# 
# ![](hms_mcresults.png)

# ##  Summary
# Examined routing using: 
# - Lag
# - Level pool routing (Puls) 
# - Muskingum
# - Muskingum-Cunge
# 
# **All require external data preparation**
# 
# :::{note}
# You should apply Muskingum-Cunge methods for the Hardin Branch study (the others will work fine, but you have the needed topography to approximate channel cross sections to apply Muskingum-Cunge)
# :::
# 
# ## End of File

# In[ ]:




