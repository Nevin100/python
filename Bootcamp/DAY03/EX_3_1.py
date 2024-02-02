# Write a python program to get 5 integers item from user,store in a list to add all numbers to each other and display result to user

lst=[]
for i in range(5):
    a=int(input("Enter your number:-"))
    lst.append(a)
    
sum=0
for j in lst:
    sum=sum+j
    
print("The sum of all the elements of the list",lst,"is:",sum)


 