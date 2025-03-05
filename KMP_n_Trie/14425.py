ROOT = 1
MX = 10000 * 500 + 5
unused = 2
check = [False] * MX
next = [[-1] * 26 for _ in range(MX)]

# c - 97
def insert(s):
    global unused
    cur = ROOT
    for i in s:
        if next[cur][ord(i) - 97] == -1:
            next[cur][ord(i) - 97] = unused
            unused += 1
        cur = next[cur][ord(i) - 97]
    check[cur] = True

def find(s):
    cur = ROOT
    for i in s:
        if next[cur][ord(i) - 97] == -1:
            return False
        cur = next[cur][ord(i) - 97]
    return check[cur]

# def erase(s):
#     cur = ROOT
#     for i in s:
#         if next[cur][ord(i) - 97] == -1:
#             return
#         cur = next[cur][ord(i) - 97]
#     check[cur] = False

n, m = map(int, input().split())
for _ in range(n):
    insert(input())
count = 0
for _ in range(m):
    if find(input()):
        count += 1
print(count)