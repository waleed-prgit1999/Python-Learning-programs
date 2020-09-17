import random
import pygame

list = ["rock","scissor","paper"]
n = 1 ; u = 0 ; c = 0 ; t = 0
pygame.mixer.init()
pygame.mixer_music.load("Free to Fly.ogg")
pygame.mixer_music.play(-1)
while n<=10:
    print("Enter your choice \n 1.Rock\n 2.Scissor \n 3.Paper")
    inp = int(input())
    val = list[inp-1]
    choice = random.choice(list)
    if choice == "rock" and val == "scissor":
        print("Computer won")
        c=c+1
    elif choice == "rock" and val == "paper":
        print("Computer Won")
        c=c+1
    elif choice == "scissor" and val == "rock":
        print("You Won")
        u = u + 1
    elif choice == "scissor" and val == "paper":
        print("Computer Won")
        c = c + 1
    elif choice == "paper" and val == "rock":
        print("You Won")
        u = u + 1
    elif choice == "paper" and val == "scissor":
        print("You Won")
        u = u + 1
    elif choice == val:
        print("Game Tied")
        t = t+1
    n=n+1
pygame.mixer_music.stop()
if u>c:
    print("You won the game")
elif c>u:
    print("Computer won the game")
else:
    print("Game Tied")
print(f"\n\t\tScorecard\nYou:{u}\nComputer:{c}\nTied:{t}")
'''
a= random.randrange(1,100)
print(a)
list = ["king","qween","ace","jack","10","2"]
random.shuffle(list)
print(list)'''