import sys
input = sys.stdin.readline

word = input().rstrip()
# word를 대문자로 변환
word = word.upper()

result = dict()
for i in word:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1

# 빈도수를 기준으로 정렬
result = sorted(result.items(), key=lambda x: x[1], reverse=True)

# 여러 개 확인
if len(result) > 1 and result[0][1] == result[1][1]:
    print('?')
else:
    print(result[0][0])
