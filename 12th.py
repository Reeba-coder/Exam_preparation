#Reverse string
a=input("Enter a string:")
print("The string is reversed:", a[::-1])

# Check palindrome
a=input("Enter a string:")
if a==a[::-1]:
    print("The string is palindrome:", a)
else:
    print("The string is not palindrome:",a)