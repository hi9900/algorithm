def solve(n, i, _result):
    global result
    if i >= 4:
        return

    if len(_result) == n:
        result.add(str(sum(_result)))
        return

    solve(n, i, _result + [rome[i]])
    solve(n, i+1, _result)


N = int(input())
rome = [1, 5, 10, 50]
result = set()

solve(N, 0, [])
print(len(result))