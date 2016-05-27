############# Parameters ################
S = 44; d = 0.01; v = 0.30; r= 0.05; K= 44; t=0; T=1/2;
############# Functions #################
A = S*exp(-d*(T-t)) # prepaid stock price
B = K*exp(-r*(T-t)) # prepaid strike price
C = v*sqrt(T-t) # period volatiltity
d1 = (log(A/B)+C^2/2)/C # d1
d2 = d1 -C # d2
put.premium = B*pnorm(-d2)-A*pnorm(-d1)
put.premium

