
def kinds(n, m):
    f = [0 for i in range(n*m+1)]
    for _ in range(1, m+1):
        f[i] = 1
    for _ in range(n-1):
        for k in range(n*m, 0, -1):
            f[k] = 0
            for j in range(1, m+1):
                if k >= j:
                    f[k] += f[k-j]
    return f


if __name__ == "__main__":
    kx = kinds(9, 4)
    ky = kinds(6, 6)

    s = sum(kx) * sum(ky)
    r = 0

    for i in range(37):
        for j in range(i):
            r += kx[i] * ky[j]

    print(r/s)