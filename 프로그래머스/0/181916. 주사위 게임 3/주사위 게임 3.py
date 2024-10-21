def solution(a, b, c, d):
    dice = list(set([a, b, c, d]))
    sum_dice = sum([a, b, c, d])

    if len(dice) == 1:
        return 1111 * a
    if len(dice) == 2:
        p, q = dice
        if (p + q) * 2 == sum_dice:
            return (p+q) * abs(p-q)
        if (a, b, c, d).count(p) == 3:
            return (10 * p + q) ** 2
        return (10 * q + p) ** 2
        
    if len(dice) == 3:
        p, q, r = dice
        if (a, b, c, d).count(p) == 2:
            return q * r
        elif (a, b, c, d).count(q) == 2:
            return p * r
        return p * q
    return min([a, b, c, d])