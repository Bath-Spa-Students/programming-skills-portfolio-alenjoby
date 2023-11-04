#Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function 
#should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional 
#arguments to make a shirt. Call the function a second time using keyword arguments.


def make_shirt(size,message):
    print("The size and the message for the given shirt is: ", size, message)

# Call the make_shirt function with specific size and message arguments.
make_shirt(5,"BSU")

#OR

# Alternatively, interactively get the shirt size and message from the user using input().
# Store the values entered by the user in the siz and msg variables.
siz = int(input("Enter your shirt size: "))
siz=int(input("enter your shirt size :" ))
msg=input("enter the message! :")


# Call the make_shirt function with the values entered by the user.
make_shirt(siz,msg)

