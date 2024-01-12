from math import floor

print("\nPasscode Generator\n")

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
    day = user_input[:2]
    month = user_input[3:4]
    year = user_input[4:]
    if int(day) > 31:
        print('')
        continue
    if int(month) > 12:
        print('')
        continue
    if int(year) < 1900:
        print('\nYou must enter a year after 1900.')
        continue
    break

day = int(day)
month = int(month)
year = int(year)

passcode = floor((((day * 7 + month * 11 + year) * day) - 19) / month)

print(f"\nYour passcode is {passcode}.")

while True:
    exit_input = input('''\nTo exit this program, type exit
: ''').lower()
    if exit_input == 'exit':
        print('\nExiting program...')
        exit()
    else:
        continue