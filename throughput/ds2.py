import random as rd

class txn:
        
        proof = []
        proof_value = 0
        count = 0
        becounted = False

        def __init__(self, index):
            self.proof_value = index
            self.proof = p[]
            self.count = 0
            self.becounted = False

class value:

        #owner = 0
        proof = []
        #ownproof = []

        #def __init__(self, ori_node):
         #   self.owner = ori_node
        def __init__(self):
            self.proof = []

        def change_own(self, new_node):
            self.owner = new_node

        def add_proof(self, newproof):
            self.proof.append(newproof)
    
        #def add_ownproof(self,newproof):
        #    self.ownproof.append(newproof)


class Node:

    nodes = []

    def __init__(self, N, M):
        self.N = N
        self.nodes = [[] for _ in range(N)]
        for i in range(N):
            #for j in range(M):
            #    self.nodes[i].append(value())
            self.nodes[i] = [value([i,j]) for j in range(M)]
        self.S = []


def Trade(node_a, node_b, trade_index, TXS, BCOT_):

    if len(node_a) == 0:
        return False

    tx_this = txn(trade_index)
    max_temp = 0
    temp_index = []

    for _ in range(len(node_a)):
        if len(node_a[_].proof) == max_temp:
            temp_index.append(_)
        elif len(node_a[_].proof) > max_temp:
            max_temp = len(node_a[_].proof)
            temp_index.clear()
            temp_index.append(_)

    choice = rd.choice(temp_index)
    node_b.append(node_a[choice])
    node_b[-1].proof.append(trade_index)
    #print(node_b[-1].proof,'x')
    #node_b[-1].ownproof.clear()
    #node_b[-1].ownproof.append(trade_index)

    #if len(node_a[choice].proof) == len(node_a[choice].ownproof):
    #    tx_this.proof = node_a[choice].proof[:]
        #print('eee')

    TXS.append(tx_this)
    #print(len(node_b))
    BCOT = 0

    for _ in node_b[-1].proof:
        TXS[_].count += 1
        BCOT += 1
    #print(BCOT)
    print(len(TXS))
    BCOT_.append(BCOT)
    #with open('./BCOT.txt','w') as f:
    #    f.write(str(BCOT)+'\t')

    del node_a[choice]
    def update(value):
        value.proof.append(trade_index)
    map(update,node_a)
    return True