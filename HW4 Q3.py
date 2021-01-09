# HW4
# Q3

import numpy as np
import matplotlib.pyplot as plt
 

# (a)
# theoretical mean = sample mean
# lambda = 1 / waiting time = 1/5

exp_commute = 0.8 * (5 + 35) + 0.2 * 30
print("Expected commute time of Alice=",exp_commute)

# (b)
#  Use simulations to estimate the mean and variance of Alices commute time.

np.random.seed(1)

n = 10000
prob=0.8
wait=35
outcome=[]


for i in range(n):
    rn = np.random.binomial(1,prob)
    
    if rn == 0:
        outcome.append(np.random.normal(30,5))

    else:
        car = np.random.exponential(5)
        car = wait + car
        outcome.append(car)
        
mean = np.mean(outcome) #sum(outcome) / n
variance = np.var(outcome)

print("Mean of Alice's commute time:\n",mean)
print("Variance of Alice's commute time:\n",variance)

# (c)
# Estimate by simulation the probability that the bus trip, including the wait,
# is longer than the car trip.


def Bus(m):
    bus_longer=0
    car_longer=0
    bus_c_list=[]
    
    for j in range(m):
        bus_c = 35 + np.random.exponential(5)
        car_c = np.random.normal(30,5)
        
        if bus_c > car_c:
            bus_longer+=1
            bus_c_list.append(bus_c)
        else:
            car_longer+=1
            
    prob_bus_longer = bus_longer / m
    print("When simulation times=",m)
    print("Probability that the bus trip is longer than the car trip:\n",prob_bus_longer)

    arr_bus = np.array(bus_c_list)
    plt.hist(arr_bus,bins=200)
    plt.show()
    
    return arr_bus



# combine into the same x axis to see if it gets narrower

x1 = Bus(1000)  
x2 = Bus(10000) 


# make them into same x-axis to see when iteration increases, it will be narrower
plt.hist([x1,x2],color=['blue','green'],bins=200) 
plt.show()

    
    

