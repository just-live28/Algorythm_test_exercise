ROOT = 1
unused = 2
# 최대 문자열 개수 * 최대 문자열 길이 + 패딩
mx = 10000 * 500 + 5
chk = [False] * mx
nxt = [[-1] * 26 for _ in range(mx)]

# c - 65
def insert(s):
    global unused
    cur = ROOT
    for i in s:
        if nxt[cur][ord(i) - 65] == -1:
            nxt[cur][ord(i) - 65] = unused
            unused += 1
        cur = nxt[cur][ord(i) - 65]
    chk[cur] = True

def find(s):
    cur = ROOT
    for i in s:
        if nxt[cur][ord(i) - 65] == -1:
            return False
        cur = nxt[cur][ord(i) - 65]
    return chk[cur]

def erase(s):
    cur = ROOT
    for i in s:
        if nxt[cur][ord(i) - 65] == -1:
            return
        cur = nxt[cur][ord(i) - 65]
    chk[cur] = False