num=int(input("ENTER AN NUMBER"))
for x in range(2,num):
    if num%x==0:
        print("NOT PRIME NUMBER ")
        break
else:
    print("PRIME NUMBER")    