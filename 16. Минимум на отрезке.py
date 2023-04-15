from collections import deque
 
 
def mininslidingwindow(A, k):
    mins = []
    deq = deque()
    for i in range(len(A)):
        if (len(deq) > 0) and (deq[0] <= i - k):
            deq.popleft()  # слишком старый индекс
        while len(deq) > 0 and A[deq[-1]] >= A[i]:
            deq.pop()
            # удалить элементы, у которых уже нет шансов стать минимумом в окошке
 
        deq.append(i)
 
        if i >= k - 1:
            mins.append(A[deq[0]])  # голова дека - минимум в текущем окне
 
    return mins
 
 
n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
print(str(mininslidingwindow(arr, k)).replace('[','').replace(']','').replace(',','').replace(' ','\n'))
