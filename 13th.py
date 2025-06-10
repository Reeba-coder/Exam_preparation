n = int(input("Enter a number: "))
sum = 0
while n > 0:
    sum += n % 10
    n = n // 10
print("Sum of digits:", sum)

# count even or odd digits
number=[1,2,3,4,5,6,7,8,9]
even=0
odd=0
for i in number:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("Even numbers:", even)
print("odd numbers:", odd)