class txn:
    def __init__(self, index):
        self.proof_value = index
        self.count = 0
        self.becounted = 0


class TXN:
    def __init__(slef, N):
        slef.txn = 



class value:

    def __init__(self, ori_node):
        self.owner = ori_node
        self.proof = []
        self.ownproof = []

    def change_own(self, new_node):
        self.owner = new_node

    def add_proof(self, newproof):
        self.proof.append(newproof)

class Node:

    def __init__(self,N,M):
        self.node = 