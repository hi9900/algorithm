def solution(participant, completion):
    partDict = dict()
    resultHash = 0
    
    for part in participant:
        partDict[hash(part)] = part
        resultHash += hash(part)
    
    for comp in completion:
        resultHash -= hash(comp)
        
    return partDict[resultHash]