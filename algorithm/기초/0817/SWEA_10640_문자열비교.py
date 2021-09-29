# # 문자열
# # 리스트로 받을 필요 없이 in 쓰기
#
# T = int(input())
# for tc in range(1, T+1):
#     word = input()
#     text = input()
#     count = 0
#
#     if word in text:
#         count = 1
#
#     print(f'#{tc} {count}')
#

# 고지식한 ~

T = int(input())
for tc in range(1, T+1):
    word = input()
    text = input()
    count = 0

    for i in range(len(text)-len(word)+1):  # i 는 word의 길이만큼은 실행 안 해도 됨
        for j in range(len(word)):
            # 불일치
            if word[j] != text[i+j]:  # text 인덱스에 j 더하는 거 잊지 말기...
                break  # i+1
        # 인덱스 j의 원소 다 일치해야 else 실행됨
        else:
            count = 1

    print(f'#{tc} {count}')