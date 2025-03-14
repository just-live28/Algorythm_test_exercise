# 하노이 탑

# 원판n개를 a->b번으로 옮겨야 함
# 원판 n-1개를 a->(6-(a+b))로 옮기기
# 마지막 원판을 a->b번으로 옮기기
# 원판 n-1개를 (6-(a+b)->b번으로 옮기기

# hanoi(n, start, end)
# n이 0일 때 아무것도 하지 않고 return

# 6 - (현재위치 목표위치)

# 20이하인 경우 : 과정 출력
# 20 초과인 경우 : 숫자만 출력

# d[1] = 1
# d[2] = 3
# 3- 7, 4- 15

# 전 거 두 배 + 1

def hanoi(n):
    if n == 1:
        return 1
    return hanoi(n-1) * 2 + 1

def print_hanoi(n, start, end):
    if n == 0:
        return

    print_hanoi(n-1, start, 6-(start+end))
    print(start, end)
    print_hanoi(n-1, 6-(start+end), end)

n = int(input())
if n <= 20:
    print(hanoi(n))
    print_hanoi(n, 1, 3)
else:
    print(hanoi(n))