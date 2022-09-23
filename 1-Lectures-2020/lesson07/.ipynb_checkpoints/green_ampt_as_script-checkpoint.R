# ***********************************************************
# Green-Ampt Infiltration Models (for pedagogical use)
# ***********************************************************
# Constants:  PSI: soil suction at interface (L)
#             DELTHETA: change in soil moisture content 
#                                    (analog to porosity) (dimensionless)
#             K : saturated hydraulic conductivity (L/T)
#             DELT: Time step increment (simulation constant)
# Variables: GA_CUM: value of cumulative infiltration for some given time.
#
# Functions: 
#        GA_rate: computes potential infiltration rate.  
#                 Requires GA_CUM specification, returns Inf for GA_CUM=0
#    GA_accum: computes accumulated infiltration from GA_CUM 
#              to current value given intensity and GA_rate.
#
GA_rate<-function(K,PSI,DELTHETA,GA_CUM){
  K*((PSI*DELTHETA/GA_CUM)+1)
}
GA_accum<-function(intensity,infiltration_rate,DELT,GA_CUM){
  min(intensity,infiltration_rate)*DELT+GA_CUM
}
# Usage  
GA_rate(1.09,11.01,0.247,0)
GA_accum(1.08,Inf,0.167,0)
# As a nested call
GA_accum(1.08,GA_rate(1.09,11.01,0.247,0),0.167,0)
# ******************************************************
#  Now to work the example: pg 144 Example 5.4.1 in CMM 
# ******************************************************
# First the raw rainfall cumulative values:
accum_rain<-c(0.00,0.18,0.39,0.65,0.97,1.34,1.77,2.41,3.55,6.73,8.38, 
              9.19,9.71,10.13,10.49,10.77,11.01,11.20,11.37)
# The elapsed time in minutes
elapsed_time<-seq(0,180,10) 
# build the other arrays in the example
incr_rain<-accum_rain # make a second vector, fill to get length OK
# set first value to zero
incr_rain[1]<-0 
# Now populate the vector (note indexing) and unit conversion (minutes2hours)
for (i in 2:19) 
  (incr_rain[i]<-accum_rain[i]-accum_rain[i-1])/
  ((elapsed_time[i]-elapsed_time[i-1])/60) 
# Same game for intensity
rain_rate<-incr_rain 
# set last value to zero
rain_rate[19]<-0
for(i in 1:18)rain_rate[i]<-incr_rain[i+1]/
  ((elapsed_time[i+1]-elapsed_time[i])/60)
# Now the Green-Ampt computations
f_rate<-seq(0,18)# array for rate
F_depth<-seq(0,18)# array for depth
for (i in 1:19){
  f_rate[i]<-GA_rate(1.09,11.01,0.247,F_depth[i]); 
  F_depth[i+1]<-GA_accum(rain_rate[i],f_rate[i],0.167,F_depth[i])
}
# Now plot everything
par(mfrow=c(3,2))
#
plot(elapsed_time,accum_rain,xlim=c(0,180),ylim=c(0,12),
     xlab="Time(minutes)",ylab="Depth(cm)",type="s",main="Accum. Rain")
#
plot(elapsed_time,f_rate,xlim=c(0,180),ylim=c(0,24),
     xlab="Time(minutes)",ylab="Rate(cm/hr)",
     type="s",main="Infiltration Potential Rate")
#
plot(elapsed_time,incr_rain,xlim=c(0,180),ylim=c(0,4),
     xlab="Time(minutes)",ylab="Depth(cm)",type="s",main="Incr. Rain")
#
plot(elapsed_time,F_depth[1:19],xlim=c(0,180),ylim=c(0,12),
     xlab="Time(minutes)",ylab="Depth(cm)",type="s",main="Infiltration Depth")
#
plot(elapsed_time,rain_rate,xlim=c(0,180),ylim=c(0,24),
     xlab="Time(minutes)",ylab="Rate(cm/hr)",type="s",main="Intensity")
#
plot(elapsed_time,accum_rain-F_depth[1:19],
     xlim=c(0,180),ylim=c(0,12),xlab="Time(minutes)",ylab="Depth(cm)",
     type="s",main="Excess Rain Depth")
cbind(elapsed_time,accum_rain,accum_rain-trunc(F_depth[1:19]*100)/100)