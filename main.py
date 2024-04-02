#Project name: Score predictor


print("Welcome to score Predictor")
print('You will get 3 chances')
import random
score=random. randint(300, 380)
attempt=3
while attempt >0:
    input1=int(input('Write the Predicted score- '))
    attempt-=1
    if score==input1:
        print ('You are the Choosen one!')
        break
    else:
        print('Wrong Guess!')
        if attempt ==1:
            print ('You have only 1 attempt left')
        elif attempt ==0:
            print('Game Over')
            print ('The correct score is ', score)
        else:
            print(attempt, 'attempts left')