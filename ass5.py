num=int(input("ENTER AN NUMBR"))
for x in range(num,2*num):
    for y in range(2,x):
        if x%y==0:
            break
    else:
        print("NEXT PRIME NUMBER ",x)
        break    