con={}
while True:
    print("===== CONTACT =====")
    print("1.add contact")
    print("2.show contact")
    print("3.serch contact")
    print("4.delete contact")
    print("5.exit")
    p=input("please input your choice:")
    if p=="1":
        name=input("name:")
        phone=input("phone:")
        con[name]=phone
    if p=="2":
        for key,value in con.items():
            print(f"{key}:{value}")

    elif p=="3":
        serch=input("serch[name]:")
        if serch in con.keys():
            print(f"{serch}:{con[serch]}")
        else :
            print("not found")
    elif p=="4":
        delet=input("delete:")
        if delet in con:
            del con[delet]
            print("delet success")
        else :
            print("not found")
    elif p=="5":
        print("have good day:)")
        break

