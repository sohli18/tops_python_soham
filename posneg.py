num1 = int(input("enter fisrt number"))
num2 = int(input("enter second number"))

if num1<0:
    if num2<0:
        print("both are negative")
    else:
        print("first number is negative and second one is positive")   
else:
    if num2>0:
        print("both are positive")
    else:
        print("first number is positive and second one is negetive")           