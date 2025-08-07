import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))
m.sort()

ans = 1

for w in m:
    if w > ans:
        break
    ans += w
    
print(ans)
