class Node:
    def __init__(self, data=None, next_node=None, previous_node=None, set_list=None):
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node
        self.set_list = set_list

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def get_previous(self):
        return self.previous_node

    def get_set(self):
        return self.set_list

class SetList:
    def __init__(self):
        self.front = None
        self.back = None

    def get_front(self):
        return self.front

    def get_back(self):
        return self.back

    def make_set(self, data):
        if self.front is None:
            node = Node(data, set_list=self)
            self.front = node
            self.back = node
            return node
        return None

     

    def union_set(self, other_set):
        if other_set.front is None:
            return 0

        if self.front is None:
            self.front = other_set.front
            self.back = other_set.back
        else:
            self.back.next_node = other_set.front
            other_set.front.previous_node = self.back
            self.back = other_set.back

        node = other_set.front 
        count = 0

        while node is not None:
            node.set_list = self
            node = node.next_node
            count += 1

        other_set.front = None
        other_set.back = None

        return count
       

    def find_data(self, data):
        node = self.front
        while node is not None:
            if node.data == data:
                return node
            node = node.next_node
        return None

    def representative_node(self):
        return self.front

    def representative(self):
        if self.front is None:
            return None
        return self.front.data

    def __len__(self):
        count = 0
        node = self.front
        while node is not None:
            count += 1
            node = node.next_node
        return count
