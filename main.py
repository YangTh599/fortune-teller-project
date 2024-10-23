# Thayer Yang
# 23 OCT 2024
# Fortune Teller

#Imported modules: randint, sleep, sys
from random import randint
from time import sleep
import sys

# FUNCTIONS

# Delayed String Print Function
def delayedPrint(str,time):
    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(time)
    sys.stdout.write('\n')
    

# LISTS

# Fortunes List
fortunes = ['You are a winner!', 'A secret admirer will soon send you a sign of affection!', 'The one you love is much closer than you think!', 'Good things will happen to you by the end of the day today!', 'Fame and fortune will be yours if you take the time to learn Python!', 'I\'m just a computer program, and have no magical powers!']

# Magical Colors List
magical_colors = ['blue', 'red','green','yellow']

# Gets Name input from user
name = input("Please enter your first name: \n")
print(f'Welcome to my fortune teller {name.title()}.')
sleep(1)

#Set true while in fortune teller mode
telling = True

#Asking user if they want to have their fortune told.
print('Do you want me to tell you your fortune? [y/n]:')

#Active while loop when user is getting their fortune told.
while telling:

    #ready input, either yes or no: used to see if user wants a fortune telling
    ready = input()
    sleep(2)

    #If input was yes, user gets fortune told
    if ready.lower() in ['yes', 'y', 'ye']:

        #boolean condition checks if color given was magical
        is_magical = False
        #While given color is not magical
        while not is_magical:
            #Color inputted by user
            color = input('Okay! To get your fortune, please input a magic color [blue/red/green/yellow]:\n')

            #Activates if color given is in magical colors list
            if color in magical_colors:

                delayedPrint('Getting your fortune. . .', .2)
                sleep(2)

                print(f'Here is your fortune {name.title()}:')
                sleep(1)

                delayedPrint(fortunes[randint(0,len(fortunes)-1)], .1)
                sleep(.5)

                # Asks user if they want another fortune telling
                print('Do you another fortune telling? [y/n]:')

                #sets boolean condition to true to break color while loop
                is_magical = True
            
            # Else statement is input it not the colors in the lists
            else:
                print("Please choose a magic color of either 'blue', 'red', 'green', or 'yellow'.\n")
                sleep(3)

    # If user does not want their fortune rea
    elif ready.lower() in ['no','n']:
        sys.stdout.write('oh')
        sleep(.5)
        delayedPrint('...',1)

        # thanks user for their time.
        print('Well, thank you for letting me read you your fortunes today '+name.title()+"!")

        sleep(2)

        print('Goodbye!')

        # Sets fortune teller mode to false, breaks the while loop.
        telling = False

    # Run if ready input was neither 'yes' nor 'no'
    else:
        print("Please enter 'yes' or 'no' [y/n].")

quit()