# 누적합
# 시간복잡도 = O(N * M + K)
N, M = map(int, input().split())
arr = []
for i in range(N):
    input_list = list(map(int, input().split()))
    arr.append(input_list)

prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        prefix_sum[i][j] = arr[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

K = int(input())
count = 0
while count < K:
    i, j, x, y = map(int, input().split())
    total_sum = (prefix_sum[x][y] - prefix_sum[i-1][y] - prefix_sum[x][j-1] + prefix_sum[i-1][j-1])
    print(total_sum)
    count += 1