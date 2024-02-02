#Illustration of argument and parameter relationship....

#example:1   
def test1(a,b,c):
    print(a+b+c)
    print(a-b-c)
    print(a*b*c)
    
test1(40,50,60)

#example:2
def test2(a,b):
    print("Your name is:",a)
    print("Your age is:",b)
    
name=input("Enter your name please:-")
age=input("Enter your age:")
test2(name,age)
