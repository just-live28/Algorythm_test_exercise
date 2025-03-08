# AC(정수 배열 연산)
# R(뒤집기) : 배열에 있는 수 뒤집기



# D(버리기) : 첫 번째 수를 버리기(비어있을 때 사용 시 error 발생)

# 함수를 조합해 한 번에 사용 가능 (AB, RDD)
# 연속해서 이뤄진다.


# 테스트 케이스 t (1~100)
# 수행할 함수 p (1~100000)
# 배열 원소 개수 n (0~100000)
# 배열 (1~100개) [~~~]형태
# R이 1인 경우, 뒤에서 빼기
# R이 0인 경우, 앞에서 빼기

# print('RRDD'.count('D'))

from collections import deque

def print_result(q, reverse):
    length = len(q)
    print('[', end='')
    if reverse == 0:
        for i in range(length):
            if i == length-1:
                print(q.popleft(), end='')
            else:
                print(q.popleft(), end=',')
    else:
        for i in range(length):
            if i == length-1:
                print(q.pop(), end='')
            else:
                print(q.pop(), end=',')
    print(']')

t = int(input())
for _ in range(t):
    cmd = input()
    n = int(input())
    arr = input()[1:-1]
    if arr == '':
        q = deque()
    else:
        q = deque(map(int, arr.split(',')))
    # 0 정방향(popleft), 1 역방향(pop)
    enable = True
    rev = 0
    for i in cmd:
        if i == 'R':
            rev = 1 - rev
        else:
            if not q:
                enable = False
                break
            if rev == 0:
                q.popleft()
            else:
                q.pop()
    if enable:
        print_result(q, rev)
    else:
        print('error')