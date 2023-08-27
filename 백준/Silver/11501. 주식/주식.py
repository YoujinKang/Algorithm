import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    stocks = list(map(int, input().split()))

    wallet, max_val = 0, 0
    for i in range(len(stocks)-1, -1, -1):  # 뒤에서부터 0까지
        if stocks[i] > max_val:
            max_val = stocks[i]
        else:
            wallet += max_val - stocks[i]

    print(wallet)