
# 주변 상태 체크하기
def check_possible(answer):
    for x, y, a in answer:
        if a == 0:  # 기둥
            # 바닥 위, 다른 기둥 위, 보의 오른쪽 끝, 보의 왼쪽 끝에 있으면 통과
            if y == 0 or [x, y-1, 0] in answer or [x-1, y, 1] in answer or [x, y, 1] in answer:
                continue
            else:
                return False
        elif a == 1:  # 보
            # 왼쪽 끝이 기둥 위, 오른쪽 끝이 기둥 위, 양쪽 끝이 보
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        if b == 0:  # 삭제
            answer.remove([x, y, a])
            if not check_possible(answer):
                answer.append([x, y, a])
        elif b == 1:  # 설치
            answer.append([x, y, a])
            if not check_possible(answer):
                answer.remove([x, y, a])
    answer.sort()
    return answer

