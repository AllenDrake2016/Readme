#Chap 11.3

#Call,one period
S=41
Su=56.75
Sd=31.14
g=0
T=1
n=1

h=T/n
v=(1/2*sqrt(h))*log(Su/Sd);v
u=Su/S
r=(1/h)*(log(u)-v*sqrt(h))+.5*(v^2)+g;r
