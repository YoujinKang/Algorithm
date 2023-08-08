import sys
input = sys.stdin.readline

n, x = map(int, input().split())

# B(P)P(P)B, B(BPPPB)P(BPPPB)B, B(B(BPPPB)P(BPPPB)B)P(B(BPPPB)P(BPPPB)B)B, ...
# 총 햄버거 장수를 저장하는 리스트
page, patty = [0] * (51), [0] * (51)
page[0] = 1
patty[0] = 1
for i in range(1, 51):
    page[i] = page[i-1] * 2 + 3
    patty[i] = patty[i-1] * 2 + 1

# to avoid page[-1], patty[-1]
page.append(0)
patty.append(0)

def burger(i, k, p):
    half = (page[i] + 1) // 2 
    start = 1
    end = page[i] 

    if k == half:
        return p + 1 + patty[i-1]
    elif k == start:
        return p 
    elif k == end:
        return p + patty[i]
    else:
        if k < half:
            return burger(i-1, k-1, p)
        else:
            p = p + 1 + patty[i-1]
            return burger(i-1, k-half, p)
        
print(burger(n, x, 0))