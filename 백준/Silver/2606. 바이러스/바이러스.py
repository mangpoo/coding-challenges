from collections import deque

c_count = int(input(""))
couple = int(input(""))

c_number = {}
for i in range(1, c_count + 1):
    c_number[i] = []


while(couple > 0):
    key, value = map(int, input("").split())

    c_number[key].append(value)
    c_number[value].append(key)
    couple -= 1

queue = deque()
queue.append(1)
virus = set()
virus.add(1)

while len(queue) > 0:
    current = queue.popleft()
    c_c = c_number[current]
    for i in c_c:
        if i not in virus:
            virus.add(i)
            queue.append(i)

print(len(virus) - 1)
