from string import ascii_lowercase
n = int(input())
letters = ascii_lowercase[:n]
data = [int(input()) for _ in range(n)]
cnt = 0
for i in range(n-1):
    if data[i] <= data[i + 1]:
        cnt += data[i]
    else:
        cnt += data[i+1]
print(cnt)
