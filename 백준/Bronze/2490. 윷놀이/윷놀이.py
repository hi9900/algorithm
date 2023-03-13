for _ in range(3):
    data = list(input())
    bea = data.count("0")
    if bea == 1:
        print("A")
    elif bea == 2:
        print("B")
    elif bea == 3:
        print("C")
    elif bea == 4:
        print("D")
    else:
        print("E")