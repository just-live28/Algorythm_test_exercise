# 알파벳 대문자를 처리하는 트라이 구현
# 각 문자의 idx: ord('S') - 65
ROOT = 1
unused = 2
MX = 10000 * 500 + 5
chk = [False] * MX
nxt = [[-1] * 26 for _ in range(MX)]

# 문자→인덱스 변환 함수
def c2i(c):
    return ord(c) - 65

# insert: 문자열 추가 함수
def insert(s):
    global unused
    cur = ROOT
    for c in s:
        # 자식 정점이 없는 경우 새롭게 추가
        if nxt[cur][c2i(c)] == -1:
            nxt[cur][c2i(c)] = unused
            unused += 1
        # 자식 정점으로 이동
        cur = nxt[cur][c2i(c)]
    # 문자열 끝에 도달했다면 단어 표시
    chk[cur] = True

# erase: 문자열 삭제 함수
def erase(s):
    cur = ROOT
    for c in s:
        # 없는 단어를 지우려고 할 경우 return
        if nxt[cur][c2i(c)] == -1:
            return
        cur = nxt[cur][c2i(c)]
    # 해당 단어의 단어 표시 해제
    chk[cur] = False

# find: 문자열 검색 함수
def find(s):
    cur = ROOT
    for c in s:
        # 검색할 단어가 없는 단어인 경우 return
        if nxt[cur][c2i(c)] == -1:
            return False
        cur = nxt[cur][c2i(c)]
    # 해당 단어 표시 여부에 따라 존재 여부 반환
    return chk[cur]