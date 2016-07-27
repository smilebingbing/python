import random

num=random.randint(0,100)
while True:
    try:
        guess=int(raw_input("Enter 1-100"))
    except ValueError,e:
        print ("Enter 1-100")