class txn:
        proof_value = 0
        count = 0
        becounted = False

        def __init__(self, index):
            self.proof_value = index


#class TXN:

 #   def __init__(slef, N):
  #      slef.txn = 


class value:
        owner = 0
        proof = []
        ownproof = []

        def __init__(self, ori_node):
            self.owner = ori_node

        def change_own(self, new_node):
            self.owner = new_node

        def add_proof(self, newproof):
            self.proof.append(newproof)
    
        def add_ownproof(self,newproof):
            self.ownproof.append(newproof)
        
        def change_ownproof(self,newproof):
            self.ownproof.


class Node:

    def __init__(self, N, M):
        nodes = [[] for _ in range(N)]
        for i in range(N):
            for j in range(M):
                self.nodes[i].append(value(i))
    
    def trade(self, i, j, k):
        for _ in self.nodes[i]:
            
