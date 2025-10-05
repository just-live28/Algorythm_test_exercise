word = input()
n = len(word)

suffixes = []
for i in range(n):
    suffixes.append(word[i:])
suffixes.sort()

for s in suffixes:
    print(s)