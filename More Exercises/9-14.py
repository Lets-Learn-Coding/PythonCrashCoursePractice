#9-14
from random import randint

class Die():
    def __init__(self, sides = 6):
        self.sides = sides

    def  roll_die(self):
        x = 0
        while x <= 10:
            roll = randint(1, self.sides)
            print (str(roll))
            x += 1
six_dice = Die()
ten_dice = Die(10)
twen_dice = Die(20)

print ('Rolling a 6 sided die 10 times')
six_dice.roll_die()

print ('\n' + 'Rolling a 10 sided die 10 times')
ten_dice.roll_die()

print ('\n' + 'Rolling a 20 sided die 10 times')
twen_dice.roll_die()