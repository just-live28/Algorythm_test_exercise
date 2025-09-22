# L 사용 가능 일수 / P 연속 일수 / V 휴가 일수
# (1) V // P * L 만큼 사용 가능
# (2-1) V % P 가 >= L 이라면 -> L일
# (2-2) V % P 가 < L 이라면 -> (v % P)일

count = 1
while True:
    l, p, v = map(int, input().split())
    if (l, p, v) == (0, 0, 0):
        break
    
    result = 0
    result += v // p * l
    if v % p >= l:
        result += l
    else:
        result += v % p

    print('Case', count, end='')
    print(':', result)
    
    count += 1