import random
import time
answer = input("Do you want to roll a dice? Answer with yes or no! " )
i=answer
while i=="yes":
    num = random.randint(1,6)
    print(f"Your number is {num}" )
    i = input("Do you want to continue? Answer with yes or no! ")
else:
    exit()
