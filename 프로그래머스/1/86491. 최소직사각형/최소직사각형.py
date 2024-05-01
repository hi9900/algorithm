def solution(sizes):
    max_x, max_y = 0, 0
    for size_x, size_y in sizes:
        max_x = max(max_x, max(size_x, size_y))
        max_y = max(max_y, min(size_x, size_y))
        
    return max_x * max_y