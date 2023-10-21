guests=['edward','elin','emmanuel']

print("Hey, I would like to call you for dinner mr.",guests[0])
print("Miss." + guests[1] + ", You are invited for the dinner")
print("Mr." + guests[2] + " I would Like you to call you for dinner")

# Or

print("As per the restaurant, There is space for only two guests")
# Remove guests from the list using pop() until only two names remain
for _ in range(len(guests) - 2):
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

# Print a message to the two people still on your list
for guest in guests:
    print(f"{guest}, you're still invited to dinner.")

# Use del to remove the last two names from your list
del guests[:]

# Print your list to make sure it's empty
print("Guest list:", guests)