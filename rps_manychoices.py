# Rock Paper Scissors Spock Devil ..........
name=input("Enter your name: ")
print("Hello, {}".format(name))
file=open('rating.txt', 'r', encoding='utf-8')
score=0
for line in file:
    na,sc=line.split(" ")
    if na==name:
        score=int(sc)
        break
import random
newset=input().split(',')
newset = list(filter(None, newset))
if newset:
    game=newset
else:
    game=['rock','paper','scissors']
print("Okay, let's start")
while True:
    user=input()
    if user=='!exit':
        print('Bye!')
        break
    if user=='!rating':
        print('Your rating: {}'.format(score))
        continue
    if user not in game:
        print('Invalid input')
        continue
    new=game[game.index(user)+1:]+game[:game.index(user)]
    userloses=new[:len(new)//2]
    userwins=new[len(new)//2:]
    computer=random.choice(game)
    if user==computer:
        print('There is a draw ({})'.format(computer))
        score+=50
        continue
    elif computer in userwins:
        print('Well done. Computer chose {} and failed'.format(computer))
        score+=100
        continue
    elif computer in userloses:
        print('Sorry, but computer chose {}'.format(computer))
        continue
