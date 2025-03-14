from itertools import combinations

dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))

for seven in combinations(dwarfs, 7):
    if sum(seven) == 100:
        seven_list = sorted(list(seven))
        for i in seven_list:
            print(i)
        break