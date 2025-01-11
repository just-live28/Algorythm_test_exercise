# 접두사 또는 접미사가 포함된 검색어를 통해 검색어별 매치된 단어 수 구하기
# 접두사(빈값가능) + ? (1~N개) / ? (1~N개) + 접미사(빈값가능)
# ?가 없는 경우 없음. 중간에 있는 경우 없음. 양쪽에 있는 경우 없음.

# 2차원 배열 dictionary[글자수][단어인덱스]
# word의 글자 수를 통해, dictionary[글자수] 배열에 추가
# 그리고 단어를 뒤집어서, reverse_dictionary[글자수] 배열에 추가

# dictionary[글자수], reverse_dictionary[글자수] 마다 단어배열 정렬

# 검색어에서 접두사인지, 접미사인지 판단 (?가 첫 글자라면 접미사, 아니면 접두사)
# bisect_left(dictionary[단어수], 쿼리.replace('?', 'a')), bisect_right(dictionary[단어수], 쿼리.replace('?', 'z')) 를 통해 단어 개수 파악 (접미사인 경우 reverse_dictionary[단어수] 를 사용)
from bisect import bisect_left, bisect_right

def find_matches(array, query):
    return bisect_right(array, query.replace('?', 'z')) - bisect_left(array, query.replace('?', 'a'))

def solution(words, queries):
    dictionary = [[] for _ in range(10001)]
    reverse_dictionary = [[] for _ in range(10001)]
    
    for word in words:
        l = len(word)
        dictionary[l].append(word)
        reverse_dictionary[l].append(word[::-1])

    for i in range(1, 10001):
        dictionary[i].sort()
        reverse_dictionary[i].sort()
    
    result = []
    for query in queries:
        l = len(query)
        if query[0] != '?':
            result.append(find_matches(dictionary[l], query))
        else:
            result.append(find_matches(reverse_dictionary[l], query[::-1]))
    
    return result