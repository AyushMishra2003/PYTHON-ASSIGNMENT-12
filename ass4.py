for x in range(int(input("ENTER AN NUMBER"),),int(input("ENTER AN NUMBER"))+1):
    for y in range(2,x):
        if x%y==0:
            break
    else:
        print(x,end=' ')    