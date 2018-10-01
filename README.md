# Coding-partner-assignments
#Calculates the number of times the sum of the randomly rolled dice equals each possible value from 2 to 12.
#Repeatedly asks the user for the number of times to roll the dice, quitting only when the user-entered number is less than 
#1. Hint: Use a while loop that will execute as long as num_rolls is greater than 
#1.Prints a histogram in which the total number of times the dice rolls equals each possible value is displayed 
#by printing a character, such as *, that number of times. The following provides an example:

import random
num_2 = 0
num_3 = 0
num_4 = 0
num_5 = 0
num_6 = 0
num_7 = 0
num_8 = 0
num_9 = 0
num_10 = 0
num_11 = 0
num_12 = 0
num_rolls = int(input('Enter number of rolls:\n'))

while num_rolls >= 1:
    for i in range(num_rolls):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        roll_total = die1 + die2
break
        #Count number of sixes and sevens
        if roll_total == 6:
            num_sixes = num_sixes + 1
        if roll_total == 7:
            num_sevens = num_sevens + 1
        print('Roll %d is %d (%d + %d)' % (i, roll_total, die1, die2))

    print('\nDice roll statistics:')
    print('6s:', num_sixes)
    print('7s:', num_sevens)
else:
    print('Invalid number of rolls. Try again.')

