### Q4 ###

import numpy as np


def GamblersRuin(invest,p,upper,lower):
    
    total=100
    invest_list=[]
    q = 1-p
    prob=(p,q)

    while total!=upper and total!=lower:
        
        p1 = np.random.choice([0,1],1,p=prob)
        
        if p1==0:
            total = total + invest * 2    
        
        elif p1==1:
            total = total - invest
            
        invest_list.append(total)
   
    print("Total assets each day:",invest_list)
    print("Total Days:",len(invest_list))

            

GamblersRuin(10,0.55,200,0) #most efficient way to get to $200


#####
GamblersRuin(5,0.55,200,0)
GamblersRuin(10,0.45,200,0)

