# babygin 탐욕알고리즘으로 풀기

greed = [0]*10 # 0~9
tri=0
run =0
arr = list(map(int, input()))
ans = "Lose"

# greed에 숫자 개수 count
for i in arr:
    greed[i] += 1

for x in range(10):
    # 트리플 판별
    if greed[x]>=3:
        greed[x]-=3
        tri+=1
    # run 판별
    if greed[x]>=1 and greed[x+1]>=1 and greed[x+2]>=1:
        greed[x] -=1
        greed[x+1] -=1
        greed[x+2] -=1
        run+=1
    if tri + run == 2:
        ans = "Baby-Gin"
        break

print(ans)


