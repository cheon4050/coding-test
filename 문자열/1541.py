data = input()
result = ""
index = 0
n = 0
data2 = ""
start = 0
for i in range(len(data)):
    if data[i] == "-" or data[i] == "+":
        start = 0
        data2 += data[i]
    elif start == 0 and data[i] == "0":
        continue
    else:
        data2 += data[i]
        start += 1
data = data2
for i in range(len(data)):
    if data[i] == "-":
        if index != 0:
            result += data[index:i] + ") - ("
            index = i + 1
        else:
            result += data[index : i + 1] + "("
            index = i + 1
    elif i == len(data) - 1:
        if index != 0:
            result += data[index : i + 1] + ")"
        else:
            result += data[index : i + 1]
print(eval(result))
# result2 = ""
# for i in range(len(result)):
#     if i == 0 and result[i] == 0:
#         continue
#     elif (result[i-1] == "-" or result[i-1] == "+" or result[i-1] == "(") and result[i] == "0":
#         continue
#     else:
#         result
