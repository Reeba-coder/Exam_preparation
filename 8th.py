# String in Variable
name="Reeba"
print(name.upper())
print(name.lower())
print(name.title())
print(name[0:3])
print("Reeba " in name)

a=input("Enter a string:")
print("My name is ",a)
print("Hello,"+a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
fruits=["Apple", "Banana","Mango","Orange"]
mangolen=len(fruits)
print(mangolen)
print(fruits[0:4])
b=input("Enter first name:")
c=input("Enter second number:")
print(b+c)

# Arthmetic operators
x=int(input("Enter a first number:"))
y=int(input("Entera second number:"))
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x**y)
print(x%y)

# comparison operators
print(x==y)
print(x!=y)
print(x>=y)
print(x<=y)
print(x>y)
print(x<y)

#Logical operarors
print(x>=10 and y<=3)
print(x>=10 or y<=3)
print(not(x>=10 or y<=3))

# Identiy operators
x=["Ali", "Ahmad"]
y=["Ali", "Ahmad"]
z=y
print(x==y)
print(y is z)
print(x is z)
print(z is not y)
print(z!=y)
print("Ahmad" in y)

