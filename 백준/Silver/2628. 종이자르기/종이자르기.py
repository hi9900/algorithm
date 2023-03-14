import sys
input = sys.stdin.readline

pb, ph = map(int, input().split())
N = int(input())
bb = [0, pb]
hh = [0, ph]

for _ in range(N):
    a, dot = map(int, input().split())
    if a == 0:
        hh.append(dot)
    else:
        bb.append(dot)

bb.sort()
hh.sort()
max_arr = 0
for i in range(1, len(bb)):
    for j in range(1, len(hh)):
        arr = (bb[i]-bb[i-1]) * (hh[j] - hh[j-1])
        if arr > max_arr:
            max_arr = arr
            
print(max_arr)