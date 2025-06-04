# Factorial Series
def factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
n=int(input("Entera number:"))
print("The factorial of ", n, "is", factorial(n))