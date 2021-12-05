#!/usr/bin/env python
# coding: utf-8

# Code the logic of RISK strategy board game in case of two players. The attacker rolls 3 red
# dices and the defender rolls 2 blue dices. In step one, we look for the greatest value in the
# dices. The looser losts 1 soldier. If the greatest value is the same at both sides, only the
# attacker losts 1 soldier. In step two, we look for the second greatest value and decide about
# losting 1 soldier as above. The game has 3 possible outcomes: attacker losts 2 soldiers, both
# sides lost 1 soldier each, the defender losts 2 soldiers.
# a) Simulate the game 1000 times and calculate the relative frequency of the three possible
# outcomes.
# b) Simulate the game 1000000 times and calculate the relative frequency of the three
# possible outcomes.
# c) Calculate the exact probability of the three outcomes by analyzing all possible cases
# (positive cases / all cases).
# Print out the results of tasks a, b and c in a tabular form.

# In[185]:


#Import needed libraries
import random


# In[191]:


#variables Declaration
attacker_dices = 3
defender_dices = 2
number_of_turns = int(input("please enter the number of game turn:"))
outcome_dict = {'attacker':0, 'both':0, 'defender':0}


# In[192]:


# a functing to calcualte the results
def risk_game (attacker_dices,defender_dices):
    #start throwing the dices
    #generating sets of dices probability for attacker and defender
    #attacker set
    attacker_score =[]
    for i in range(attacker_dices):
        score = random.randint(1,6)
        attacker_score.append(score)
    print(attacker_score)
    # defender set
    defender_score =[]
    for i in range(defender_dices):
        score=random.randint(1,6)
        defender_score.append(score)
    print(defender_score)

    # find the highest value in each set and compaier it to get the results:

    attacker_highest_dice = max(attacker_score)
    defender_highest_dice = max(defender_score)
#     print(attacker_highest_dice,defender_highest_dice)

    if attacker_highest_dice > defender_highest_dice:
        defender_dices -=1
    else:
        attacker_dices -=1
    return attacker_dices,defender_dices


# In[193]:


#define the number of games that we want to play
for game in range(number_of_turns):
    #in each game we have just 2 rounds
    for round in range(2):
        attacker_dices,defender_dices = risk_game(attacker_dices,defender_dices)
    #calculating  the outcome
    if attacker_dices == 3:
        # the defender lost 2 solders
        outcome_dict['defender'] +=1
    elif attacker_dices == 2:
        # both lost 1 solder
        outcome_dict['both'] +=1
    else:
        # the attacker losts 2 solders
        outcome_dict['attacker'] +=1
    # reset the dices for a new game
    attacker_dices = 3
    defender_dices = 2
# print(outcome_dict)
        


# In[194]:


# results
probabilties = {}
probabilties['attacker']  = outcome_dict['attacker']/number_of_turns
probabilties['both']  = outcome_dict['both']/number_of_turns
probabilties['defender']  = outcome_dict['defender']/number_of_turns
print(outcome_dict)
print(probabilties)


# In[ ]:




