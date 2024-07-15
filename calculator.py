print("welcome to the calculator")
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
print("enter 1 for addition")
print("enter 2 for subtraction")
print("enter 3 for multiplication")
print("enter 4 for division ")
c=int(input("enter the operation you want to perform(1,2,3,4) :"))
if c==1:
    print("addition of two numbers is:",a+b)
elif c==2:
    print("subtraction  of two numbers is:",a-b)    
elif c==3:
    print("multiplication of two numbers is:",a*b)
elif c==4:
    if b==0:
        print("invalid choice")
    else:
     
     print("division of two numbers is:",a/b)
else :
    print("invalid choice...try again ")