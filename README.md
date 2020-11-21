# Surfs Up

## Overview
The purpose of this analysis is to find out if Oahu is a sustainable place to open a surf and ice cream shop, based on temperatures in June and December. 

To do this, I used Python, Pandas, and SQL Alchemy. My input file was a SQL Lite file containing weather information.
## Results
Here are three key differences in weather between June and December (all temperatures are in Fahrenheit). See the corresponding images for details.
- The minimum temperature in December is 8 degrees lower than June's lowest temperature.
- The maximum temperature in December is only 2 degrees lower than June's highest temperature.
- During the month of December, temperatures fluctuate 27 degrees as opposed to only 21 degrees for the month of June.

![](./Resources/June_Temps.png)  


![](./Resources/December_Temps.png)  

## Summary
The analysis showed that temperatures are very moderate in Oahu for both June and December. December is just a little cooler.  The standard deviation was low, meaning data points are very close to the average temperature. It seems that people could both surf and eat ice cream in both months. 

We know that it rains a lot in Hawaii, and it's unlikely that people will visit the shop on those days. To find the number of days in which there will be little to no sales, these additional queries could be run:
- Find the number of days it rained in June and the number of days it rained in December.
- Find the rainfall amount for the month of June and the rainfall amount for the month of December.



