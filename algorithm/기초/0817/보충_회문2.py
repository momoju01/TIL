import sys

sys.stdin = open("input4861.txt", "r")

T = int(input())


def check(s):
    #  s가 회문이면 True return
    #  아니면 False
    st = 0
    ed = len(s) - 1

    while st < ed and s[st] == s[ed]:
        st += 1
        ed -= 1
    if st >= ed:
        return True
    return False


def arrcheck():
    # 회문을 찾아서 return 한다  =>
    # # 가로 확인
    # for row in range(N):
    #     for st in range(N-M-1):
    #         result = check(arr[row][st:st + M])
    #         if result:
    #             return arr[row][st:st + M]
    # #세로 확인
    # for col in range(N):
    #     for st in range(N-M-1):
    #         temp_str = ''
    #         for k in range(st, st+M):
    #             temp_str += arr[k][col]
    #         result = check(temp_str)
    #         if result:
    #             return temp_str
    # 가로 확인
    for i in range(N):
        for st in range(N - M - 1):
            result = check(arr[i][st:st + M])
            if result:
                return arr[i][st:st + M]
            # 세로 확인
            temp_str = ''
            for k in range(st, st + M):
                temp_str += arr[k][i]
            result = check(temp_str)
            if result:
                return temp_str

TC = int(input())

for tc in range(1, T + 1):
    N0 = int(input())
    N = 100
    arr = [input() for _ in range(N)]


    for

