#A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if
#they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their 
#age, and then tell them the cost of their movie ticket

# Ask the user for their age
age = int(input("What is your age? "))

# Determine the cost of the ticket based on the user's age
if age < 3:
  ticket_price = 0
elif age >= 3 and age <= 12:
  ticket_price = 10
else:
  ticket_price = 15

# Tell the user the cost of their ticket
print(f"The cost of your movie ticket is ${ticket_price}.")
