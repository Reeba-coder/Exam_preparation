a=input("Enter a string:")
count=0
for i in a:
    if i.lower() in "aeiou":
        count+=1
print("The string has following vowels=", count)