#A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if
#they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their 
#age, and then tell them the cost of their movie ticket


#asks the user for their age
age=input("Enter Your Age :")

#create loop which shows the ticket price on the basis of age
for ages in age:
    if age<3:
        print("Congratulations! your ticket is free")
    elif age>3 and age<12:
        print("Your Tickets Cost $10 each")
    else:
        print("Your Tickets $15 each")