def solution(n):
    MOD = 1000000007
    
    if n == 1:
        return 1
    elif n == 2:
        return 3
    
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 3  # 기본 값 설정
    
    for i in range(3, n + 1):
        dp[i] = (3 * dp[i - 2] + 2) % MOD
        for j in range(i - 4, 0, -2):
            dp[i] = (dp[i] + 2 * dp[j]) % MOD
    
    return dp[n]