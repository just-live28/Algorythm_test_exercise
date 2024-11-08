# def solution(words, queries):
#     answer = []
#     return answer
from bisect import bisect_left, bisect_right

def count_lyrics(array, prefix):
    left_idx = prefix.replace("?", "a")
    right_idx = prefix.replace("?", "z")

    return bisect_right(array, right_idx) - bisect_left(array, left_idx)

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

dictionary = [[] for _ in range(100001)]
reverse_dictionary = [[] for _ in range(100001)]

for word in words:
    length = len(word)
    
    dictionary[length].append(word)
    reverse_dictionary[length].append(word[length-1::-1])

for i in range(100001):
    dictionary[i].sort()
    reverse_dictionary[i].sort()

answer = []
for query in queries:
    if query[0] == "?": # 접미사인 경우     
        result = count_lyrics(reverse_dictionary[len(query)], query[len(query)-1::-1])
    else: # 접두사인 경우
        result = count_lyrics(dictionary[len(query)], query)
    answer.append(result)

print(answer)