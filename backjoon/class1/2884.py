# 시 : 0~23 / 분 : 0 ~ 59
# 45 분 이상이라면, h 변동 없음.

h, m = map(int, input().split())

if m >= 45:
    print(h, m - 45)
else:
    h = (h - 1) % 24
    print(h, 60 - (45 - m))