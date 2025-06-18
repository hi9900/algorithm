import sys
input = sys.stdin.readline

N, game = input().strip().split(" ")

arr = set()
for _ in range(int(N)):
    arr.add(input().strip())
count = len(arr)
if game == "Y":
    print(count)
elif game == "F":
    print(count // 2)
elif game == "O":
    print(count // 3)
