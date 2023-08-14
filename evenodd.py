num1 = int(input("enter fisrt number"))
num2 = int(input("enter second number"))

if num1%2==0:
    if num2%2==0:
         print("both are even")
    else:
         print("first number is even and second one is odd")   
else:
    if num2%2==0:
        print("first number is odd and second one is even")
    else:
        print("both are odd")