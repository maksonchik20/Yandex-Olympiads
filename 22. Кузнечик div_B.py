n, k = map(int, input().split())
cnt = 0
dp = [1] * n
for i in range(2, n):
    loc_cnt = 0
    # print(dp)
    for j in range(1, k + 1):
        if i - j >= 0 and i-j <= len(dp):
            loc_cnt += dp[i-j]
    dp[i] = loc_cnt
print(dp[-1])
