import random
number = random.randint(1,101)
num=0
while num<=6 :
  num1 =int(input("enter your guess :"))
  num=num+1
  if num1==number:
    print("you guessed correctly")
    break
  elif num1<number:
    print("up down ")
  elif num1>number:
    print("less down")
  else :
      print("ereor")