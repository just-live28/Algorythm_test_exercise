# 스택 첫번째에 엄청 큰 무한 높이의 탑이 존재
# 자기보다 높은 게 나올 때까지 없애버리기. 그리고 그 높은 것의 인덱스를 출력
# 그리고 자기를 append

n = int(input())
towers = list(map(int, input().split()))
stack = []
stack.append((int(1e9), 0))
result = []
for i in range(1, n+1):
    while stack[-1][0] <= towers[i-1]:
        stack.pop()
    result.append(stack[-1][1])
    stack.append((towers[i-1], i))
print(*result)