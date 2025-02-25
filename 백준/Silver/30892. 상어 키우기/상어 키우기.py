import sys
# 아기상어

N, K, T = map(int, sys.stdin.readline().split())
shark = list(map(int, sys.stdin.readline().split()))

shark.sort()
eat_shark = []
count = 0
for _ in range(K):

    while count < N and shark[count] < T:
        eat_shark.append(shark[count])  
        count += 1  

    if not eat_shark:
        break

    T += eat_shark.pop()

print(T)