import sys
input = sys.stdin.readline

n = int(input())
arr = []
# 입력
for i in range(n):
    x = input().strip()
    arr.append(x)

l = len(arr[0])
ans = ''
# i번째 자리의 문자가 모두 같으면 해당 문자 출력
# 하나라도 다르면, ?
for i in range(l):
    tmp = ''
    for a in arr:
        if tmp == '':
            tmp = a[i]
            continue

        if tmp != a[i]:
            ans += '?'
            break
    else:
        ans += arr[0][i]

print(ans)