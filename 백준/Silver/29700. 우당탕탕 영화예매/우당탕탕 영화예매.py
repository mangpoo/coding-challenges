# 우당탕탕 영화예매

N, M, K = map(int, input("").split())
result = 0

seat = []
for i in range(N):
    List = list(map(int, input("")))
    seat.append(List)

for i in seat:
    count = 0
    for j in i:
        if(j == 0):
            count += 1
            if (count >= K):
                count -= 1
                result += 1
        else:
            count = 0

print(result)