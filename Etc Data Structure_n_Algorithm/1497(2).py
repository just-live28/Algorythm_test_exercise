# 최대한 많은 곡 -> 기타의 최소 개수
# 기타 N(1~10) 곡 M(1~50)
# 각 기타의 스탯을 2진수로 관리

def cal_songs(state):
    return bin(state)[2:].count("1")

def func(k, state, selected):
    global max_songs, min_guitars
    enable_songs = cal_songs(state)
    if enable_songs > max_songs:
        max_songs = enable_songs
        min_guitars = selected
    elif enable_songs == max_songs and selected < min_guitars:
        min_guitars = selected
    
    if k == n:
        return
    
    func(k+1, state | guitars[k], selected+1)
    func(k+1, state, selected)

max_songs = 0
min_guitars = -1
n, m = map(int, input().split())
guitars = [0] * n
for i in range(n):
    _, stat = input().split()
    guitars[i] = int(stat.replace("Y", "1").replace("N", "0"), 2)
func(0, 0, 0)
print(min_guitars)