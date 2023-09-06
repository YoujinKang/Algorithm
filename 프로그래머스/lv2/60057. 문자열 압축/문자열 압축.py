import sys
from collections import deque

def solution(s):
    answer = len(s)
    # 1개 단위부터 압축 단위를 len(s)//2 까지 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]  # 앞에서부터 step까지의 문자열
        cnt = 1
        # step 크기만큼 증가시키며 이전 문자열 prev와 비교
        for j in range(step, len(s), step):
            if prev == s[j:j + step]:  # 확인하는 문자열이 prev와 같다면,
                cnt += 1
            else:  # 다른 문자열이 나왔다면
                prev_str = "".join(prev)
                compressed += str(cnt) + prev_str if cnt > 1 else prev_str
                prev = s[j:j + step]  # prev 업데이트
                cnt = 1
        # 남은 문자열 처리
        prev_str = "".join(prev)
        compressed += str(cnt) + prev_str if cnt > 1 else prev_str
        answer = min(answer, len(compressed))
    return answer
