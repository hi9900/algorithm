def solution(clothes):
    clothesType = {}
    
    for cloth, tp in clothes:
        if tp in clothesType:
            clothesType[tp] += 1
        else:
            clothesType[tp] = 2
    
    result = 1
    for v in clothesType.values():
        result *= v
        
    return result - 1
    
