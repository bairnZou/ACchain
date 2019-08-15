import sys
import random as rd
import ds2
import os


def main():
    argvs = sys.argv
    if len(argvs) < 4:
        sys.exit(0)
    print('1')
    N = int(sys.argv[1])
    NumofV = int(sys.argv[2])
    #m = int(sys.argv[3])
    TPS = int(sys.argv[3])
    #T = int(sys.argv[5])
    #Rotation = int(sys.argv[6])

    nodes_ = ds2.Node(N, NumofV)
    TXS = []
    trade_index = 0
    BCOT_ = []

    while TPS:
        trade_num = rd.sample(range(N),2)
        trade_flag = True
        trade_flag = ds2.Trade(nodes_.nodes[trade_num[0]],nodes_.nodes[trade_num[1]],trade_index,TXS,BCOT_)
        if trade_flag:
            trade_index += 1
        print(BCOT_)


if __name__ == '__main__':
    main()