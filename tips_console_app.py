# Define known values
food_cost = float(input("What was the total cost of the food? "))
tax = food_cost * .08
tip = float(input('Tip amount? '))


# Calculate the unknown
total_due = food_cost + tax + tip

# Display the results
#print("The total due is " + str(total_due))

print("Food cost is " + str(food_cost) + " and 8% tax is " + str(round(tax, 2)))
print("Tip is " + format(tip, ".2f"))
print("Total due is " + str(round(total_due, 2)))
