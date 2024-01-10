AB = input()

# A + B
if len(AB) == 2:
    print(int(AB[0]) + int(AB[1]))
# 10 + 10
elif len(AB) == 4:
    print(20)
elif len(AB) == 3:
    if AB[1] == '0':
        # 10 + B
        print(10 + int(AB[-1]))
    else:
        # A + 10
        print(int(AB[0]) + 10)
