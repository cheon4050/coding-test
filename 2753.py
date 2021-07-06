k = int(input())

if (k % 400 == 0):
    print(1)
else:
    if (k % 4 == 0):
        if(k % 100 != 0):
            print(1)
        else:
            print(0)
    else:
        print(0)
