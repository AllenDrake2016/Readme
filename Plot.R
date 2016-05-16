xv<-seq(-2,2,by=0.1)
plot(xv,exp(xv),type='l',xlab='x',
ylab='exp(x)',main='y=exp(x)',las=1)

xv<-seq(0,5,by=0.1)
plot(xv,log(xv),type='l',xlab='x',
ylab='ln(x)',main='y=ln(x)',las=1)
lines(c(0,5),c(0,0),col='red',lwd=1)

#X is binomial with p=0.5 and n=10. Plot the probability function of X
f=function(x){dbinom(x,size=10,prob=0.5)}
plot(1:10,f(1:10),type='h',lwd=10,col='blue',ann=FALSE,las=1)
title(main="Binomial Probability Function, n=10, p=0.5",xlab="x",ylab="p(x)")

v=rbinom(1000,size=1023,prob=0.439)
hist(v,n=50,col='red')


## A first example of stochastic simulation ##
# Parameters
a=0.15;d=0.01;v=0.33;S0=40;dt=0.001
# Random Normal Numbers
rn=rnorm(1000,mean=0,sd=1)
#Stock Price Vector
S=1:1000;S[1]=S0
# Recurrence relation
for(i in 2:length(S)){S[i]<-S[i-1]+(a-d)*S[i-1]*dt+
v*S[i-1]*sqrt(dt)*rn[i-1]}
# Plot the stock price
plot(S,type="l",ann=FALSE,las=1,axes=FALSE)
title(main="Stochastic Simulation of Stock Prices",
xlab="Time in months",ylab="Stock Price")
box()
ma=10*ceiling(0.1*max(S))
mn=10*floor(0.1*min(S))
axis(2,at=seq(mn,ma,by=5),las=1)
axis(1,at=seq(0,1000,length=12),lab=1:12)
par (mfrow=c(3,2))
par (mfrow =c(rows,columns))