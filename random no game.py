import random
flag= True
while flag:
    nm = input('type a number for upper bound: ')
    if nm.isdigit():
        print("Lets Play")
        num= int(nm)
        flag= False
    else:
        print('invalid input')

secret= random.randint(1,num)
guess = None 
count = 1

while guess!= secret:
    guess = input('please type a number between 1 and your upper bound')
    if guess.isdigit():
        guess=int(guess)
    if guess == secret:
        print('You won')
    else:
        print("please try again")
        count=+1
print('it took you', count, 'tries')
