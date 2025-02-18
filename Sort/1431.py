def compare(word):
    total = 0
    for w in word:
        if w.isdecimal():
            total += int(w)
    return total

n = int(input())
words = []
for _ in range(n):
    words.append(input())

words.sort(key = lambda x : (len(x), compare(x), x))
for word in words:
    print(word)