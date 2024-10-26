import random

target=random.randint(1,100)
while True:
    userChoice=(input("Guess the target or Quit(Q)  :"))
    if (userChoice=="Q"):
        break

    userChoice=int(userChoice)
    if(userChoice==target):
        print("Congratulation!,You guessed the correct number")
        break
    elif(userChoice<target):
        print("The number you entered was too small.Take a bigger guess....")
    else:
        print("The number you entered was too big . Take a smaller guess.....")

print("------GAME OVER------")