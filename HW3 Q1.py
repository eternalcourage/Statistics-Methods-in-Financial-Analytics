#HW2

import numpy as np
from itertools import combinations 
from scipy.stats import binom

### Q1-(a) ###

p = 0.55 # probability A wins
q = 1 - p # probability B wins

A_4 = binom.pmf(4,4,p)
A_5 = binom.pmf(3,4,p) * p
A_6 = binom.pmf(3,5,p) * p
A_7 = binom.pmf(3,6,p) * p

prob_A = A_4 + A_5 + A_6 +A_7
print("Probability of A wins:", prob_A)


# simulation

x=[]
y=[]
c=[]
n=1000
players=['A','B']
prob=(0.55,0.45)

for i in range(n):
    Awin=0
    Bwin=0
    current_game=0
    list_games=[]
    count=0
    
    while Awin!=4 and Bwin!=4:
        
        current_game = ''.join(np.random.choice(players,1,prob)) 
        list_games.append(current_game) 
        
        if current_game =='A':
            Awin+=1
            count+=len(list_games)
        else:
            Bwin+=1
            count+=len(list_games)
    x.append(list_games)
    y = count
            
countA=0
countB=0

for i in range(n):
    if x[i][-1] == 'A':
        countA+=1
        c.append(x[i])
    else:
        countB+=1
        
prob_A_sim = Awin / (Awin+Bwin)
print("Simulate probability of A wins:", prob_A_sim)

### Q1-(b) ###  

B_4 = binom.pmf(4,4,q)
B_5 = binom.pmf(3,4,q) * q
B_6 = binom.pmf(3,5,q) * q
B_7 = binom.pmf(3,6,q) * q
prob_B_ = B_4 + B_5 + B_6 + B_7


expected_games = 4*(A_4+B_4) + 5*(A_5+B_5) + 6*(A_6+B_6) + 7*(A_7+B_7)
print("Expected games:", expected_games)
  
# simulation

resultb=[]
gamesb=[]


for i in range(1000):
    
    resultb.clear()
    
    for j in range(7):
        currentb = np.random.choice(players,1,prob)  
        resultb.append(currentb)
        
        if(resultb.count('A') == 4 or resultb.count('B') == 4):
            gamesb.append(len(resultb))
            break
            

expected_games_sim = sum(gamesb)/len(gamesb)
print("Simulate expected games:",expected_games_sim)

### Q1-(c) ### 

def winnerA(x):
   outcome = len(list(combinations(x,3)))
   return outcome

A1 = winnerA('AAA')     # 4 series games
A2 = winnerA('AAAB')    # 5 series games
A3 = winnerA('AAABB')   # 6 series games
A4 = winnerA('AAABBB')  # 7 series games

A1 = A1*p**4 
A2 = A2*p**4*q 
A3 = A3*p**4*q**2 
A4 = A4*p**4*q**3 

conA = 4*(A1/prob_A) + 5*(A2/prob_A) + 6*(A3/prob_A) + 7*(A4/prob_A) 
conA




#simulation

resultc=[]
gamesc=[]
gamesc_total=[]

for i in range(1000):
    
    resultc.clear()
    for j in range(7):
        currentc = np.random.choice(players,1,prob)
        resultc.append(currentc)
        
        if (resultc[j][-1]=='A'):
            gamesc_total.append()
            
        if(resultc[j][-1]=='A' and resultc.count('A')==3):
            gamesc.append(len(resultc))
            break
        
conA_sim = sum(gamesc)/len(gamesc)  
print("Simulate expected games given A wins:",conA_sim)

        
        





