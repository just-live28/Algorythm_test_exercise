import sys
input = sys.stdin.readline

n = int(input())

paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

white_count = 0
blue_count = 0

def cal_paper(size, px, py):
    global white_count
    global blue_count
    
    base = paper[px][py]
    for x in range(px, px + size):
        for y in range(py, py + size):
            if paper[x][y] != base:
                unit = size // 2
                for a in range(2):
                    for b in range(2):
                        cal_paper(unit, px + a * unit, py + b * unit)
                return
    
    if base == 1:
        blue_count += 1
    else:
        white_count += 1

cal_paper(n, 0, 0)

print(white_count)
print(blue_count)