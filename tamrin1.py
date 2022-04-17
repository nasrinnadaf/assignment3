import random
 
words = ('pen', 'book', 'notbook','pencil' , 'eraser', 'chair')
 
correct = random.choice(words)

answer = correct

 
while correct != answer :
    position = random.randrange(len(answer))
    answer = answer[:position] + answer[(position + 1):]
 
guess = input("Guess word:")
guess = guess.lower()
 
while (guess != correct) or (guess == ""):
    print("That is not the correct answer")
    guess = input("enter your guess : ")
    guess = guess.lower()
 
if guess == correct:
    print("You Win!")
