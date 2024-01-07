word = input()
# A ~ Z = 65 ~ 90
# a ~ z = 97 ~ 122
# 차이는 32

for w in word:
    # 90보다 작으면 대문자 -> + 32
    if ord(w) <= 90:
        print(chr(ord(w) + 32), end="")
    # 97보다 크면 소문자 -> -32
    else:
        print(chr(ord(w) - 32), end="")