word = input()
N = len(word)
for i in range(N // 10 + 1):
    print(word[i*10:i*10+10])