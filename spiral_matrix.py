inp = input().strip().split(sep=' ')

n_ = int(inp[0])
m_ = int(inp[1])

tmp_matr = []

for i in range(n_):
    tmp_str = []
    for j in range(m_):
        tmp_str.append(0)
    tmp_matr.append(tmp_str)

n_i = 0
n_j = 1
tmp_i = 0
tmp_j = 0

for k in range(n_*m_):
    tmp_matr[tmp_i][tmp_j] = k+1
    if n_j == 1 and n_i == 0:
        if tmp_j + n_j == m_:
            n_i = 1
            n_j = 0
        elif tmp_matr[tmp_i][tmp_j + n_j] != 0:
            n_i = 1
            n_j = 0
    elif n_j == -1 and n_i == 0:
        if tmp_j + n_j < 0:
            n_i = -1
            n_j = 0
        elif tmp_matr[tmp_i][tmp_j + n_j] != 0:
            n_i = -1
            n_j = 0
    elif n_i == 1 and n_j == 0:
        if tmp_i + n_i == n_:
            n_i = 0
            n_j = -1
        elif tmp_matr[tmp_i + n_i][tmp_j] != 0:
            n_i = 0
            n_j = -1

    elif n_i == -1 and n_j == 0:
        if tmp_i + n_i == 0:
            n_i = 0
            n_j = 1
        elif tmp_matr[tmp_i + n_i][tmp_j] != 0:
            n_i = 0
            n_j = 1

    tmp_i += n_i
    tmp_j += n_j




for i in range(n_):
    print(' '.join([str(num) for num in tmp_matr[i]]))