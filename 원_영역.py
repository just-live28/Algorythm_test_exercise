import sys
from bisect import bisect_right

input = sys.stdin.readline
MX = int(1e9)+1

class CircleNode:
    def __init__(self, x, r):
        self.r = r                  # 원의 반지름
        self.x = x                  # 원의 중심점
        self.st = x - r             # 원의 시작값
        self.en = x + r             # 원의 끝값
        self.children = []          # 자식 CircleNode 리스트
        self.children_starts = []   # 자식 노드들의 정렬된 시작값 리스트

def append_circle(node, x, r):
    new_st = x - r
    new_en = x + r
    children = node.children
    starts = node.children_starts
    
    # 자식 노드 리스트가 비어있지 않다면, 시작점을 기준으로 이진 탐색 진행
    if children:
        # new_st보다 작거나 같은 가장 오른쪽 인덱스 찾기
        idx = bisect_right(starts, new_st) - 1
        if idx >= 0:
            candidate = children[idx]
            if new_en <= candidate.en and r < candidate.r:
                append_circle(candidate, x, r)
                return
    # 적절한 자식이 없으면, 현재 노드 자식으로 새 원 삽입
    idx = bisect_right(starts, new_st)
    children.insert(idx, CircleNode(x, r))
    starts.insert(idx, new_st)

def cal_area(node):
    # 자식 원이 없으면 영역 1개
    if not node.children:    
        return 1
    
    radius_sum = 0
    count = 1
    for child in node.children:
        radius_sum += child.r
        count += cal_area(child)
    if radius_sum == node.r:
        count += 1
    return count

n = int(input())
circles = []
for _ in range(n):
    x, r = map(int, input().split())
    circles.append((x, r))
circles.sort(key = lambda x : (-x[1], x[0]))

root = CircleNode(0, MX)
for x, r in circles:
    append_circle(root, x, r)

print(cal_area(root))