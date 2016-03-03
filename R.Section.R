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
