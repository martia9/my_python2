import time
import random
chars="abcdefghijklmnopqrstuvwxyz"
password=input("password:")
guss=""
num=0
while guss!=password:
    guss=""
    for i in range(len(password)):
        guss +=random.choice(chars)
        num=num+1
    print("\n trying...!",guss)
    time.sleep(0.0001)

print("password cracked:",guss)
print("numbe of trying:",num)




