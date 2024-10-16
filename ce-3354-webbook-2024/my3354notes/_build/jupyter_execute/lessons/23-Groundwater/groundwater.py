#!/usr/bin/env python
# coding: utf-8

# # 23. Groundwater Hydrology - I

# :::{admonition} Course Website
# [Link to Course Website](http://54.243.252.9/ce-3354-webroot/)
# :::
# 
# 

# ## Readings
# 
# 1. Gupta pp. 127-132
# 4. [Basic Groundwater Hydrology - USGS WSP 2020](http://54.243.252.9/ce-3354-webroot/3-Readings/USGS-WSP2020-GroundwaterHydrology/usgs-wsp-2020.pdf)
# 1. [Cleveland, T. G. (2017) *Engineering Hydrology Notes (Groundwater - I) to accompany CE-3354*, Department of Civil, Environmental, and Construction Engineering, Whitacre College of Engineering.](http://54.243.252.9/ce-3354-webroot/1-Lectures-2017/Lecture21.pdf)
# 2. [Groundwater - Excerpt from Viessman](http://54.243.252.9/ce-3354-webroot/3-Readings/Groundwater-Viessman/GroundwaterHydrology.pdf)
# 3. [Groundwater - Excerpt from Ferris](http://54.243.252.9/ce-3354-webroot/3-Readings/Groundwater-Wisler&Brater/Groundwater-Wisler.pdf)

# ## Videos
# 
# 1. [What is an Aquifer? (YouTube)](https://www.youtube.com/watch?v=gRY7TYBx-is)
# 2. [What is Groundwater? (YouTube)](https://www.youtube.com/watch?v=VtIY4FYWJV8)
# 3. [Aquifer Demonstration (YouTube)](https://www.youtube.com/watch?v=8Q7C3xrJrpw)
# 4. [How Groundwater and Wells Work (YouTube)](https://www.youtube.com/watch?v=bG19b06NG_w)
# 5. [Intoduction to Groundwater Flow (YouTube)](https://www.youtube.com/watch?v=O7K00PQaQIw)
# 6. [Hydrogeology (YouTube)](https://www.youtube.com/watch?v=G7CnE5NBxZs)
# 7. [Porosity and Permeability (YouTube)](https://www.youtube.com/watch?v=JjEmxgr0TR8)
# 8. [Porosity and Permeability Demo (YouTube)](https://www.youtube.com/watch?v=8mfBomrw0rs)
# 9. [Porosity, Permeability, and Capillarity (YouTube)](https://www.youtube.com/watch?v=NL2lQFCW4M4)
# 10. [Darcy's Law I (YouTube)](https://www.youtube.com/watch?v=--8SC0Q-cKs)
# 11. [Darcy's Law II (YouTube)](https://www.youtube.com/watch?v=fL6fvdbz3vY)

# ## Outline
# - Aquifers
# - Material Properties
# - Darcy's Law

# ## Groundwater and Aquifers
# 
# Groundwater hydrology is the study of water beneath the surface of the Earth
# 
# ![](GroundwaterSketch.png)
# 
# Groundwater usually is found in porous media (not underground rivers). A porous medium is
# comprised of solid space and void or pore space. Liquids and gasses are found in the pore space, the solid matrix forms the physical
# structure of aquifers and other geologic formations of interest.
# 
# ![](PorousMedia.png)
# 
# The ratio of total pore volume to bulk medium volume is the porosity.
# 
# ![](PorosityCalculation.png)

# ### Aquifers
# An **aquifer** is an underground layer of water-bearing rock or sediment that stores and transmits groundwater. It is a critical resource for supplying fresh water to wells, springs, and natural ecosystems.
# 
# - Store water (water bearing formations)
# - Transmit water (in economically useful quantities)
# 
# Aquifers are classified as confined, unconfined, and/or leaky (a single unit can exhibit all three classifications).
# 
# A confined aquifer draws its water from a geologic formation upper bounded by a layer that does not readily transmit water.  Visualize a pipe filled with sand; the interior of the pipe will behave like a confined aquifer.
# 
# ![](ConfinedAquifer.png)
# 
# An unconfined aquifer draws its water from a geologic formation that is not upper bounded - the aquifer has the equivalent of a free surface.  A bathtub filled with sand and water will behave like an unconfined aquifer. 
# 
# ![](UnconfinedAquifer.png)
# 
# A leaky aquifer is a hybrid of the two extremes, and there can be leakage between layers.  Most real aquifers are somewhat leaky.
# 
# ![](LeakyAquifer.png)

# ## Material Properties
# 
# ### Porosity
# 
# Porosity is the ratio of total pore volume to bulk medium volume;
# 
# $n = \frac{V_{pore}}{V_{total}}$
# 
# Range in values is large for geologic materials
# 
# ![](PorosityTable.png)
# 
# 
# ### Specific Yield
# 
# A concept related to porosity is the **specific yield** $S_y$ of a material.  
# 
# $S_y$ is the amount of water that will drain from a porous medium under the influence of gravity.
# 
# $S_r$ is the amount of water left behind in the material and is called the specific retention.
# 
# ![](SpecificYield.png)
# 
# The specific yield is important in water supply as it represents the amount of water that can drain to wells.  Thus when making groundwater reservoir estimates the water in storage should be based on the specific yield and not porosity.
# 
# Two additional related terms are: water content and saturation.
# 
# 
# ### Storativity
# 
# Storativity refers to the ability of a porous medium to store water within its bulk.
# 
# The mechanisms of storage are:
# - draining and filling of the pore space
# - compression/decompression of the water, and
# - compression/decompression of the solids.
# 
# In an unconfined aquifer the draining and filling of the pore space is the most significant mechanism.
# 
# ![](StorageUnconfined.png)
# 
# $S=\frac{V_{water}}{\Delta h A}$
# 
# In a confined aquifer, the compression and decompression of the solids structure is the primary mechanism of storage.
# 
# ![](StorageConfined.png)
# 
# $S=\frac{V_{water}}{\Delta h A}$
# 
# The formula is the same for either case, but the magnitude os $S$ is different (by a lot!)
# 
# Storage per unit thickness of aquifer is called the specific storage.
# 
# ### Average Linear Velocity (in a porous media)
# 
# The discharge $Q$ divided by cross sectional flow area $A$ in a pipe or open channel is the velocity $V$
# 
# In groundwater, some of the area is solid, so the porosity enters the equation as:
# 
# $V=\frac{Q}{nA}$
# 
# The figure below illustrates the concept.
# 
# ![](AverageLinearVelocity.png)
# 
# If the garbage cans are identical, the velocity of the free surface in the marble filled can is bigger.
# 
# - Transmissivity, permeability, hydraulic conductivity
# 
# ### Hydraulic Gradient
# 
# Hydraulic gradient is change in head per unit distance and provides the driving force for groundwater to flow.  It is the same concept as the slope of the EGL in pipe hydraulics.
# 
# ![](HydraulicGradient.png)
# 

# ## Equation(s) of Motion
# 
# ### Darcy's Law
# 
# Permeability refers to the ease which water can flow through a porous material under a specified gradient.  
# 
# Consider the head loss equation for a pipe.
# 
# $\Delta h = f\frac{L}{D}\frac{V^2}{2g}$
# 
# Solve for $V$ 
# 
# $V=\frac{2g D \Delta h}{V f L} $
# 
# or
# 
# $V = \frac{2g \cdot D}{f \cdot V} \frac{\Delta h}{L}$
# 
# The right most term is the hydraulic gradient.  Now multiply by the pipe cross sectional area:
# 
# $Q = [\frac{2g \cdot D}{f \cdot V}] A \frac{\Delta h}{L}$
# 
# The term in the square brackets is the inverse of the pipe permeability (dependent on $V$, $Re$, and $k_s$)
# 
# 
# Permeable materials offer little resistance, while impermeable materials offer a lot of resistance.  In the pipe analog, large $k_s$ would cause a large $f$ for any $Re$ maening that pipe has small permeability.
# 
# Darcy's law was established experimentally 1856.  
# 
# ![](FilterColumn.png)
# 
# Total discharge through a filter, $Q$, was proportional to:
# 1. Cross sectional area of flow, $A$,
# 2. head loss $h_1 − h_2$.
# 
# And $Q$, was inversely proportional to:
# 1. the length of the filter column, $L$.
# 
# The relationship is expressed as
# 
# $Q \propto A\frac{h_1-h_2}{L}$
# 
# The head loss can be expressed as $\Delta h$ so the expression is
# 
# $Q \propto A\frac{\Delta h}{L}$
# 
# The constant of proportionality is called the hydraulic conductivity, $K$ so Darcy' law is
# 
# $Q = KA\frac{\Delta h}{L}$

# If we examine the two flow models we observe the two models have the same structure:
# 
# -   Pipe:$Q =[\frac{2g \cdot D}{f \cdot V}]A\frac{\Delta h}{L}$
# - Filter:$Q =KA\frac{\Delta h}{L}$
# 
# So the Hydraulic conductivity plays the same role in the relationship between flow and head loss in filter flow as does the square bracket term in the pipe flow model.
# 
# :::{note}
# The pipe flow is non-linear, notice the square bracket contains $V$ both explicitly, and in the friction factor by its dependence on Reynolds number.
# :::
# 
# The constant of proportionality is called the hydraulic conductivity.  Permeability is sometimes used interchangeably. In reservoir engineering the permeability is related to K, but not numerically identical.
# 
# $K = \frac{k \rho g}{\mu}$

# ## Section End
