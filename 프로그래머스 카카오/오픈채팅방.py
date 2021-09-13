def solution(records):
    answer = []
    auth = {}
    for record in records:
        tup = list(map(str, record.split()))
        if tup[0] == "Enter" or tup[0] == "Change":
            auth[tup[1]] = tup[2]
    for record in records:
        tup = list(map(str, record.split()))
        if tup[0] == "Enter":
            answer.append(auth[tup[1]] + "님이 들어왔습니다.")
        elif tup[0] == "Leave":
            answer.append(auth[tup[1]] + "님이 나갔습니다.")

    return answer
