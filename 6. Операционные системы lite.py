m = int(input())
n = int(input())

data = []

def compare_segments(line_1, line_2):
    first_pair=max(line_1[0], line_2[0])
    second_pair=min(line_1[1], line_2[1])
    if first_pair < second_pair:
        return(first_pair, second_pair)
    elif first_pair==second_pair:
        return True
    else:
         return False
for i in range(n):
    a, b = map(int, input().split())
    prev_data = []
    for el in range(len(data)):
        if not compare_segments((a,b), data[el]):
            prev_data.append(data[el])
    prev_data.append((a, b))
    data = prev_data
print(len(data))