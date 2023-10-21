#You just heard that one of your guests can’t make the
#dinner, so you need to send out a new set of invitations. You’ll have to think of
#someone else to invite.

#•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.

#•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

#•Print a second set of invitation messages, one for each person who is still in your list.

Names=['shaan','adil','karthikayen','abhishek']
for i in Names:
    print(i,", We are gladly inviting you join us on a Dinner party")

#OR

Guests= ['Alen','Abel','Mary']
msg1=("hello " + Guests[0] + ", You are Invited to the dinner")
msg2=("hello " + Guests[1] + ", You are Invited to the dinner")
msg3=("hello " + Guests[2] + ", You are Invited to the dinner")

print(msg1)
print(msg2)
print(msg3)

print("\nsadly  " + Guests[2] + "Cannot Come to the party")
Guests[2]="JOBY"

msg1=("\nhello " + Guests[0] + ", You are Invited to the dinner")
msg2=("\nhello " + Guests[1] + ", You are Invited to the dinner")
msg3=("\nhello " + Guests[2] + ", You are Invited to the dinner")

print(msg1)
print(msg2)
print(msg3)