line = input()
word = input()

count = 0
idx = 0
while True:
    result = line[idx:].find(word)
    if result == -1:
        break
    idx += result + len(word)
    count += 1
print(count)