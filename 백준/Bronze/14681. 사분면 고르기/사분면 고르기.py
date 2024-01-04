import sys
input = sys.stdin.readline

x = int(input())
y = int(input())

# ++ 1
# +- 4
# -+ 2
# -- 3

if x*y > 0: 
    if x > 0:
        print(1)
    elif x < 0:
        print(3)
else:
    if x > 0:
        print(4)
    elif x < 0:
        print(2)