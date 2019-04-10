import random

my_hidden_random = random.randint(0, 100)
status = False
guess = 0

while (status != True):
    guess = input("Neue Zahl: ")
    if guess > my_hidden_random:
            print("Zahl zu gross!")
    elif guess < my_hidden_random:
            print ("Zahl zu klein!")
    elif guess == my_hidden_random:
        print("Super, Sie haben die Zahl erraten!")
        status = True
