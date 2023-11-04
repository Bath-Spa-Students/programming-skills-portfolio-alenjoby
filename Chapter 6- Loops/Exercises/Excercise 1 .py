#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,
#print a message saying you’ll add that topping to their pizza.


# a variable that stores the pizza toppings
topings=[]

while True:
    #prompt for user to add toppings
    toping=input("Enter the pizza toping: (or type quit to quit the code)")

#if user type quit the code will break
    if toping == 'quit':
        break
#add the toping to list "Topings"
    topings.append(toping)

print("This are your toppings:")
for i in topings:
    print(i)