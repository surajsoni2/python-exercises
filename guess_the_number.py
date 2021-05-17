import emoji
import random
x=random.randrange(1,50)

number_of_guesses=5
print(emoji.emojize("Python is fun :red_heart:",variant="emoji_type"))
while(number_of_guesses!=0):
    number_of_guesses-=1
    guess=int(input("enter the number guessed :"))

    if number_of_guesses == 0:
        print("game over")
        break
    if guess==x:
        print("you won \U0001F601")
        break

    if guess > x :
        print("enter lesser number \U0001F914")
        print("😏")
        print("you only have ",number_of_guesses,"guesse remain")
        continue

    if guess < x :
        print("enter greater number \U0001F928")
        print("you only have ",number_of_guesses,"guesse remain")
        continue

