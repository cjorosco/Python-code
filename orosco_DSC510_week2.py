# orosoco_DSC510_week2.py
# 30 November 2019

'''
This program displays a welcome message and prompts the user
for a comppany name and the number of feet of fiber cable.  The cost of installation of the cable
is claculated and prints a receipt for the user

'''


# Display Welcome Message

message = "Welcome to the installation cost calculator"
print(message)

# Prompt for Company Name and assign the input to a variable

prompt = "What is the name of your Company?\n"
company = input(prompt)

# Prompt for the number of feet for installation

prompt = "Enter the number of feet of fiber optic cable to be installed? Enter in whole feet only\n"
cable_feet = input(prompt)
cable_feet = int(cable_feet)

# Calculate cost @ $.87 cents per feet

per_foot_cost = 0.87
total_cost = (cable_feet * per_foot_cost)

# Display the Receipt with the compnay name, number of feet of cable, cost per foot, and total cost.
print("Receipt For Company = {}" .format(company))
print("Number of feet of cable to install = {0}ft. Cost per foot = ${1:.2f}" .format(cable_feet, per_foot_cost))
print("Total Cost = ${0:.2f}" .format(total_cost))
print("Thank you for your business")
