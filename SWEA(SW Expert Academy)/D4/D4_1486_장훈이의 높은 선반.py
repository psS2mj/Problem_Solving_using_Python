# date: 2020/10/25
# author: psS2mj
# brief: SWEA_1486_장훈이의 높은 선반 (D4)

from itertools import combinations
T = int(input())
for tc in range(1,T+1):
    N, B = map(int,input().split()) # N: 점원의 수, B: 탑의 높이
    height = list(map(int,input().split())) # 점원의 키
    result = list() # 조건을 만족하는 결과값을 저장할 리스트
    # 조합을 이용해 길이가 1 이상인 모든 부분집합 구하기
    for i in range(1,N+1):
        c = combinations(height,i)
        # 각 부분집합마다 합을 구해준다.
        for j in c:
            sum = 0
            for k in j:
                sum += k
            # 키의 합이 B 이상일 때만 리스트에 저장
            if sum >= B:
                result.append(sum)
    # 리스트를 정렬한 뒤 첫 번째 원소를 출력한다.
    print("#{} {}".format(tc,sorted(result)[0]-B))