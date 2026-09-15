import random
num=0
while True:
    roll=input("y/n:")

    if roll=="y":
        x=random.randint(1,6)
        y=random.randint(1,6)
        print(f"({x},{y})")
        num=num+1
        print(f"your roll {num} times")