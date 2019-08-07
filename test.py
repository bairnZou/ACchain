class qwe:
    _z = 1
    def __init__(self, a, b):
        self.gg = a
        self.hh = b


    
    
def main():
    a = 3
    b = 3
    c = [[] for _ in range(4)]
    print(c)
    for i in range(a):
        for j in range(b):
            c[i].append(qwe(i,j))
            print(c[i][j].gg)

if __name__ == '__main__':
    main()