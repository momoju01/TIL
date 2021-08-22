T = int(input())  # 테스트 케이스 개수

for tc in range(1, T + 1):
    N = int(input())  # 상자 개수
    sq = [[0] * 10 for _ in range(10)]  # 전체 칸
    purple = 0  # 보라색 칸 수

    # 각 상자별로 칸에 색 칠하기
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for x in range(r1, r2 + 1):
            for y in range(c1, c2 + 1):
                sq[x][y] += color  # 입력받은 영역에 color 칠해주기
                if sq[x][y] == 3:  # 같은 색인 영역은 겹치지 않음으로 3인 부분은 보라색
                    purple += 1

    print(f'#{tc} {purple}')