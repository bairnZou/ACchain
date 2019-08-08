import sys
import random as rd
import ds
#import numpy as np


def main():
    argvs = sys.argv
    if len(argvs) < 6:
        sys.exit(0)

    N = int(sys.argv[1])
    NumofV = int(sys.argv[2])
    m = int(sys.argv[3])
    TPS = int(sys.argv[4])
    T = int(sys.argv[5]) 
    
    nodes = ds.Node(N, NumofV)
    #print(nodes.nodes[1][0].owner)

    time = 0
    check_point = 0
    trade_index = 0

    while True:
        for i in range(TPS):
            trade_num = rd.sample(range(N),2)
            ds.Trade(nodes[trade_num[0]],nodes[trade_num[1]],trade_index)
            


        
    

if __name__ == '__main__':
    main()