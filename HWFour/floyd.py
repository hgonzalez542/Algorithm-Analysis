# floyd.py

INF = 10000  # Representing infinity

# Initial weight matrix W = D(0)
D = [
    [0,     1,    INF,   1,     5],
    [9,     0,    3,     2,     INF],
    [INF,   INF,  0,     4,     INF],
    [INF,   INF,  2,     0,     3],
    [3,     INF,  INF,   INF,   0]
]

def print_matrix(D, k):
    print(f"\nD({k}):")
    for row in D:
        print(["∞" if x >= INF else x for x in row])

def floyd(D):
    n = len(D)
    print_matrix(D, 0)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
        print_matrix(D, k + 1)

# Run Floyd's algorithm
floyd(D)
