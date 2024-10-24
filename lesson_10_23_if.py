# Define the known

# pumpkins = int(input("How many pumpkins ya' got? (Whole numbers only): ")) #optimal pumpkin inventory = 1500

# p_ship = 400

# # Calculate the unknown
# if pumpkins < 600:
#     print("Pumpkin emergency! Only " + str(pumpkins) + " pumpkins")
#     pumpkins = pumpkins + (2 * p_ship)
#     print("Pumpkins ordered")
# elif pumpkins < 1200:
#     print("Time to order some pumpkins. (" + str(pumpkins) + ") left")
#     pumpkins = pumpkins + p_ship
#     print("Pumpkins ordered")
# elif pumpkins == 1500:
#     print("Whoa! Exactly 1500 pumpkins!")
# else:
#     print("No order needed")

# Display the results
#print("Now we have " +str(pumpkins) + " pumpkins")

apples = int(input("How many apples are in inventory? "))

if 0 < apples < 10:
    print("There is an error in inventory. Please review.")
elif apples != 0:
    print("Yeah, we got apples")
else:
    print("We are out of apples")