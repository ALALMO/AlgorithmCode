import sys

row, col = map(int, input().split())
MIN_VALUE = sys.maxsize
MAX_VALUE = 0



for i in range(row):
    card = list(map(int, input().split()))
    MIN_VALUE = min(card)
    MAX_VALUE = max(MIN_VALUE, MAX_VALUE)

print(MAX_VALUE)
