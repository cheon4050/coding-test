n, k = map(int, input().split())

arr = [0 for x in range(n+1)]
cnt = 0
result = 0
if n == 2:
    print(2)
if n == 3:
    if k == 1:
        print(2)
    else:
        print(3)
for i in range(2, int(len(arr)-1/2)):
    if arr[i] == 0:
        for j in range(1, int((len(arr)-1)/i)+1):
            if(arr[i*j] == 1):
                continue
            arr[i*j] = 1
            cnt += 1
            if cnt == k:
                result = i*j
                break
    if result != 0:
        print(result)
        break
