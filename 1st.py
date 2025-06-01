a=int(input("Enter a first number:"))
b=int(input("Enter a second number:"))
c=int(input("Enter a third number:"))
if a>=b and a>=c:
    print("The first number is greatest=",a)
elif b>=a and b>=c:
    print("The second number is greatest=",b)
else:
    print("The Third number is greatest=",c)
