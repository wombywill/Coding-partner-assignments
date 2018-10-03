import random

num_sixes = 0
num_sevens = 0
num_rolls = int(input('Enter number of rolls:\n'))

if num_rolls >= 1:
    for i in range(num_rolls):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        roll_total = die1 + die2

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

#number 2 and 3 additional program (need a while loop with a break)
while True:
    num_rolls = int(input('Enter number of rolls : '))
    if num_rolls<1:
        break

    termCount = [0,0,0,0,0,0,0,0,0,0,0,0,0];
    for i in range (num_rolls):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        roll_total = die1 + die2
        termCount[roll_total]+=1;
    print(termCount)

#number 1 additional program
for i in range(2,13):
    print("%2ds : "%i,end="")
    for j in range(termCount[i]):
        print("$",end="")
    print()
    



    
