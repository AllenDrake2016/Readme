#Chap 11.2

#Call,one period
S=41
v=.3
g=0
alfa=.15
r=.08
K=40
T=1
n=1

h=T/n
u=exp((r-g)*h+v*sqrt(h))
d=exp((r-g)*h-v*sqrt(h))
P_star=((exp((r-g)*h)-d)/(u-d))
Cu=max(0,S*u-K);Cu
Cd=max(0,S*d-K);Cd

delta=exp(-g*h)*((Cu-Cd)/(S*(u-d)));delta
B=exp(-r*h)*((u*Cd-d*Cu)/(u-d));B
rightside=((S*delta)/(S*delta+B))*exp(alfa*h)+(B/(S*delta+B))*exp(r*h)
gamma=log(rightside)/log(exp(h));gamma

