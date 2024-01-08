L = int(input())

# 숙제
A = int(input())
B = int(input())

# 하루 최대
C = int(input())
D = int(input())

x, y = divmod(A, C)
x1, y1 = divmod(B, D)

if y > 0:
    x += 1
if y1 > 0:
    x1 += 1

print(L - max(x, x1))
