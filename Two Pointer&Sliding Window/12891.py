# A C G T
# 65 67 71 84

# s - 4

s, p = map(int, input().split())
word = input()
min_a, min_c, min_g, min_t = map(int, input().split())

def check(freq):
    if freq[ord('A')] >= min_a and freq[ord('C')] >= min_c and freq[ord('G')] >= min_g and freq[ord('T')] >= min_t:
        return 1
    return 0

freq = [0] * 91
for w in word[:p]:
    freq[ord(w)] += 1
result = check(freq)
for i in range(s - p):
    freq[ord(word[i])] -= 1
    freq[ord(word[p + i])] += 1
    result += check(freq)

print(result)