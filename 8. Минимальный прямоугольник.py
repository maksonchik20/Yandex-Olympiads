k = int(input())
x1 = -(10**9) - 1
y1 = -(10**9) - 1
x2 = (10**9) + 1
y2 = (10**9) + 1

for i in range(k):
    x, y = map(int, input().split())
    x1 = max(x1, x)
    y1 = max(y1, y)
    x2 = min(x2, x)
    y2 = min(y2, y)
print(x2, y2, x1, y1)