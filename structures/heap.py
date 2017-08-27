# default heap is max heap
# TODO: write tests for data structure
class Heap(object):
    def __init__(self, max_heap=True):
        super(Heap, self).__init__()
        self.data = []
        less_than = lambda x, y: x < y
        greater_than = lambda x, y: x > y
        if max_heap:
            self.comparison_fxn = less_than
        else:
            self.comparison_fxn = greater_than

    # @staticmethod
    # def heapify(heap, value):
    #     index = len(heap) - 1
    #     parent_index = int(len(heap) / 2)
    #     while heap[index] > heap[parent_index] and parent_index >= 0:
    #         heap[index] = heap[parent_index]
    #         heap[parent_index] = value
    #         index = parent_index
    #         parent_index = int(index / 2)
    #     return heap

    def add_element(self, value):
        """
        Adds an element to the data of the heap
        :param value: value to be added to heap
        :return: list representation of heap
        """
        self.data.append(value)
        index = len(self.data) - 1
        parent_index = int(len(self.data) / 2)

        # while the parent does not satisfy the heap quality (ex. max heap parent is < index)
        while self.comparison_fxn(self.data[parent_index], self.data[index]) and parent_index >= 0:
            self.data = self.swap(self.data, index, parent_index)
            # self.data[index] = self.data[parent_index]
            # self.data[parent_index] = value
            index = parent_index
            parent_index = int(index / 2)
        return self.data

    @staticmethod
    def swap(_list, index, index_to_swap_with):
        """
        Swaps the numbers at index and index to swap with in the list
        :param _list: nonempty list
        :param index: index of one number in the swap, must be a valid index (ie. between 0
            and len(_list)-1)
        :param index_to_swap_with: index of number to swap with, must be a valid index 
            (ie. between 0 and len(_list)-1)
        :return: list with the values at index and index_to_swap_with exchanged
        """
        value = _list[index]
        _list[index] = _list[index_to_swap_with]
        _list[index_to_swap_with] = value
        return _list

    def remove_element(self, value):
        """
        Removes the value from the heap, or prints an error and returns None
        :param value: value to remove from the heap
        :return: list representing the heap with the value removed
        """
        try:
            node_index = self.data.index(value)

            # swap values and remove last element
            self.data[node_index] = self.data[-1]
            self.data = self.data[:-1]

            # swap node until min
            node_value = self.data[node_index]
            left_index = node_index * 2 + 1
            right_index = node_index * 2 + 2
            heap_size = len(self.data)

            # as long as left/right index are within bounds and node is not the minimum (max)
            while (0 < left_index < heap_size and 0 < right_index < heap_size) and \
                    (self.comparison_fxn(node_value, self.data[left_index]) or
                             self.comparison_fxn(node_value, self.data[right_index])):

                # if node is less than left child, swap (for max)
                if self.comparison_fxn(node_value, self.data[left_index]):
                    self.data = self.swap(self.data, node_index, left_index)
                    node_index = left_index

                # if node is less than right child, swap (for max)
                elif self.comparison_fxn(node_index, self.data[right_index]):
                    self.data = self.swap(self.data, node_index, right_index)
                    node_index = right_index

                # reassign left index and right index
                left_index = node_index * 2 + 1
                right_index = node_index * 2 + 2

            return self.data

        except ValueError:
            print('Value not found in heap')

    def __str__(self):
        return str(self.data)

if __name__ == '__main__':
    heap = Heap(max_heap=False)
    for number in [3, 2, 1]:
        heap.add_element(number)
    print(heap)