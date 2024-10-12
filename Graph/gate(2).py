# 끝에서부터 1까지 검사 : parent[i]가 1을 가리키고 있다면 이미 쓰고 있는 곳임.
# 1이 아니라 자기 자신이라면, parent[i] = 1로 바꾼다.

import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

g = int(input())

parent = [0] * (g+1)

for i in range(1, g+1):
    parent[i] = i

p = int(input())

result = 0
is_p1_use = False
is_count = True
for _ in range(p):
    # 1~G까지 착륙 가능한 비행기
    n = int(input())
    
    is_possible = False
    for i in range(n, 0, -1):
        if find_parent(parent, i) == i:
            if i == 1:
                if is_p1_use == False:
                    is_p1_use = True
                    is_possible = True
                else:
                    is_count = False
                    break
            else:
                is_possible = True
                union_parent(parent, 1, i)
                break
    
    if is_possible == False:
        is_count = False
    
    if is_count == True:
        result += 1

print(result)

