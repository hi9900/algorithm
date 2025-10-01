from collections import Counter

def solution(participant, completion):
    part_count = Counter(participant)
    comp_count = Counter(completion)
    
    diff = part_count - comp_count
    
    return list(diff.keys())[0]