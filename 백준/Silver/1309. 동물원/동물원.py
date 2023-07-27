import sys 

n = int(sys.stdin.readline())

def res(k):
    return k % 9901

# no, left, right
cage = [1, 1, 1]

for _ in range(n-1):
    temp = [0, 0, 0]  # 이번 단계의 no, left, right 저장 할 리스트  
    temp[0] = sum(cage) # all case possible. cage는 이전 단계의 no, left, right
    temp[1] = cage[0] + cage[2]  # 이번 단계에서 left를 넣으려면 이전 단계에서 no거나 right거나 
    temp[2] = cage[0] + cage[1]  # 이번 단계에서 right를 넣으려면 이전 단계에서 no거나 left거나 
    cage = [res(t) for t in temp]  # temp를 cage로 업데이트

print(res(sum(cage)))