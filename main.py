## Imports ##
from math import floor

## Functions ##
def verify_input(user_input):
    while True:
        try:
            user_input = int(input('''Please enter a valid date in the ddmmyyyy format
: '''))
        except ValueError:
            print("You did not enter a date.\n")
            continue
        user_input = str(user_input)
        if len(user_input) != 8:
            print('')
            continue
        if int(user_input[:2]) > 31:
            print('')
            continue
        if int(user_input[3:4]) > 12:
            print('')
            continue
        if int(user_input[4:]) < 1900:
            print('\nYou must enter a year after 1900.')
            continue
        return user_input

def exit_loop():
    while True:
        exit_input = input('''\nTo exit this program, type exit
: ''').lower()
        if exit_input == 'exit':
            print('\nExiting program...')
            exit()
        else:
            continue

## Main Code ##
print("\nPasscode Generator\n")

user_input = ''
user_input = verify_input(user_input)

day = int(user_input[:2])
month = int(user_input[3:4])
year = int(user_input[4:])

passcode = floor((((day * 7 + month * 11 + year) * day) - 19) / month)

print(f"\nYour passcode is {passcode}.")

exit_loop()