import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns


'# The Jungle Game 🌳'

'''Welcome to the 🌳 JUNGLE's survival memory game!

Your mission is to feed all the animals of the jungle to save them.
To do that, you have to find and match each animal behind the trees to its favourite meal.

**How to play the game**
\nAt each round you will flip 2 trees and find the matching animal-food pair.
To flip the tree, you need to enter the wanted index, by writing its column and row positions.
The game will loop while you have chances left.

** Example:** 
\n 1st round: flip 2 trees by inputing the index: 'column-row' positions
-> 'A-1'
-> 'B-2'
'''


# animals
monkey = '🐵'
bear = '🐻'
rabbit = '🐇'
lion = '🦁'
squirrel = '🐿'
panda = '🐼'
mouse = '🐀'
worm = '🐛'

# food
banana = '🍌'
honey = '🍯'
carrot = '🥕'
meat = '🍖'
nuts = '🥜'
bamboo = '🎍'
cheese = '🧀'
leaf = '🥬'

animals = [monkey, bear, rabbit, lion, squirrel, panda, mouse, worm]
food = [banana, honey, carrot, meat, nuts, bamboo, cheese, leaf]
pairs_list = [animals, food]
pairs = dict(zip(animals, food))
pairs_df = pd.DataFrame(pairs_list, index=['animal','food'], columns=list(range(1,9))).T


## Defining grids

# the initial blank grid
x = "🌳"

blank =  [[x,x,x,x],
          [x,x,x,x],
          [x,x,x,x],
          [x,x,x,x]]
blank_grid = pd.DataFrame(blank, columns=['A','B','C','D'])

# Saves only right answers
round_grid = blank_grid.copy()

# the current game's answer grid
rand_grid = np.random.choice(animals+food, 16, replace=False).reshape(4,4)
answer_grid = pd.DataFrame(rand_grid, columns=['A','B','C','D'])

# Variables
rows = list(range(answer_grid.shape[0]))
cols = list(answer_grid.columns) + [col.lower() for col in list(answer_grid.columns)]
chances=30


## Main Game function:

def round_play(round_number: int, round_grid: pd.DataFrame)-> tuple:
    '''
    This function requests to the player his choices by receiving 2 arguments:
        - The current round number (int)
        - The current round grid (DataFrame)
    And returning: 
        - Round grid (with the matched pairs when answer is correct)
    '''
    
    import time
    st.write ('\n', f'ROUND #{round_number}:','\n', round_grid)

    time.sleep(2)
    
    temp_grid = round_grid.copy()
    
    # Choosing first tree:
    
    while True:
        guess1 = str(st.text_input("FIRST PAIR: Which 🌳 do you choose? (column-row position)")).split('-')
        
        try:
            col1 = guess1[0].strip()   
            row1 = int(guess1[1].strip())
             
            if len(guess1) == 2 and row1 in rows and col1 in cols:
                st.write  (f'You chose the 🌳 in position {guess1}.')
                temp_grid.loc[row1, col1] = answer_grid.loc[row1,col1]
                st.write (temp_grid)
                break
            else:
                st.write (guess1)
                st.write  ('\n', "You must enter: 'column letter' + '-' + 'number of row' of the 🌳")
        except:
            st.write  ('\n', "You must enter: 'column letter' + '-' + 'number of row' of the 🌳")
            
    # Choosing 2nd tree:
    while True:        
        guess2 = str(input("SECOND PAIR: Which 🌳 do you choose? (column-row position)")).split('-')
        
        try:
            col2 = guess2[0].strip()
            row2 = int(guess2[1].strip())

            if guess2 == guess1:
                print ("You must choose a different 🌳 ")

            else:
                if len(guess2) == 2 and row2 in rows and col2 in cols :
                    print (f'You chose the 🌳 in position {guess2}.')
                    temp_grid.loc[row2,col2] = answer_grid.loc[row2,col2]
                    print(temp_grid)
                    break
                else:
                    print ('\n', "You must enter: 'column letter' + '-' + 'number of row' of the 🌳")

        except:
            print ('\n', "You must enter: 'column letter' + '-' + 'number of row' of the 🌳")


    # Verify compatibility :
    ## verifying if first choice is an animal or food:
    g1 = temp_grid.loc[row1, col1]
    g2 = temp_grid.loc[row2,col2] 

    if g1 in animals:
        g1_complement = pairs.get(g1)

    else:
        g1_complement = [animal for animal, food in pairs.items() if food == g1][0]

    if g1_complement == g2:
        print("It's match! 🎊")
        round_grid = temp_grid 
        
    else:
        print("It's not a match😔, keep looking!💪")
        round_grid = round_grid
        
    return round_grid


# PLAY game
rand_grid = np.random.choice(animals+food, 16, replace=False).reshape(4,4)
answer_grid = pd.DataFrame(rand_grid, columns=['A','B','C','D'])

for rounds in range(chances):
    
    if rounds == 0:
        init_game = str(st.text_input('Are you ready to play? (yes / no) '))
        if init_game in ["Yes", "yes", 'Y', 'y']:
            blank_grid
            st.write('\n', 'These are the animals and their favourite meal:','\n')
            st.write(pairs_df)
            rounds += 1
        else:
            st.write('Thank you and see you next time!')
        
    elif rounds >= 1:
        if sum(sum(round_grid.values != answer_grid.values))!= 0:
            round_grid
            result = round_play(rounds, round_grid)
            round_grid = result

        elif sum(sum(round_grid.values == answer_grid.values))== 16:
            print('Congratulations! You saved all the animals from the jungle!')

print ("Game Over! You ran out of chances! :( ")

