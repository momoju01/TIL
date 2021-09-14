T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    res = 'NO'
    for i in range(N-5+1):
        for j in range(N-5+1):
            cnt3 = 0         # 우하향
            cnt4 = 0         # 우상향
            for k in range(5):
                cnt1 = 0     # 행
                cnt2 = 0     # 열
                for l in range(5):
                    if arr[i+k][j+l] == 'o':
                        cnt1 += 1
                    if arr[i+l][j+k] == 'o':
                        cnt2 += 1
                # 5개만 도니까 for 문 끝나고 조건 맞는지 검사해도 됨
                if cnt1 == 5 or cnt2 == 5:
                    res = 'YES'
                    break
                # 대각선 검사
                if arr[i + k][j + k] == 'o':
                    cnt3 += 1
                if arr[i+k][(5-1)+j-k] == 'o':
                    cnt4 += 1
            # k가 for 문 다 돌면 조건 확인
            if cnt3 == 5 or cnt4 == 5:
                res = 'YES'
                break
        if res == 'YES':
            break

    print(f'#{tc} {res}')