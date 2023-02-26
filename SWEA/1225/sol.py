import sys
sys.stdin = open("input.txt")

T = 10
for _ in range(1, T+1):
    tc = int(input())
    data = list(map(int, input().split()))
    num = 0
    # %8; 0 1 2 3 4 5 6 7
    while 0 not in data:
        for i in range(1, 6):
            data[num] -= i
            if data[num] <= 0:
                data[num] = 0
                end = num
                break
            num += 1
            num %= 8

    result = data[end+1:]+data[:end+1]
    print(f"#{tc}", *result)
