import sys
input = sys.stdin.readline

n, m = map(int, input().split())

num_to_name = [None]
name_to_num = {}
for i in range(1, n+1):
    name = input().rstrip()
    num_to_name.append(name)
    name_to_num[name] = i

for _ in range(m):
    quiz = input().rstrip()
    if quiz.isdigit():
        print(num_to_name[int(quiz)])
    else:
        print(name_to_num[quiz])