
# 길이가 짧은 것부터
# 길이가 같다면 사전순
# 중복된 단어는 하나만 남기고 제거
word = set()

N = int(input())
for _ in range(N):
    word.add(input())

word = list(word)
word.sort(key=lambda x: (len(x), x))

print(*word, sep="\n")
