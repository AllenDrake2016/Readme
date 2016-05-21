#Call payoff vector
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
Cuu=max(0,S*u*u-K);Cuu
Cud=max(0,S*u*d-K);Cud
payoff=S*u-K;payoff
Cu=exp(-r*h)*(P_star*Cuu+(1-P_star)*Cud);Cu



call.payoff=function(x){max(0,x-K)}
pv = 1:(n+1)
for(i in 1:length(pv)){pv[i]<-call.payoff(S*u^{n+1-i}*d^{i-1})};pv

call.payoff=function(x){max(0,x-K)}
pv1=1:n
for(i in 1:length(pv1)-1){pv[i]<-call.payoff(S*u^{n+1-i}*d^{i-1})};pv1

#ifelse(x<=K,0,x-K)

#sum(dbinom(0:1, 10, 0.4))

#list=1:3;list

2*(sum(list*dbinom(0:2, 10, 0.4)))

