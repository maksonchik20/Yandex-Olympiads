# решение за O(n)

# Красотой строки назовем максимальное число идущих подряд одинаковых букв. (красота строки abcaabdddettq равна 3)

# Сделайте данную вам строку как можно более красивой, если вы можете сделать не более k операций замены символа.

# Формат ввода
# В первой строке записано одно целое число k (0 ≤ k ≤ 109)

# Во второй строке дана непустая строчка S (|S| ≤ 2 ⋅ 105). Строчка S состоит только из маленьких латинских букв.

# Формат вывода
# Выведите одно число — максимально возможную красоту строчки, которую можно получить.
from string import ascii_lowercase
k = int(input())
s = input()
res = 0
for search in ascii_lowercase:
    _max = 0
    right = 0
    for left in range(len(s)):
        while k >= 0 and right < len(s):
            if k <= 0 and s[right] != search:
                break
            if s[right] != search:
                k -= 1
            right += 1
        _max = max(_max, right - left)
        if s[left] != search:
            k += 1
    res = max(res, _max)
print(res)
