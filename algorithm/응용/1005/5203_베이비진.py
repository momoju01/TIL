# 베이비 진 >> run또는 triplet 확인
# run과 triplet 검사를 많이 해야 하기 때문에
# 검사 코드를 별도 함수로 작성
def check_run_triplet(arr):
    """
    :return: run이거나, triplet 이면,  1반환하기 아니면 0반환
    내가 가진 카드 덱의 순열을 이용한 run/triplet 확인이 아니라...
    각 카드를 몇장 가지고 있는가? 하는 배열을 이용한 확인
    arr : 1~9까지의 카드가 각 몇장씩 있는가 저장하는 배열
    """
    for x in range(len(arr)):
        # 트리플 판별
        if arr[x] == 3:
            return 1
        # run 판별
        # if arr[x] >= 1 and arr[x + 1] >= 1 and arr[x + 2] >= 1:
        #     return 1  >이렇게 했더니 인덱스 에러남

        # x < len(arr) - 2  : 8이나 9번 인덱스에서 검사x
        if x < len(arr)-2 and arr[x] and arr[x+1] and arr[x+2]:
            return 1
    return 0



T = int(input())
for tc in range(1,T+1):
    numbers = list(map(int,input().split()))
    # 각 플레이어가.... 돌아가면서 한 장씩 카드를 뽑기
    # 카드를 뽑을 때 마다 카드 덱이 run/ triplet인지 확인하기

    # 카드덱에서 한장씩 확인하면서, winner가 나오면 winner를 바꿔주면 됩니다.
    winner = 0  # 비기면, 0이니까. 0으로 초기화
    p1 = [0]*10
    p2 = [0]*10

    for i in range(0, 12, 2):
        #카드 뽑으면서 승자가 나왔는지 확인
        #i 번째 카드가 p1의 카드 >> p1의 카드덱을 만들고
        p1[numbers[i]] += 1
        #check_run_triplet(p1의 카드덱)
        if check_run_triplet(p1):
            winner = 1
            break
        #i + 1 번째 카드가 p2의 카드 >> p2가 카드덱을 만들기
        p2[numbers[i+1]] += 1
        # check_run_triplet(p2의 카드덱)

        if check_run_triplet(p2):
            winner = 2
            break

    print('#{} {}'.format(tc, winner))