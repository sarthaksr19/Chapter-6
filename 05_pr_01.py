num1 = int(input("enter the number1\n"))
num2 = int(input("enter the number2\n"))
num3 = int(input("enter the number3\n"))
num4 = int(input("enter the number4\n"))

if(num1>num2):
    f1 = num1
else:
    f1 = num2

if(num3>num4):
    f2 = num3
else:
    f2 = num4

if(f1>f2):
    print(f1, " is greater")
else:
    print(f2, "is greater")