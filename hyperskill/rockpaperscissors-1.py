#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Write your code here
name=input("Enter your name: ")
print("Hello, {}".format(name))
file=open('rating.txt', 'r', encoding='utf-8')
score=0
for line in file:
    na,sc=line.split(" ")
    if na==name:
        score=sc
        break
import random
game=['rock','paper','scissors']
newset=[input().split(',')]
if newset:
    game=newset
print("Okay, let's start")
while True:
    user=input()
    if user=='!rating':
        print('Your rating: {}'.format(score))
        continue
    if user=='!exit':
        print('Bye!')
        break
    if user not in game:
        print('Invalid input')
        continue
    loss=0
    computer=random.choice(game)
    if user==computer:
        print('There is a draw ({})'.format(computer))
        score+=50
        continue
    elif user=='paper':
        if computer=='scissors':
            loss=1
    elif user=='scissors':
        if computer=='rock':
            loss=1
    elif user=='rock':
        if computer=='paper':
            loss=1
    if loss:
        print('Sorry, but computer chose {}'.format(computer))
        continue
    else:
        print('Well done. Computer chose {} and failed'.format(computer))
        score+=100
        continue

