def solution(arr, queries):
    for query in queries:
        a, b = query
        arr[a], arr[b] = arr[b], arr[a]
    
    return arr