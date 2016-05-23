#Chap 11.1

#Put,two period
S=1
v=.3
g=.03
r=.07
K=S
T=1
n=2

h=T/n
u=exp((r-g)*h+v*sqrt(h))
d=exp((r-g)*h-v*sqrt(h))
P_star=((exp((r-g)*h)-d)/(u-d))
Pud=max(0,K-S*u*d);Pud
Pdd=max(0,K-S*d*d);Pdd
payoff=K-S*d;payoff
Pd=exp(-r*h)*(P_star*Pud+(1-P_star)*Pdd);Pd

#Put payoff vector
put.payoff=function(x){max(0,K-x)}
pv = 1:(n+1)
for(i in 1:length(pv)){pv[i]<-put.payoff(S*u^{n+1-i}*d^{i-1})};pv