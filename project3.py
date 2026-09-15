
while True:
    num = input("> ")
    if num=="help".lower():
        print("1.sum")
        print("2.minus")
        print("3.multiplication")
        print("4.division")
        print("5.exit")
    elif num=="1":
     num1=float(input("please enter number1= "))
     num2=float(input("please enter number 2="))
     num3=float(num1)+float(num2)
     print(f"{num1}+{num2}={num3}")
    elif num=="2":
        num1=float(input("please enter number1= "))
        num2=float(input("please enter number 2="))
        num3=float(num1)-float(num2)
        print(f"{num1}-{num2}={num3}")
    elif num=="3":
        num1=float(input("please enter number1= "))
        num2=float(input("please enter number 2="))
        num3=float(num1)*float(num2)
        print(f"{num1}*{num2}={num3}")
    elif num=="4":
        num1=float(input("please enter number1= "))
        numnt(f"{num1}/{num2}={num3}")
    elif num=="5":
        print("have good day:)")
        break
    else:
        print("eror")
        print("please enter 1 to 5 :")