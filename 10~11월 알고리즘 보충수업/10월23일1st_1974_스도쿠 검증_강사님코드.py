# 👨🏻‍🏫행 우선순회, 열 우선순회 둘 다 할 줄 알아야합니다.

# import sys
# sys.stdin = open("스도쿠.txt","r") # 파일 읽어오기

# 함수 정의해보기
# 👨🏻‍🏫짧게 쓰는 것보다 풀어서, 내가 이해하기 쉽게 작성하는 것이 가장 중요하다.
# 👨🏻‍🏫짧게 쓰는 것은 익숙해 진 후에 나중에 연구해보기. 풀어서 쓰는 것이 가장 쉽다.

def check_sudoku(): # 스도쿠라면 True, 아니라면 False 반환
    # 행이 모두 1~ 9까지로 구성되어 있는지 검사
    for i in range(9):
        check = [0] * 10  # 1~9까지의 수가 나왔는지 확인하는 배열
        for j in range(9):
            if check[sudoku[i][j]] == 0:
                check[sudoku[i][j]] = 1
            else:
                return False
    # 열이 모두 1~ 9까지로 구성되어 있는지 검사
    for i in range(9):
        check = [0] * 10  # 1~9까지의 수가 나왔는지 확인하는 배열
        for j in range(9):
            if check[sudoku[j][i]] == 0:
                check[sudoku[j][i]] = 1
            else:
                return False

    # 3*3 부분행렬이 1~9까지로 구성되어 있는지 검사
    for i in range(3):
        for j in range(3):
            #3*3행렬 순회
            check = [0] * 10  # 1~9까지의 수가 나왔는지 확인하는 배열
            for a in range(i*3,i*3+3):
                for b in range(j*3,j*3+3):
                    if check[sudoku[a][b]] == 0:
                        check[sudoku[a][b]] = 1
                    else:
                        return False

    return True

T = int(input())
for tc in range(1,T+1):
    sudoku = [list(map(int,input().split())) for _ in range(9)] # 이차원배열 입력 받기
    if check_sudoku(): # 함수의 반환값이 True일 때
        print("#{} 1".format(tc))
    else:
        print("#{} 0".format(tc))

# 잘 저장되었는지 출력해보기
    # for row in sudoku:
    #     print(*row) >>> unpacking
    #     print(row)