############# Parameters ################
S = 44; d = 0.01; v = 0.30; r= 0.05; K= 44; t=0; T=1/2;
############# Functions #################

d1 = (log(S/K)+(r-d+0.5*v^2)*(T-t))/(v*sqrt(T-t)) # d1
d2 = (log(S/K)+(r-d-0.5*v^2)*(T-t))/(v*sqrt(T-t)) # d2
call.premium = S*exp(-d*(T-t))*pnorm(d1)-K*exp(-r*(T-t))*pnorm(d2)
call.premium
