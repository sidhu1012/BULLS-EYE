#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random

num = random.randint(1,100)

print("                       WELCOME TO BULL'S EYE!                 \n")
print("                   Here are some rules for the game")
print("1. I'm thinking of a number between 1 and 100")
print("2. If your guess is more than 10 away from my number, I'll tell you you're FAR")
print("3. If your guess is within 10 of my number, I'll tell you you're CLOSE")
print("                       SO LET'S START THE GAME!")


guesses = [0]


# In[7]:


while True:

    guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))
    
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue

    if guess == num:
        print(f'CONGRATULATIONS, YOU HIT THE BULLS EYE IN ONLY {len(guesses)} GUESSES!!')
        break

    guesses.append(guess)
    
    if abs(num-guess) <= 10:
        print('CLOSE!')
    else:
        print('FAR!')


# In[ ]:




