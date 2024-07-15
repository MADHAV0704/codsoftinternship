print("welcome to the  password generator")
import random
a=input("enter your name:")
b=int(input("enter length of password "))
cAPalpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallalpha="abcdefghijklmnopqrstuvwxyz"
numb="0123456789"
charac="?@#%&*!"
av1=b//3
av2=b%3
def pswrdgen(b):
    p = " "
    for i in range(av1):
        p+=cAPalpha[random.randint(0,25)]
        p+=smallalpha[random.randint(0,25)]
        p+=numb[random.randint(0,9)]
    for i in range(av2):
        p+=charac[random.randint(0,7)]  
    return p     

print(a,"your generated password is:",pswrdgen(b))