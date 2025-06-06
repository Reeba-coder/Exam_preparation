for k in range(10):
    print(k, end=" , ")
name="Reeba"
for i in name:
    print(i,  end=" , ")
for k in range(1,20,2): # print odd numbers
    print(k)


for i in range(1,12):
    if(i==10):
        break
    print("5 * ", i, "=", 5*(i))


for i in range(12):
    if (i==10):
        print("Skip iteration")
        continue
    print("5*",i+1,"=",5*i)
# i=0
# while True:
#     print(i)
#     i+=1
#     if(i%100==0):
#         break
