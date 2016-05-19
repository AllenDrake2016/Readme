#Chap 11.3

#Call,one period
S=41
v=.4
g=0
alfa=.15
r=.07
K=41
T=.5
n=2

h=T/n
u=exp(v*sqrt(h));u
d=exp(-v*sqrt(h));d
P_star=((exp((r-g)*h)-d)/(u-d));P_star
Cuu=max(0,S*u^2-K);Cuu
Cud=max(0,S*u*d-K);Cud
Cdd=max(0,S*d^2-K);Cdd

Co=exp(-r*h)*(P_star^2*Cuu+2*P_star*(1-P_star)*Cud+(1-P_star)^2*Cdd);Co

