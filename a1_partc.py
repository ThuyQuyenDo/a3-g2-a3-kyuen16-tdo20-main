from a1_partb import SetList

class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.num_sets = 0
    
    def make_set(self, element):
        if element in self.parent:
            return False
        self.parent[element] = {'parent': element, 'size': 1} # initialize size to 1
        self.num_sets += 1
        return True

    def find_set(self, element):
        if element not in self.parent:
            return None
        if self.parent[element]['parent'] == element:
            return element
        self.parent[element]['parent'] = self.find_set(self.parent[element]['parent'])
        return self.parent[element]['parent']

    def union_set(self, element1, element2):
        root1 = self.find_set(element1)
        root2 = self.find_set(element2)
        if root1 is None or root2 is None or root1 == root2:
            return False
        if self.parent[root1]['size'] < self.parent[root2]['size']:
            root1, root2 = root2, root1
        self.parent[root2]['parent'] = root1
        self.parent[root1]['size'] += self.parent[root2]['size']
        self.num_sets -= 1
        return True
        
    def get_set_size(self, element):
        root = self.find_set(element)
        if root is None:
            return 0
        return self.parent[root]['size']
    
    def get_num_sets(self):
        return self.num_sets
    
    def __len__(self):
        count = 0
        for i in self.parent:
            count += 1
        return count
