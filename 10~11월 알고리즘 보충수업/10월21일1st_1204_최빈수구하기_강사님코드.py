T = int(input()) # 테스트 케이스의 수
for _ in range(T):
    tc = int(input()) # 테스트 케이스의 번호
    scores = list(map(int,input().split()))
    # 최빈수 구하기
    # 각 숫자가 얼마나 나왔는지 저장할 배열
    cnt = [0] * 101
    # scores 배열을 순회하면서 각 숫자들이 나올 때마다 cnt 배열의 수를 1 증가
    # 👨🏻‍🏫index에 익숙해지세요!!
    for i in range(len(scores)):
        cnt[scores[i]] += 1

    # cnt 배열을 순회하면서, 가장 큰 cnt를 가지는 인덱스를 저장
    # 👨🏻‍🏫max로 찾으면 금방 찾겠지만, index에 좀 더 적응해봅시다!!
    max_v = 0 # 최대값을 저장할 변수 (👨🏻‍🏫초기화할 때는 항상 정당한 이유가 있어야 한다!!)
    max_i = 0 # 최대값을 가지는 인덱스를 저장할 변수, 최빈수를 저장하게 된다.
    for i in range(len(cnt)):
        if max_v <= cnt[i]: # 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력
            max_v = cnt[i] # 최대값 저장
            max_i = i # 최대값 인덱스 저장

    print("#{} {}".format(tc,max_i))
    