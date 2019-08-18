import sys
import random as rd
import ds2
import os
import numpy as np
from functools import reduce
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

    T_ac = []
    S_a,S_cc,S_txn = 1,1,1      #参数

    nodes_ = ds2.Node(N, NumofV)
    nodes_.changeS(S_txn)

    time_ac = 0
    SS_a,SS_c = 0,0
    
    #print(nodes.nodes[1][0].owner)
    TXS = []
    nodes_C = [{} for i in range(N)]
    #BCOT = 0
    T_ac = list(map(lambda x: x*Rotation, sorted(list(np.random.normal(0, 1, Rotation)))))

    while T_ac[-1] < Rotation:
        T_ac = list(map(lambda x: x*Rotation, sorted(list(np.random.normal(0, 1, Rotation)))))

    index_ac = 0
    node_ac = [0] * N

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

    if not os.path.exists('./ssa.txt'):
        os.mknod('./ssa.txt')
    f=open('./ssa.txt', "r+")
    f.truncate()
    f.close()

    if not os.path.exists('./ssc.txt'):
        os.mknod('./ssc.txt')
    f=open('./ssc.txt', "r+")
    f.truncate()
    f.close()

    if not os.path.exists('./nodeS.txt'):
        os.mknod('./nodeS.txt')
    f=open('./nodeS.txt', "r+")
    f.truncate()
    f.close()

    while Rotation:
        for _ in range(TPS):
            trade_num = rd.sample(range(N), 2)
            trade_flag = True
            node_ac[trade_num[0]] = 1
            trade_flag = ds2.Trade(nodes_.nodes[trade_num[0]],nodes_.nodes[trade_num[1]],trade_index,TXS,BCOT_, nodes_C,trade_num[0],trade_num[1],nodes_,S_txn)
            #print(trade_num)
            #print(nodes_.nodes[trade_num[1]][-1].proof)
            #print(trade_flag)
            if trade_flag:
                trade_index += 1
            
            time += 1
            time_ac += 1

        if time_ac > T_ac[index_ac]:

            tmpSum = reduce(lambda x,y:x+y,node_ac)
            SS_a = S_a * tmpSum
            index_ac += 1
            time_ac = 0
            node_ac = [0] * N

        if time >= T:
            
            SS_c += S_cc
            time = 0
            print('aaa')
            
            for i in range(len(nodes_.nodes)):
                for j in nodes_.nodes[i]:
                    for t in j.proof:
                        if t not in j.ownproof:
                            if nodes_C[i][t]:
                                nodes_C[i][t] -= 1

                for value in nodes_.nodes[i]:
                    value.proof.clear()
                    value.proof = value.ownproof[:]
            
            for _ in range(len(TXS)-check_point):
                #print('bbb')
                _ = _ + check_point
                TXS[_].count += m
                TXS[_].becounted = True
                if TXS[_].proof:
                    #print('ccc')
                    print(TXS[_].proof)
                    for t in TXS[_].proof:
                        #print('yyy')
                        if TXS[t] and TXS[t].becounted is False:
                            #print('xxx')
                            TXS[t].count += m
                            #print(TXS[_].proof[t])
                            TXS[t].becounted = True
            
            for _ in range(len(TXS)-check_point):
                _ = _ + check_point
                #print(_)
                TXS[_].becounted = False
                if TXS[_].proof:
                    for t in TXS[_].proof:
                        
                        TXS[t].becounted = False
            
            check_point = len(TXS)
            Rotation -= 1
            #print(BCOT_)
            
            with open('./BCOT.txt', 'a') as f:
                f.write(' '.join(str(BCOT_)))
                f.write('\n')

    print(SS_a,SS_c)
    with open('./TBCPT.txt', 'a') as f:
        for i in TXS:
            tmp = i.count
            #print(len(TXS))
            f.write(str(tmp))
            f.write('\t')
    with open('./ssa.txt', 'a') as f:
        f.write(str(SS_a))
        f.write('\n')
        
    with open('./ssc.txt', 'a') as f:
        f.write(str(SS_c))
        f.write('\n')
    
    with open('./nodeS.txt', 'a') as f:
        f.write(' '.join(str(nodes_.S)))
        f.write('\n')

if __name__ == '__main__':
    main()