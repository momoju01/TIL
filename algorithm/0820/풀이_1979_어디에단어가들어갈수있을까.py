T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())  # N * N 행렬, K: 찾을 단어 길이

    puzzle = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for i in range(N):
        # 행 검사
        cnt_r = 0  # 행에서 칸 세기
        for j in range(N):
            if puzzle[i][j] == 1:  # if white
                cnt_r += 1
            else:
                # wall
                if cnt_r == K:
                    ans += 1
                cnt_r = 0  # reset cnt_r as 0

        # 끝까지 가서야 완성이 된 경우 위의 else 에 못 들어가므로 아래에서 ans+1 해야함
        if cnt_r == K:
            ans += 1

        # 열을 검사
        cnt_c = 0
        for j in range(N):
            if puzzle[j][i] == 1:  # 열을 먼저 보겠다.
                cnt_c += 1
            else:
                if cnt_c == K:
                    ans += 1
                cnt_c = 0
        if cnt_c == K:
            ans += 1


    print(f'#{tc} {ans}')
########################################################################
#
# # 띠 두르는 경우
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#
#     puzzle = [list(map(int, input().split())) + [0] for _ in range(N)]
#     puzzle.append([0]*(N+1))
#     ans = 0
#
#     for i in range(N):
#         # 행 검사
#         cnt_r = 0
#         for j in range(N):
#             if puzzle[i][j] == 1:  # if white
#                 cnt_r += 1
#             else:
#                 # wall
#                 if cnt_r == K:
#                     ans += 1
#                 cnt_r = 0  # reset cnt_r as 0
#         # 삭제
#         # # 끝까지 가서야 완성이 된 경우
#         # if cnt_r == K:
#         #     ans += 1
#
#         # 열을 검사
#         cnt_c = 0
#         for j in range(N):
#             if puzzle[j][i] == 1:  # 열을 먼저 보겠다.
#                 cnt_c += 1
#             else:
#                 if cnt_c == K:
#                     ans += 1
#                 cnt_c = 0
#         # 삭제!
#         # if cnt_c == K:
#         #     ans += 1
#
#
#     print(f'#{tc} {ans}')