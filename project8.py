a=0
while True:
    while a<1:
      menu=input("menu(m):")
      print(" ===== MANEGE MONY =====")
      print("1.your mony")
      print("2.your cost")
      print("3.your goal for save mony:")
      print("4.Remaining mony")
      a=a+1

    choice=input("(1.2.3.4):")
    if choice=="1":
        mony=int(input("mony:"))
    elif choice=="2":
        cost=int(input("cost:"))
    elif choice=="3":
        goal=int(input("save_mony:"))
    elif choice=="4":
         cal=mony-cost-goal
         print(cal)

