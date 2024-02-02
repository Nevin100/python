'''Write a program to get marks from the user and display the grade according to the user marks as follows 
marks>=90,display A
marks>=80,display B
marks>=70,display C
marks>=60,display D
otherwise Fail.......
'''

marks=int(input("Enter your marks:"))
print("Displaying the grade correspondingly to the marks been entered by you... ")

if (marks >= 90):
    print("Your grade for marks",marks,"is: A")
    
elif (marks >=80):
    print("Your grade for marks",marks,"is: B")

elif (marks >=70):
    print("Your grade for marks",marks,"is: C")
    
elif (marks >=60):
     print("Your grade for marks",marks,"is: D")
     
else:
    print("You are failed.....")
     