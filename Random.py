import random

num = int(input('Guess a number! '))
randt = random.randint(1,50)
while num != randt:
    num = int(input('wrong guess! try again : '))
if num == randt:
    print("That's it!")
