import sys
import random as rd
import ds
import os
#import numpy as np


def main():
    argvs = sys.argv
    if len(argvs) < 7:
        sys.exit(0)

    N = int(sys.argv[1])
    NumofV = int(sys.argv[2])
    m = int(sys.argv[3])
    TPS = int(sys.argv[4])
    T = int(sys.argv[5])
    Rotation = int(sys.argv[6])
    
    nodes_ = ds.Node(N, NumofV)
    #print(nodes.nodes[1][0].owner)
    TXS = []
    #BCOT = 0

    time = 0
    check_point = 0
    trade_index = 0
    BCOT_ = []
    
    if not os.path.exists('./BCOT.txt'):
        os.mknod('./BCOT.txt')
    f=open('./BCOT.txt', "r+")
    f.truncate()
    f.close()

    if not os.path.exists('./TBCPT.txt'):
        os.mknod('./TBCPT.txt')
    f=open('./TBCPT.txt', "r+")
    f.truncate()
    f.close()

    while Rotation:
        for _ in range(TPS):
            trade_num = rd.sample(range(N),2)
            trade_flag = True
            
            trade_flag = ds.Trade(nodes_.nodes[trade_num[0]],nodes_.nodes[trade_num[1]],trade_index,TXS,BCOT_)
            #print(trade_num)
            #print(nodes_.nodes[trade_num[1]][-1].proof)
            #print(trade_flag)
            if trade_flag:
                trade_index += 1
            
            time += 1
            
        if time >= T:

            time = 0
            print('aaa')
            for i in range(len(nodes_.nodes)):
                for value in nodes_.nodes[i]:
                    value.proof.clear()
                    value.proof = value.ownproof[:]
                    
            
            for _ in range(len(TXS)-check_point):
                #print('bbb')
                _ = _ + check_point
                TXS[_].count += m
                TXS[_].becounted = True
                if TXS[_].proof:
                    print('ccc')
                    for t in TXS[_].proof:
                        print('yyy')
                        if TXS[TXS[_].proof[t]] and TXS[TXS[_].proof[t]].becounted is False:
                            print('xxx')
                            TXS[TXS[_].proof[t]].count += m
                            #print(TXS[_].proof[t])
                            TXS[TXS[_].proof[t]].becounted = True
            
            for _ in range(len(TXS)-check_point):
                _ = _ + check_point
                #print(_)
                TXS[_].becounted = False
                if TXS[_].proof:
                    for t in TXS[_].proof:
                        
                        TXS[TXS[_].proof[t]].becounted = False
            
            check_point = len(TXS)
            Rotation -= 1
            #print(BCOT_)
            with open('./BCOT.txt', 'a') as f:
                f.write(' '.join(str(BCOT_)))
                f.write('\n')

    with open('./TBCPT.txt', 'a') as f:
        for i in TXS:
            tmp = i.count
            #print(len(TXS))
            f.write(str(tmp))
            f.write('\t')

if __name__ == '__main__':
    main()