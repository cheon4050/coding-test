def solution(food_times, k):
    food_min_time = sorted(food_times)
    cnt = 0
    fcnt = 0
    answer = 0
    for time in range(len(food_min_time)):
        food_min_time[time] -= cnt
        if k < food_min_time[time] * (len(food_times) - fcnt):
            for a in range(food_min_time[time], 0, -1):
                if k >= a * (len(food_times) - fcnt):
                    k -= a * (len(food_times) - fcnt)
                    break
            food_min_time[time] += cnt
            answer = food_min_time[time]
            break
        k -= food_min_time[time] * (len(food_times) - fcnt)
        cnt += food_min_time[time]
        fcnt += 1
    else:
        return -1
    for i in range(len(food_times)):
        if food_times[i] < answer:
            continue
        k -= 1
        if k < 0:
            return i + 1
