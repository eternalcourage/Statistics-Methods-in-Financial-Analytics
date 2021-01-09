#HW3

import numpy as np
import matplotlib.pyplot as plt

### Q2-(a) ###

X_list=[]

for i in range(100000):
    X = np.random.uniform(low=0,high=100000,size=2)
    X = sum(X)
    X_list.append(X)

plt.hist(X_list, color='blue',bins=100)
plt.show()


### Q2-(b) ###

# Strategy 1 

best_list=[]

for i in range(10000):
    Y = np.random.uniform(low=0,high=100000)
    Z = np.random.normal(loc=Y,scale=1000)
    
    Z_list = Y + Z
    
    best_list.append(Z_list)
    

plt.hist(best_list, color='blue',bins=100)
plt.show()

# Strategy 2

best2_list=[]

for i in range(10000):
    A = np.random.uniform(low=0,high=100000)
    A = 2*A

    best2_list.append(A)


plt.hist(best2_list, color='blue',bins=100)
plt.show()