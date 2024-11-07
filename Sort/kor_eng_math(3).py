import sys
input = sys.stdin.readline

n = int(input())

array = []
for _ in range(n):
    name, kor, eng, math = input().split()
    array.append((name, int(kor), int(eng), int(math)))
    
array.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for student in array:
    print(student[0])