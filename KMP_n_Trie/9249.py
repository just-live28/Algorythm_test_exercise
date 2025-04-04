import sys

class SuffixAutomaton:
    def __init__(self):
        # 각 상태는 {'len': 길이, 'link': suffix link, 'next': 전이 dict}로 구성
        self.states = [{'len': 0, 'link': -1, 'next': {}}]
        self.last = 0  # 마지막 상태의 인덱스
        self.size = 1  # 현재 상태의 개수

    def add_char(self, c):
        p = self.last
        # 새 상태 curr 생성: 길이는 이전 상태 길이 + 1
        curr = self.size
        self.size += 1
        self.states.append({'len': self.states[p]['len'] + 1, 'link': 0, 'next': {}})
        # p로부터 c에 대한 전이가 없다면 모두 새 전이를 추가
        while p != -1 and c not in self.states[p]['next']:
            self.states[p]['next'][c] = curr
            p = self.states[p]['link']
        if p == -1:
            # 처음부터 전이가 없었으면 새 상태의 suffix link은 0번 상태
            self.states[curr]['link'] = 0
        else:
            q = self.states[p]['next'][c]
            if self.states[p]['len'] + 1 == self.states[q]['len']:
                self.states[curr]['link'] = q
            else:
                # q를 복사한 clone 상태를 생성
                clone = self.size
                self.size += 1
                self.states.append({
                    'len': self.states[p]['len'] + 1,
                    'link': self.states[q]['link'],
                    'next': self.states[q]['next'].copy()
                })
                while p != -1 and self.states[p]['next'].get(c) == q:
                    self.states[p]['next'][c] = clone
                    p = self.states[p]['link']
                self.states[q]['link'] = self.states[curr]['link'] = clone
        self.last = curr

def build_sa(s):
    sa = SuffixAutomaton()
    for ch in s:
        sa.add_char(ch)
    return sa

def find_lcs(sa, T):
    """
    sa: Suffix Automaton built for 문자열 S
    T: 두 번째 문자열
    T를 순회하면서 S와 T의 공통 부분 문자열 중
    최대 길이인 것들을 dp 배열에 기록합니다.
    """
    v = 0    # 현재 automaton 상태
    l = 0    # 현재까지 일치하는 길이
    best = 0 # 최대 공통 부분 문자열 길이
    dp = [0] * len(T)
    for i, c in enumerate(T):
        if c in sa.states[v]['next']:
            v = sa.states[v]['next'][c]
            l += 1
        else:
            while v != -1 and c not in sa.states[v]['next']:
                v = sa.states[v]['link']
            if v == -1:
                v = 0
                l = 0
            else:
                l = sa.states[v]['len'] + 1
                v = sa.states[v]['next'][c]
        dp[i] = l
        if l > best:
            best = l

    # best가 최대 길이, dp[i]==best인 위치에서 T에서 후보가 됨.
    candidates = []
    for i, length in enumerate(dp):
        if length == best and best > 0:
            # T[i-best+1 : i+1]가 공통 부분 문자열 후보
            candidates.append(T[i-best+1 : i+1])
    if best == 0:
        return 0, ""
    # 여러 후보 중 사전 순으로 가장 작은 것을 선택
    return best, min(candidates)

def main():
    input = sys.stdin.readline
    S = input().strip()
    T = input().strip()
    sa = build_sa(S)
    lcs_length, lcs = find_lcs(sa, T)
    print(lcs_length)
    if lcs_length > 0:
        print(lcs)

if __name__ == '__main__':
    main()