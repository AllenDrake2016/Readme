 ###### Binomial Tree / European Call Option #####

 # Parameters
 r= 0.08; S=41.00; K=40.00; v = 0.30; T=1.000; div = 0.00
 # Functions
 h = function(n){T/n}
 u = function(n){exp((r-div)*h(n)+v*sqrt(h(n)))}
 d = function(n){exp((r-div)*h(n)-v*sqrt(h(n)))}
 # risk-neutral probability of an up move

 p = function(n){(exp((r-div)*h(n))-d(n))/(u(n)-d(n))}
 # Call option payoff function

 call.payoff = function(x){max(0,x-K)}
 # Vector of Call Payoffs

 fp = function(n){cp = 1:(n+1)
 for(i in 1:length(cp)){cp[i]<-call.payoff(S*u(n)^{n+1-i}*d(n)^{i-1})}
 cp}
 # Risk Neutral Expected Payoff

 Ex = function(n){sum(fp(n)*(dbinom(n:0,n,p(n))))}
 # Discount to get time-0 premium

 C = function(n){call.premium=exp(-r*T)*Ex(n);call.premium}
 # Compute Table 12.1

 xs = c(1,4,10,50,100,500)
 premiums = 1:6
 for(i in 1:6){premiums[i]<-C(xs[i])};premiums
