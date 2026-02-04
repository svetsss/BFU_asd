def numbers_3_5_7(x: int):
    out = []


    def dfs(n, i, k, l, m):
        if n > x:
            return
        out.append((n, k, l, m))
        if i <= 0: dfs(n * 3, 0, k + 1, l, m)
        if i <= 1: dfs(n * 5, 1, k, l + 1, m)
        if i <= 2: dfs(n * 7, 2, k, l, m + 1)


    dfs(1, 0, 0, 0, 0)
    for n, k, l, m in sorted(out):
        print(f"{str(n).rjust(len(str(x)))}  →  3^{k}  5^{l}  7^{m}")


x = int(input('Введите х:'))
numbers_3_5_7(x)
