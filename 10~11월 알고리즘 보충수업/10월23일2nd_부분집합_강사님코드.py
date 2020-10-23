# 재귀를 이용한 부분집합 구하기 >> DFS
# DFS: 다음 단계로 진행하기 위한 후보군들을 구한다.
# 그 후보 중 하나를 골라 다음 단계로 진행하는 형태

# A = {1,2,3}의 부분집합을 구한다고 하면,
# 각 요소를 선택하거나(O) 선택하지 않을(X) 수 있다.
# => 각 요소의 부분집합 포함 여부 결정!
# 즉, 각 요소 마다 2개씩의 선택지가 있으므로 다 곱해주면 된다.

N = 5
arr = [1,2,3,4,5]
select = [0] * N
# 👨🏻‍🏫멱집합: POWER SET (주어진 집합의 모든 부분 집합들로 구성된 집합)
# idx: 요소의 인덱스
def power_set(select,idx):
    # pass
    if idx >= N: # 👨🏻‍🏫인덱스가 5가 되면 이 조건에 걸려서 끝난다.
        # 조건이 걸리는 시점: 모든 인덱스에 대해 부분집합 포함 여부를 결정한 상태
        # 어떤 요소들이 부분집합에 포함되었는지 확인
        sub_set = list()
        for i in range(N):
            if select[i]: # 값이 1일 때
                # print(arr[i],end=" ")
                sub_set.append(arr[i])
        print(sub_set)
        return

    # 해당 인덱스의 요소의 포함 여부 결정
    # 부분집합에 포함
    select[idx] = 1
    power_set(select,idx+1)
    # 부분집합에 포함되지 않음 (그래도 다음 단계로 진행한다.)
    select[idx] = 0
    power_set(select,idx+1)

    # [1,2,3,4,5]

# 0번 index부터 검사를 시작한다.
power_set(select,0)

# 👨🏻‍🏫하다보면 보입니다. 저도 2년 반 헤맸습니다.
# 👨🏻‍🏫모든 사람이 숙달-반복을 통해 하는 겁니다. 재귀 파이팅!