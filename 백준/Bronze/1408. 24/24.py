import sys
input = sys.stdin.readline

now = list(map(int, input().split(':')))
start = list(map(int, input().split(':')))
# end
start[0] += 24

# start - now
answer = [0] * 3
for i in range(3):
    answer[i] = start[i] - now[i]

result = ''
for i in range(2, -1, -1):
    if i != 0 and answer[i] < 0:
        answer[i-1] -= 1
        answer[i] += 60
    if i == 0 and answer[i] >= 24:
        answer[i] -= 24

for i in answer:
    result += f':{i:02d}'
print(result[1:])