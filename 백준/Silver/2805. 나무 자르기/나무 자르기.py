# 최소절단높이, 최대절단높이, 원하는 양, 리스트
def solution(s, e, target, lst):
    h = (s + e) // 2
    if s > e:
        return h

    get = 0
    for tree in trees:
        if tree > h:
            get += tree - h
    # 위로 올리기
    if get >= target:
        return solution(h+1, e, target, lst)
    # 더 자르기; 아래로
    elif get < target:
        return solution(s, h-1, target, lst)
        

N, M = map(int, input().split())
trees = list(map(int, input().split()))

# 가장 큰 나무의 값을 최댓값으로 함
max_tree = max(trees)
print(solution(0, max_tree, M, trees))
