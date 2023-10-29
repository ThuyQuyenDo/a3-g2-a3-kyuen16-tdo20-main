# A class for a min heap
class MinHeap:
   # Constructor method for the MinHeap class. 
    def __init__(self, arr=[]):
        # Initializes the heap as a list with a dummy element [0].
        self.heap = [0]
        for item in arr:
            # If an input array 'arr' is provided, each element is added to the heap and 'float-up' is called to maintain the heap property.
            self.heap.append(item)
            self.__float_up(len(self.heap) - 1)

# adds element to the MinHeap
    def insert(self, element):
        # added to the end of the heap list and then 'float-up' is called on the index of the new element to maintain the heap property.
        self.heap.append(element)
        self.__float_up(len(self.heap) - 1)

#  returns smallest value in the MinHeap without altering the data structure
    def get_min(self):
        if len(self.heap) > 1:
            return self.heap[1]
# If the heap is empty, returns None.
        else:
            return None

# removes the smallest value from the MinHeap and returns that value
    def extract_min(self):
        # first checks if the heap has more than 2 elements.
        if len(self.heap) > 2:
            # swaps the first and last elements, removes the last (minimum) element
            self.__swap(1, len(self.heap) - 1)
            min_value = self.heap.pop()
            # bubbles down the first element to restore the heap property
            self.__bubble_down(1)
            # if the heap has 2 elements
        elif len(self.heap) == 2:
            # pops and returns the last element
            min_value = self.heap.pop()
        else:
            # If the heap is empty
            min_value = None
            # Return none
        return min_value

# returns True if the MinHeap does not have any values in the heap, False otherwise
    def is_empty(self):
        return len(self.heap) == 1
#  returns number of values stored in the heap
    def __len__(self):
        return len(self.heap) - 1

# restores the heap property by moving an element up the heap if it violates the property
    def __float_up(self, index):
        # Calculate the parent index by /2
        parent_index = index // 2
        # greater than 0 && parent's value is greater than the current element's value
        if parent_index > 0 and self.heap[parent_index] > self.heap[index]:
            # swaps the two elements 
            self.__swap(parent_index, index)
            self.__float_up(parent_index)


# restores the heap property by moving an element down the heap if it violates the property
    def __bubble_down(self, index):
        # calculates the indices of the left and right child nodes using arithmetic
        left_child_index = index * 2
        right_child_index = index * 2 + 1
        # initializes a variable to keep track of the smallest child index as the current node's index.
        smallest_child_index = index

        # checks if the left child node exists and has a smaller value than the current node
        if len(self.heap) > left_child_index and self.heap[left_child_index] < self.heap[smallest_child_index]:
            # updates the smallest child index if true.
            smallest_child_index = left_child_index
            # Same but checks the right
        if len(self.heap) > right_child_index and self.heap[right_child_index] < self.heap[smallest_child_index]:
            smallest_child_index = right_child_index
            # smallest child index is different from the current node index
        if smallest_child_index != index:
            # swaps the two elements and recursively calls itself on the smallest child index to continue checking the heap property.
            self.__swap(index, smallest_child_index)
            self.__bubble_down(smallest_child_index)


# swaps two elements in the heap data structure.
    def __swap(self, i, j):
        # takes two indices as arguments, and swaps the values of the elements at those indices in the heap list using Python's tuple unpacking feature.
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]