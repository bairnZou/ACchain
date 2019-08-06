class txn:
    def __init__(self):
        self.proof = []
        self.count = 0
        self.becounted = 0


class value:

    def __init__(self, ori_node):
        self.owner = ori_node
        self.proof = []
        self.ownproof = []

    def change_own(self, new_node):
        self.owner = new_node

    def add_proof(self, newproof):
        self.proof.append(newproof)
