import random
print 'number game will be started'
num=random.randint(1,100)
#print num
while True:
    guess=raw_input('enter a number:')
    guess=int(guess)
    if num==guess:
        print 'u won the game'
        break
    elif guess<num:
        print 'ur no is low'
    else:
        print 'ur no is high'
        
    

