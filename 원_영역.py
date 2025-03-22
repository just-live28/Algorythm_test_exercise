import sys
input = sys.stdin.readline

n = int(input())
points = []
for _ in range(n):
    x, r = map(int, input().split())
    points.append(['{', x - r, 0, 0])
    points.append([')', x + r, 0, 0])
points.sort(key = lambda x : (x[1], x[0]))

stack = []
ans = 1
for i in range(2 * n):
    if points[i][0] == '{':
        if stack:
            if stack[-1][1] == points[i][1] or stack[-1][3] == points[i][1]:
                stack[-1][2] = 1
            else:
                stack[-1][2] = 0
        stack.append(points[i])
    else:
        half = stack.pop()
        if stack and stack[-1][2] == 1:
            stack[-1][3] = points[i][1]
        if half[2] == 1 and half[3] == points[i][1]:
            ans += 1
        ans += 1
print(ans)