# 데이터를 어떻게 넣을지?
# hint : 양쪽 두개 중에 제일 큰 것과 본인의 차이

import sys
sys.stdin = open("input1206.txt", "r")

TC = 10
for tc in range(TC):
    N = int(input())
    lst = list(map(int, input().split())

    result = 0

    # for i in range() :
    
    # i번째의 조망권 수는 :
    # t = build[i-2] build[i-1] build[i+1] build[i+2] 중에 제일 큰 값
    # i_result = build[i] - t

    print('#{} {}'.format(tc+1, result))

