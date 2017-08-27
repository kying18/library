# TODO: figure out how to implement this with data elements linked / how to remove from front

class LinkedList(object):
    class Element(object):
        def __init__(self, value, predecessor=None):
            self.value = value
            self.predecessor = predecessor

        # def __iter__(self):
        #     if not self.predecessor:
        #         yield self.value
        #     else:
        #         yield from self.predecessor.__iter__()
        #         yield self.value

    def __init__(self):
        super(LinkedList, self).__init__()
        self.data_list = {}
        #
        # predecessor = None
        # for data in initial_data:
        #     data_list = self.DataList(data, predecessor)
        #     self.data_list = data_list
        #     predecessor = data_list

    def add_to_end(self, value):
        if not self.data_list:
            self.data_list[self.Element(value)] = None

        else:
            #todo: fix this
            self.data_list = self.Element(value)


    def remove_from_end(self):
        self.data_list = self.data_list.predecessor

    def remove_from_front(self):
        while self.data_list.predecessor:
            new_first_element = self.data_list.predecessor
        new_first_element = self.DataList(new_first_element.data, None)

    def __str__(self):
        if self.data_list.data:
            data_list = [i for i in self.data_list]
            return(str(data_list))
        else:
            return('[]')


if __name__ == '__main__':
    linked_list = LinkedList([1, 2, 3])
    linked_list.remove_from_front()
    print(linked_list)
