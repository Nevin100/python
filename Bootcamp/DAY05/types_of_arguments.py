#Covering various types of arguements...

#keyword argument..

def add(a,b,c):
    print("The sum is:",a+b+c)
    
add(b=50,c=82,a=42) 

#default argument..

def add1(val1,val2=45):
    print("The sum is:",val1+val2)
    
add1(20)
add1(45,64)

