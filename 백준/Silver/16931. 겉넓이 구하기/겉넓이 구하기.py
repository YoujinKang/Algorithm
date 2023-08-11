import sys
input = sys.stdin.readline

n, m = map(int, input().split())
boxes = [list(map(int, input().split())) for _ in range(n)]

# 뒷면: 첫 박스면 각 박스의 수. 두번째 부터는 뒤쪽으로부터 이전의 박스의 수보다 작거나 같으면 0, 크면 차이 만큼
# 앞면: 다음 박스보다 작거나 같으면 0, 크면 차이만큼. 마지막 박스는 각 박스의 수
# 왼쪽면: 첫 박스면 각 박스의 수. 두번째 부터는 왼쪽으로부터 이전의 박스의 수보다 작거나 같으면 0, 크면 차이 만큼
# 오른쪽면: 다음 박스보다 작거나 같으면 0. 크면 차이만큼. 마지막 박스는 각 박스의 수
# 아랫면: 박스의 수가 0 보다 크면 1
# 윗면: 박스의 수가 0보다 크면 1

cnt = 0
for i in range(n):  # 0, 1, 2
    for j in range(m):  # 0, 1, 2
        # 뒷면
        if i == 0:  # 뒷면의 첫 박스들
            cnt += boxes[i][j]
        else:  # i >= 1
            cnt += max(0, boxes[i][j] - boxes[i-1][j])

        # 앞면
        if i == n-1:  # 마지막 박스
            cnt += boxes[i][j]
        else:  # i < n-1 . 처음부터 마지막 박스 직전까지
            cnt += max(0, boxes[i][j] - boxes[i+1][j])

        # 왼쪽면
        if j == 0:
            cnt += boxes[i][j]
        else:  # j >= 1
            cnt += max(0, boxes[i][j] - boxes[i][j-1])

        # 오른쪽면
        if j == m-1:  # 마지막 박스
            cnt += boxes[i][j]
        else:  # j < m-1.  처음부터 마지막박스 직전까지
            cnt += max(0, boxes[i][j] - boxes[i][j+1])

        # 아랫면과 윗면 (종이 한 칸에 놓인 정육면체는 항상 1보다 같거나 큼)
        cnt += 2

print(cnt)