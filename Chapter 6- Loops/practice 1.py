i=1
while i < 10:
    print(i)
    i=i+1



count = 1
while count <= 5:
    print("count is: ", count)
    count+=1

student= 5
while student<=6:
    print("The class is full : there is no space for an extra student")
    break
    student+=1


cars=['Super safari','G 63','A250']
for i in cars:
    print(i)

left=3
for i in range(left):
    print("only " + str(left), "cookies left")
    left-=1



##activity- calculate square root of eaach nujmber in a range


#sentinals
sum=0
while True:
    x=float(input("enter the number"))
    sum+=x
    if x==-1:
        break
print(sum)
