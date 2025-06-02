n=int(input("Enter a number:"))
for i in range(1,12):
    if i==9:
        continue
    print(n ,"*",i ,"=", n*i)