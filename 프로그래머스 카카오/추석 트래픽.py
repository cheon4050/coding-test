def solution(lines):
    answer = [1]
    arr = []
    for line in lines:
        line, ing = line.split()[1], line.split()[2]
        timestamp = (
            int(line[:2]) * 1000 * 60 * 60
            + int(line[3:5]) * 1000 * 60
            + int(line[6:8]) * 1000
            + int(line[-3:])
        )
        arr.append((timestamp - int(float(ing[:-1]) * 1000) + 1, timestamp))
    for i in range(len(arr)):
        cnt = 1
        for j in range(i + 1, len(arr)):
            if arr[i][1] + 1000 > arr[j][0]:
                cnt += 1
        answer.append(cnt)
    return max(answer)
