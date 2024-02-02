#if nested statement illustration...

number=int(input("Enter your number:"))
if (number%2==0):
    if (number%3==0):
        print("Your number",number,"is divisible by 6")
        