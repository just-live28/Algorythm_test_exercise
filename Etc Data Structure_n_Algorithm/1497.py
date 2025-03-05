# 기타 n(1~10) 곡 m(1~50)
# 기타가 k개 선택되었고, k index의 기타를 선택해야 함.

def count_song(stat):
    return bin(stat).count('1')

def func(k, stat):
    global min_count, max_song
    
    enable_song = count_song(stat)
    if enable_song > max_song:
        max_song = enable_song
        min_count = k
    elif enable_song == max_song and k < min_count:
        min_count = k
    
    if k == n:
        return

    for i in range(k, n):
        func(k+1, stat | guitars[i])

n, m = map(int, input().split())
guitars = [0] * n
for i in range(n):
    brand, enables = input().split()
    guitars[i] = int(enables.replace("Y", "1").replace("N", "0"), 2)

max_song = 0
min_count = -1
func(0, 0)
print(min_count)