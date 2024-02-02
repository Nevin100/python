#Variables and initialisation 
num1=454
k = "Nevin"
op= "Delhi"
#basically variable num1 has been assigned a value 454,similiarly k has been assigned value Nevin and correspondingly rest..... 

#Global and local variabales

num1=int(input("Enter your number:"))
num2=int(input("Enter your number2:"))

if num1 > num2:
    c=10
    print(num1,"is greater than",num2)
    
else:
    print(num2,"is greater than",num1)
    
print(c)
#num1 and num2 are global variables while c is local.. you will get an error while displaying the variables c value......