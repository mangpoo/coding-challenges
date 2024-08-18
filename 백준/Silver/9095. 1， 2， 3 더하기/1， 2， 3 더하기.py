# 1, 2, 3 더하기

T = int(input())

dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

while(T > 0):
    result = int(input())
    print(dp[result])
    T = T - 1