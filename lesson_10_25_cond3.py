# # Boolean operators

# # recyling inputs
# cans = 0
# bottles = 0
# boxes = 0

# print(cans != 0 and bottles != 5) # both conditions must be true
# print(cans < bottles or bottles < 5) # either condition must be true

# if (cans > 0 or bottles > 0) and not boxes > 0:
#     print('Call the recylcing service for pickup')
# elif boxes != 0:
#     print("We've gotta do something with these boxes.")

## MATCH CASE

greeting = input('Enter your greeting: ')

match greeting:
    case 'Hello':
        print('Hello to you too!')
    case 'Good morning':
        print('Good morning to you too!')
    case other:
        print('Oh, you don\'t say?')

if greeting == 'Hello':
    print('Hi')
elif greeting == 'Good morning':
    print('Good morning')
else:
    print('Oh, you don\'t say?')