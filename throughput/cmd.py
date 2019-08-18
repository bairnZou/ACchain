import sys
import random as rd
import ds2
import os


def main():
    argvs = sys.argv
    if len(argvs) < 4:
        sys.exit(0)
    N = int(sys.argv[1])
    NumofV = int(sys.argv[2])
    #m = int(sys.argv[3])
    TPS = int(sys.argv[3])
    #T = int(sys.argv[5])
    #Rotation = int(sys.argv[6])
     
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
            
        with open('./BCOT.txt', 'a') as f:
                f.write(' '.join(str(BCOT_)))
                f.write('\n')
        
        TPS -= 1
    
    with open('./TBCPT.txt', 'a') as f:
        for i in TXS:
            tmp = i.count
            #print(len(TXS))
            f.write(str(tmp))
            f.write('\n')
if __name__ == '__main__':
    main()