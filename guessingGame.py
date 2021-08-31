import random;

chances = 0
number = random.randint(1,9)
guess = input("Guess a number from 1 through 9")

    

while chances < 5:
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    
    if guess != number:
        guess = input("Guess a number from 1 through 9")
        chances+=1



if not chances < 5:
    print("You Lose! The right answer was",number,)