#!/usr/bin/env python
# coding: utf-8

# # Historical Observations
# 
# While **Design storms** are created from statistical models of observations, incorporating observed precipitation data offers a faithful representation of actual weather patterns and variability, capturing nuances that statistical design storm models may overlook. By using observed data, engineers can better assess real-world risks, enhancing the reliability and precision of infrastructure designs and flood mitigation strategies. Additionally, observed precipitation data provide valuable insights into localized climatic trends and extreme weather events, enabling proactive adaptation measures to address changing environmental conditions effectively.
# 
# At times, there might be motivation to study the source observations - so how to obtain data is important.  There are likely multiple sources of data - here we will examine just a few.
# 
# ## NCDC
# 
# This is the easiest, and may suffice in many situations.  The National Climatic Data Center maintains historical records of climate related data - in some locations over a century of data exist.  Using our study area, and current online tools one can find gages near the study site. 
# 
# [https://www.ncei.noaa.gov/maps/daily/](https://www.ncei.noaa.gov/maps/daily/) will navigate to the NCDC server where daily data are available.  The landing page will look something like:
# 
# ![](ncdc-landing-page.png)

# I have already located our study site - so I'll just zoom in.  In the figure our area is the small yeller rectangles in West Texas.  Zoomed into a useful scale:
# 
# ![](ncdc-zoom-area.png)
# 

# We will select gages by drawing a polygon around them - the one gage close to the study site would be awesome, but it has a really short record, so we will get nearby gages and use some algorithm to map the records to the study site.  To draw the polygon, use the tool on the layers panel, then choose polygon and draw the outline.
# 
# ![](ncdc-polygon-area.png)

# Now we can examine the gages - notice the Caprock Canyon SP gage only has a 3 year record, so alone kind of useless. But the other two extend the historical range considerably.  Next we can add these to the cart for delivery.  
# 
# Once the request is built the NCDC will send a link to a file for you to download.  In secure systems, you have to edit the link by-hand to defeat the anti- Soviet/DPRK/GDR intrusion software - again will demonstrate as needed.
# 
# The data file itself looks like (click on the link in class):
# 
# [3594221.csv](http://54.243.252.9/ce-5361-webroot/ce5361book/lessons/04precipitation/3594221.csv)
# 

# In[ ]:




