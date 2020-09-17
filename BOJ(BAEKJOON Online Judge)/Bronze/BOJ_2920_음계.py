# date: 2020/09/12
# author: psS2mj
# brief: BOJ_2920_음계

# 첫 번째 풀이방법
note = list(map(int, input().split()))

start = note[0]
check = True

if start == 1:
    for i in note:
        if start == i:
            start += 1
        else:
            check = False
            print("mixed")
            break
    if check:
        print("ascending")
elif start == 8:
    for i in note:
        if start == i:
            start -= 1
        else:
            check = False
            print("mixed")
            break
    if check:
        print("descending")
else:
    print("mixed")

# 두 번째 풀이방법
note = input()
print("ascending" if note == "1 2 3 4 5 6 7 8"
        else "descending" if note == "8 7 6 5 4 3 2 1" else "mixed")

# 세 번째 풀이방법
note = {"12345678":"ascending", "87654321":"descending"}
print(note.get(input()[::2], "mixed"))

# 네 번째 풀이방법
print({"12345678":"ascending", "87654321":"descending"}.get(input()[::2], "mixed"))