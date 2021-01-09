#HW2

### Q1-(a) ###

import random
import numpy as np

random.seed(11)

# Q1-(a)
def flip_p(num,n,p,goal):
    count = 0

    for i in range(num):  
        Heads = np.random.binomial(n,p) #fair coin must follow binomial distribution
        if Heads == goal:
            count = count +1 #count if 5 Heads occurs

        
    
    result = count / num #calculate the probability
    return result
    

flip_p(1000000,20,0.5,5)



# Q1-(b)

def at_least(num,n,p,g1,g2,g3,g4,g5): 
    count = 0
    
    for i in range(num):
        Heads = np.random.binomial(n,p)

        if Heads == g1 | g2 | g3 | g4 | g5:
            count = count + 1 #count if the quantity of Heads doesn't satisfied at least 5 Heads
    
    result = count / num
    result = 1 - result # all possibility - not satisfied 
    return result


at_least(1000000,20,0.5,4,3,2,1,0)       



