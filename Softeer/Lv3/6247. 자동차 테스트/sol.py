import sys
input = sys.stdin.readline

def find(a, target, start, end):
    if start > end:
        return -1
        
    mid = (start + end) // 2
    if a[mid] == target:
        return mid

    if a[mid] > target:
        return find(a, target, start, mid-1)
    elif a[mid] < target:
        return find(a, target, mid+1, end)

n, q = map(int, input().split())
cars = list(map(int, input().split()))
cars.sort()
for _ in range(q):
    m = int(input())
    # 3개의 자동차를 골랐을 때 중앙값이 m이 나오는 가짓수
    # m보다 작은 차, m, m보다 큰 차
    
    # 이분 탐색으로 index 찾기
    i = find(cars, m, 0, n-1)

    if i == -1:
        print(0)
    else:
        print(i * (n-i-1))
