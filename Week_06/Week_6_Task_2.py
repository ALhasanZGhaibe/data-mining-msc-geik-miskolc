#!/usr/bin/env python
# coding: utf-8

# We are flipping coin until it turns to its head. If it happens for the n-th time of flipping, the
# player gains 2n dollars. Simulate m games (that is we are playing until flipping m heads).
# What will be the average gain if m=100, m=10000 and m=1000000? 

# In[36]:


#Import needed libraries
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[37]:


# vriable declaration
number_of_experince = int(input('Enter the number of experinces that you want to play please:'))
z=[]


# In[38]:


# strart the game
for game in range(number_of_experince):
    counter=0
    #generate random number 0 or 1
    while 1 :
        x =random.randint(0,1)
        counter+=1
       #check if we get 1 our not if we get 1 break the loop and save the counter value in z
        if x==1:
            break
    z.append(counter)
#calculate the average gain & mean & standard deviation
avg=2*sum(z)/number_of_experince
mean = np.mean(z)
sd = np.std(z, ddof=1)
print(z)
print(sum(z))
print(avg)
print(sd)
print(mean)
# plot the normal distribution
t=np.random.normal(loc=mean,scale=sd,size=(1,2))
sns.distplot(t, hist=False)
plt.show()


# In[24]:





# In[ ]:




