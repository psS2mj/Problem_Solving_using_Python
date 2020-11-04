# 👨🏻‍🏫 시작지점으로부터 같은 거리에 있는 애들을 처리해주면 된다.("시작지점으로부터 얼마나 떨어져있나?") => BFS

for tc in range(1,11):
    #데이터의 길이와 시작점
    N, start = map(int,input().split())
    #인원 최대 100명, 번호는 1부터 100까지
    arr = list(map(int,input().split()))
    #최대 100명에 대한 정보를 저장할 수 있게 배열 준비
    adj = [[0] * 101 for _ in range(101)]
    #2명의 정보가 한쌍, 2칸씩 읽음
    for i in range(0,len(arr),2):
        adj[arr[i]][arr[i+1]] = 1 # 👨🏻‍🏫 유향 그래프라서 한 방향에만 표시

    #비상 연락이 돌기 까지 오래 걸린시간을 탐색
    #같은 단계에 있는 사람들 끼리 함께 처리 하면됨 >> BFS
    def bfs(start):
        queue = list()
        queue.append((start,0)) # 단계를 체크 해야 함, 시작은 0단계
        visited = [0] * 101
        visited[start] = 1 # 👨🏻‍🏫 시작점을 방문했다는 의미.
        max_cnt = 0
        max_num = 0
        while queue:
            num,cnt = queue.pop(0)
            if cnt > max_cnt:   #연락횟수가 가장크면(가장늦게 연락받으면)
                max_cnt = cnt   #추가
                max_num = num
            elif cnt == max_cnt and num > max_num :
                #시간은 같은데, 숫자가 더 크면,
                max_num = num

            for i in range(101):
                if adj[num][i] == 1 and not visited[i]:
                    queue.append((i,cnt+1)) # 👨🏻‍🏫 이런 스킬을 유형화해서 외우면 앞으로 좀 더 문제풀 때 좋을 것 같다.
                    visited[i] = 1

        return max_cnt, max_num

    max_cnt,max_num = bfs(start)
    print("#{} {}".format(tc,max_num))