#HW1

### Q1-(b) ###

from itertools import combinations
from itertools import permutations
   
# Use combination tools

# Define a winner function
def winner(x):
   outcome = len(list(combinations(x,3)))
   outcome = 2 * outcome
   print("Combinations to win the game",outcome)


# Result   
winner('AAA')     # 4 series games
winner('AAAB')    # 5 series games
winner('AAABB')   # 6 series games
winner('AAABBB')  # 7 series games


### Q2 ###

# select movie title Tulsa to do combinations and permutations

# Combination function
def title_combinations(title):
    for i in range(len(title)):  
        for m in combinations(title,i+1):
            print(m)
            count_c = len(list(combinations(title,i+1)))
        print("The amount of combination:",count_c)


# Permutation function        
def title_permutations(title):
    j = len(title)
    for n in permutations(title,j):
        count_p = len(list(permutations(title,j)))
        print(n)
    print("The amount of permutations:",count_p)
 
    
# Result    
title_combinations('Tulsa')
title_permutations('Tulsa')

