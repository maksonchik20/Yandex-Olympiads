# Найти частоту повторения букв
# Пример:
# Input:
# Hello, world!
# Output:
     #   
     ##  
  #########
# !,Hdelorw


from sys import stdin

s = {}

for line in stdin:
    line = line.strip()
    for el in line:
        if s.get(el) is not None:
            s[el] += 1
        elif el != ' ' and s.get(el) is None:
            s[el] = 1
sort_s = sorted(s.items(), key=lambda x:ord(x[0]))
_max = 0
end_s = ""
for el in sort_s:
    _max = max(_max, el[1])
    end_s += el[0]
for h in range(_max, 1, -1):
    pr = ""
    for w in range(len(end_s)):
        if s[end_s[w]] >= h:
            pr += '#'
        else:
            pr += ' '
    print(pr)
print('#' * len(end_s))
print(end_s)