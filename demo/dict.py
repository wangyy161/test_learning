import datetime

dict = {}
for i in range(5):
    port = 5000 + i + 1
    pid = i + 6000
    start_time = datetime.datetime.now()
    dict[i + 1] = (port, pid, start_time)
print(dict, "\n", len(dict))


del dict[1]

print(dict, "\n", len(dict))
print(dict[2][2-1])
dict.update({6:(2,3,4)})
print(dict)
dict.update({1:(2,4,4)})
print(dict)
dict = {1: 3, 2:4}