def solution(num_list):
    A, B = '', ''
    for n in num_list:
        if n % 2:
            A += str(n)
        else:
            B += str(n)
    
    return int(A)+int(B)