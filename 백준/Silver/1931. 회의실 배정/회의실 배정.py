# 회의실 배정
max_conference = int(input(""))

conference_list = []

for _ in range(max_conference):
    start_time, end_time = map(int, input().split())
    conference_list.append((start_time, end_time))

conference_list.sort(key=lambda x: (x[1], x[0]))

count = 0
last_end_time = 0

for i in conference_list:
    start_time, end_time = i
    if start_time >= last_end_time:
        count += 1
        last_end_time = end_time

print(count)
