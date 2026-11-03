def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    r_a = len(a)
    c_a = len(a[0])
    r_b = len(b)
    c_b = len(b[0])

    #check the dimensions of the matrix
    if c_a != r_b:
        return -1

    c = [[0 for _ in range(c_b)] for _ in range(r_a)]

    for i in range(r_a):
        for j in range(c_b):
            for k in range(c_a):
                c[i][j] += a[i][k] * b[k][j]


    return c