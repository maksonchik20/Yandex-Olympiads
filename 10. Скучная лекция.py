cnt = 0
s = input()
sl = {}
length = len(s)
for i in range(length):
    if sl.get(s[i]) is not None:
        sl[s[i]] += (i+1) * (length - i)
    else:
        sl[s[i]] = (i+1) * (length - i)
    
for el in sorted(sl.items(), key=lambda x:x[0]):
    print(el[0] + ': ' + str(el[1]))