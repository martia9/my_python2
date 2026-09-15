List=[]
while True:
   print("===== TO-DO LIST =====")
   print("1.add task ")
   print("2.shows task ")
   print("3.delet task ")
   print("4.Exite ")
   p=input("please enter your choice : ")
   if p=="1":
     b=input("enter your task : ")
     List.append(b)
   if p=="2":
     print("your tasks:")
     for i,task in enumerate(List,1):
      print(f"{i}. {task}")
   if p=="3":
       c=int (input("which task do you want to delet? "))
       List.pop(c -1)
   if p=="4":
       print("have good day:)")
       break
  

