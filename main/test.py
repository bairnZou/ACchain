class A:
    A = 0
    B = 0
    C = []
    def __init__(self, a, b):
        self.A = a
        self.B = b

def main():
    a = [[] for i in range(10)]
    for i in range(10):
            a[i] = [A(i,j) for j in range(10)]
    for i in range(10):
        for j in range(10):
            a[i][j].C = [i,j]
    print(a[3][3].C)
    print(a[4][4].C)


if __name__ == '__main__':
    main()