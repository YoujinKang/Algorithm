import sys
from collections import Counter
input = sys.stdin.readline

name = list(input().rstrip())
name.sort()
# 전체 개수가 짝수: 모든 요소가 짝수여야함
# 전체 개수가 홀수: 단 하나의 요소만 홀수고 나머지는 짝수여야함

result = []
counter = Counter(name)

if len(name) % 2 == 0:
    for k, v in counter.items():
        for _ in range(v // 2):
            result.append(k)
    reversed_result = result[::-1]
    result += reversed_result
else:
    odd, odd_char = 0, ''
    for k, v in counter.items():
        if v % 2 == 1:
            odd_char = k
            odd += 1
            if odd > 1:
                result = []
                break
        for _ in range(v // 2):
            result.append(k)
    reversed_result = result[::-1]
    result.append(odd_char)
    result += reversed_result

if len(result) != len(name):
    print("I'm Sorry Hansoo")
else:
    print(''.join(result))