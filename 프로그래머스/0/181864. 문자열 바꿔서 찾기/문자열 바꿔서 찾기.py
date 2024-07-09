def solution(myString, pat):
    newString = ""
    for s in myString:
        if s == "A":
            newString += "B"
        else:
            newString += "A"
            
    return 1 if pat in newString else 0