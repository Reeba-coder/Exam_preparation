# Fibonacci Series
def number(n):
    a,b=0,1
    for i in range (n):
        print(a,end=" ")
        a,b=b,a+b
n=int(input("Enter a number:"))
number(n)