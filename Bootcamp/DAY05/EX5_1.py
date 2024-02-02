#Write a program to make a function that take three subject marks from user ,make another function which finds total of three subject marks,make another function which finds average of that marks...

def marks():
    sub1=int(input("Enter your marks for subject1:"))   
    sub2=int(input("Enter your marks for subject2:"))   
    sub3=int(input("Enter your marks for subject3:"))   
    v1=avg(sub1,sub2,sub3)
    print("The average of three subject:",v1)
    v2=total(sub1,sub2,sub3)
    print("The total of three subjects:",v2)

def avg(a,b,c):
    k=(a+b+c)/3
    return k

def total(p,q,r):
    n=(p+q+r)
    return n
        
marks()
