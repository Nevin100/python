# Write a python program to get 5 integers item from user,store in a tuple to multiply all numbers to each other and display result to user.

lst1=[]
for i in range(5):
    k=int(input("Enter your number:-"))
    lst1.append(k)

tple=tuple(lst1)

prd=1
for i in tple:
    prd=prd*i

print("The product of the elements of the tuple",tple,"is:",prd)
    
    
    