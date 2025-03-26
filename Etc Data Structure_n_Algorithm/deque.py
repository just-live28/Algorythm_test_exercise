from typing import Any

class FixedQueue:
    def __init__(self, capacity: int) -> None:
        self.no = 0                     # 현재 데이터 개수
        self.front = 0                  # 맨 앞 원소 커서
        self.rear = 0                   # 맨 끝 원소 커서
        self.capacity = capacity               # 큐의 크기
        self.que = [None] * capacity    # 큐의 본체

    def __len__(self) -> int:
        return self.no

    def is_empty(self) -> bool:
        return self.no <= 0

    def is_full(self) -> bool:
        return self.no >= self.capacity

    # 데이터를 큐에 추가
    def enque(self, x: Any) -> None:
        if self.is_full():
            return
        self.que[self.rear] = x
        self.rear = (self.rear + 1) % self.capacity
        self.no += 1

    # 데이터를 큐에서 삭제
    def deque(self) -> None:
        if self.is_empty():
            return
        val = self.que[self.front]
        self.front = (self.front + 1) % self.capacity
        self.no -= 1
        return val