def prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input("Enter a number:"))
if prime(n) and n%2!=0:
    print(n,"is prime and odd")
else:
    print(n,"is not prime")