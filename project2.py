import random
l=["peaper","stone","cut"]
r=random.choice(l)
h=0
a=0
d=0
while h<=4:
  b=input(">")
  print(f"camputer={r}")
  h+=1
  if b==r:
      print("draw")
  elif b=="stone" and r=="cut" :
    print("you win")
    a=a+1
  elif b=="peaper"and r=="stone":
      print("you win")
      a=a+1
  elif b=="cut" and r=="peaper":
      print("you win")
      a=a+1
  elif r=="stone" and b=="cut":
      print("you lose ")
      d=d+1
  elif r=="peaper" and b=="stone":
      print("you lose ")
      d=d+1
  elif r=="cut" and b=="peaper":
      print("you lose")
      d=d+1


print(f"the result is = you{a}  and camputer {d}")
