import sys

stop = True
cnt = 1
while stop:
    treearr = []
    while True:
        arr = input()
        if not arr:
            continue
        if arr[0] == "-":
            stop = False
            break
        elif arr[-3:] == "0 0":
            for i in arr.split("  ")[:-1]:
                treearr.append(i)
            break
        else:
            for i in arr.split("  "):
                treearr.append(i)
    if stop == False:
        break
    treeoutchack = []
    treeincheck = []
    for i in treearr:
        t_in, t_out = i.split(" ")
        if t_out in treeoutchack:
            print("Case " + str(cnt) + " is not a tree.")
            cnt += 1
            break
        else:
            treeoutchack.append(t_out)
        if t_in in treeincheck:
            continue
        else:
            treeincheck.append(t_in)
    else:
        if len(set(treeincheck) - set(treeoutchack)) != 1:
            print("Case " + str(cnt) + " is not a tree.")
            cnt += 1
        else:
            print("Case " + str(cnt) + " is a tree.")
            cnt += 1
