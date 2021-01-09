# HW4
# Q4

import numpy as np
import matplotlib.pyplot as plt

# (a)
# Plot the distribution of the mixture distribution where X is selected with probability p 
# and Y with probability (1−p) for three different values of p.

# (b)
# For each value of p you chose, 
# what is the mean and variance of the resulting distribution?

np.random.seed(1)


def mix(p):
    n = 10000 
    mu = [0, 4]
    sigma = [1, 2]
    data = []
    
    for i in range(n): 
        Z = int(np.random.choice((0,1),1,(p, 1-p))) 
        data.append(np.random.normal(mu[Z], sigma[Z], 1))
    
    arr_data = np.array(data)
    plt.hist(arr_data, bins=400)
    plt.show() #(a) plot the distribution
    
    mean = np.mean(data)
    var = np.var(data)
    print("Mean=",mean) #(b) find mean and variance of the distribution
    print("Variance=",var)

mix(0.1)
mix(0.6)
mix(0.9)


# (c)
# Let p = 0.5 and for n = 1,2,4,8,32 plot the distribution of the average of 
# n samples from the mixture distribution. What is the distribution converging to?

def mix_samples(p):
    n = 10000 
    mu = [0, 4]
    sigma = [1, 2]
    data = []
    
    for i in range(n): 
        Z = int(np.random.choice((0,1),1,(p, 1-p))) 
        data.append(np.random.normal(mu[Z], sigma[Z], 1))
    
    arr_data = np.array(data)
    return arr_data


def central_limit(n):
    i = 0
    total = 0
    while i < n:
        total = total + mix_samples(0.5)
        i = i + 1
    mean = total / n


    plt.hist(mean, bins=400)
    plt.show()


    
central_limit(1)
central_limit(2)
central_limit(4)
central_limit(8)
central_limit(32)

# Conclusion: 
# As the sample size n increases, the mixture distribution 
# will converge to mean=2 following the Central Limit Thereom.




# (d) Foreachvalueofn,whatisthemeanandvarianceofyoursampling distribution 
# (i.e. the variance of the averages)? Compute this from your sampled values,
# not using a formula.


def result(n):
    i = 0
    total = 0
    while i < n:
        total = total + mix_samples(0.5)
        i = i + 1
    mean = total / n
    
    mean_samples = np.mean(mean)
    var_samples = np.var(mean)
    print("When n =",n)
    print("Mean=",mean_samples)
    print("Variance=",var_samples)
        
    
   
result(1)
result(2)
result(4)
result(8)
result(32)
    
    
    
    
    
    
    
    
    



