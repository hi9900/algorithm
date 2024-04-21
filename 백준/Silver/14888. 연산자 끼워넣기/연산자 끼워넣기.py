import sys
input = sys.stdin.readline

def calc(x, y, c):
    if c == 0:
        return x + y
    if c == 1:
        return x - y
    if c == 2:
        return x * y
    if c == 3:
        if x >= 0:
            return x // y
        return -(-x // y)


def solve(i, result):
    global max_a, min_a, operator
    if i == N:
        max_a = max(max_a, result)
        min_a = min(min_a, result)
        return

    for x in range(4):
        if operator[x]:
            operator[x] -= 1
            solve(i+1, calc(result, arr[i], x))
            operator[x] += 1


N = int(input())
arr = list(map(int, input().split()))
operator = list(map(int, input().split()))

max_a, min_a = -10e9, 10e9

solve(1, arr[0])

print(max_a)
print(min_a)
