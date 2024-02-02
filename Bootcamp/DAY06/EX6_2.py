#Write a program to get a number from user,pass that number to a function as a parameter and display table for that number..

num=int(input("Enter the number:"))
print("Table for the given number:",num,"is as follows:")
def displaytable(a):
    for i in range(1,11):
        print(a,"*",i,"=",a*i)
        
displaytable(num)
        
        