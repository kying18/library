# TODO: figure out how to implement this with data elements linked / how to remove from front

class LinkedList(object):
    class Element(object):
        def __init__(self, value, predecessor=None):
            self.value = value
            self.predecessor = predecessor

        def __iter__(self):
            if not self.predecessor:
                yield self.value
            else:
                yield from self.predecessor.__iter__()
                yield self.value

        def __str__(self):
            return str(self.value)

    def __init__(self):
        super(LinkedList, self).__init__()
        self.data_list = {}

    def add_to_end(self, value):
        if not self.data_list:
            self.data_list[self.Element(value)] = None

        else:
            for (element, successor) in self.data_list.items():
                if not successor:
                    new_element = self.Element(value, element)
                    self.data_list[element] = new_element
                    self.data_list[new_element] = None
                    break

    def remove_from_end(self):
        end_node = None
        for (element, successor) in self.data_list.items():
            if not successor:
                self.data_list.pop(element)
                end_node = element
                break
        for (element, successor) in self.data_list.items():
            if successor == end_node:
                self.data_list[element] = None
                break

    def remove_from_front(self):
        start_node = None
        for (element, successor) in self.data_list.items():
            if not element.predecessor:
                self.data_list.pop(element)
                start_node = successor
                break
        for element in self.data_list.keys():
            if element == start_node:
                element.predecessor = None
                break

    def __str__(self):
        if self.data_list:
            data_list = [str(i) for i in self.data_list]
            return(str(data_list))
        else:
            return('[]')


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.add_to_end(1)
    linked_list.add_to_end(2)
    linked_list.add_to_end(3)
    linked_list.remove_from_end()

    print(linked_list)
