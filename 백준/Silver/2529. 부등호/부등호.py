import sys
input = sys.stdin.readline

# A = <<<><<><>
# 3<4<5<6>1<2<8>7<9>0
# 최대, 최소 정수 출력
# 5689023174
# 3456128790


k = int(input())  # 2 <= k <= 9
signs = list(map(str, input().split()))
visited = [0] * 10
min_result, max_result = "", ""

# 3 < 4 를 검사할 때, 3과 < 가 맞춰진 상황에서 4를 넣을지 말지 판단해야함
def check(i: int, j: int, sign: str):
    if sign == "<":
        return i < j
    else:
        return i > j


def solve(cnt: int, answer: str):  # (0, ""), (1, "0"), (2, "01"),
    global min_result, max_result

    if (cnt == k + 1):  # 3
        if len(min_result) == 0:
            min_result = answer
        else:
            max_result = answer
        return

    for i in range(10):
        if visited[i] == 0:  # visited[0] = 0, visited[0] = 1 이므로 패스 -> visited[1], visited[2]
            if (cnt == 0) or (check(int(answer[-1]), i, signs[cnt-1])):  # check(0, 1, <) = True, check(1, 2, >) = False
                visited[i] = 1  # visited[0] = 1, visited[1] = 1, X
                # i = 0 일 때 나머지 숫자에 대해서 쭉 생각해야 하고
                solve(cnt + 1, answer + str(i))  # solve(1, "0"), solve(2, "01"), X, X, ... 으로 solve(2, "01")은 cnt 3을 채우지 못하고 끝남
                # i = 1 이면 또 나머지 숫자에 대에서 쭉 생각해야 하기 때문에 visited[i] = 0으로 리셋
                visited[i] = 0  # visited[1] = 0으로 바뀜. 


solve(0, "")
print(max_result)
print(min_result)


