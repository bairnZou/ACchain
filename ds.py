import random as rd

class txn:
        
        proof = []
        proof_value = 0
        count = 0
        becounted = False

        def __init__(self, index):
            self.proof_value = index


#class TXN:

#    def __init__(slef, N):
#       slef.txn = 


class value:

        #owner = 0
        proof = []
        ownproof = []

        #def __init__(self, ori_node):
         #   self.owner = ori_node

        def change_own(self, new_node):
            self.owner = new_node

        def add_proof(self, newproof):
            self.proof.append(newproof)
    
        def add_ownproof(self,newproof):
            self.ownproof.append(newproof)
        
        #def change_ownproof(self,newproof):
         #   self.ownproof.


class Node:

    nodes = []

    def __init__(self, N, M):
        self.nodes = [[] for _ in range(N)]
        for i in range(N):
            #for j in range(M):
            #    self.nodes[i].append(value())
            self.nodes[i] = [value()] * M
    #def trade(self, i, j, k):
     #   for _ in self.nodes[i]:
            
def Trade(node_a, node_b, trade_index, TXS):

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
    node_b[-1].ownproof.clear()
    node_b[-1].ownproof.append(trade_index)

    if len(node_a[choice].proof) == len(node_a[choice].ownproof):
        tx_this.proof = node_a[choice].proof[:]
    
    TXS.append(tx_this)
    BCOT = 0
    
    for _ in node_b[-1].proof:
        TXS[_].count += 2
        BCOT += 2

    with open('BCOT.txt','w') as f:
        f.wirte(BCOT+'\t')

    del node_a[choice]
    
    



