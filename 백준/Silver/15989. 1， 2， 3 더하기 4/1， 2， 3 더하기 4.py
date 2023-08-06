import sys
input = sys.stdin.readline

d = [1] * 10001

# 2가 추가되는 경우
# d[2]: 1*2, 2, d[3]: 1*3, 1+2, d[4]: 1*4, 1*2+2, 2+2, d[5]: 1*5, 1*3+2, 1+2+2
for i in range(2, 10001):
    d[i] += d[i - 2]

# 3이 추가되는 경우
# d[3]: d[3], 1+3, d[4]: d[4], 1*2+3, 2+3, d[5]: d[5], 1*2+3, 2+3 
for i in range(3, 10001):
    d[i] += d[i - 3]


# d[i]에 동시에 d[i-2]와 d[i-3]을 하게 되면 
# d[5]에 사용되는 d[3]에서 이미 3을 추가하는 경우가 더해지기 때문에 중복됨



t = int(input())
for _ in range(t):
    n = int(input())
    print(d[n])