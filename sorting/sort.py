from structures.heap import Heap

def merge_sort(data_list):
    """
    Sort a list using the merge sort algorithm (split the list until smallest possible
    element; combine by taking the least from each merged list)
    :param data_list: list of comparable, sortable elements (ie. numbers)
    :return: sorted list from minimum to maximum
    """
    sorted_list = []

    # base case: if no data, return empty list
    if not data_list:
        return []

    # base case: if list contains one element, return list containing element
    elif len(data_list) == 1:
        return data_list

    # else recursively call merge sort on both halves of the list
    # sort elements according to the least in each half
    elif len(data_list) > 1:
        # call merge sort of halves of the list
        halfway_index = int(len(data_list)/2)
        first_list = merge_sort(data_list[:halfway_index])
        second_list = merge_sort(data_list[halfway_index:])

        # while elements still exist
        while first_list or second_list:
            # if elements exist in both lists, find the minimum and remove from list
            if first_list and second_list:
                min_element = min(first_list[0], second_list[0])
                sorted_list.append(min_element)
                if min_element == first_list[0]:
                    first_list = first_list[1:]
                else:
                    second_list = second_list[1:]

            # if elements in either list still exist, extend results by elements in list
            elif first_list:
                sorted_list.extend(first_list)
                break
            elif second_list:
                sorted_list.extend(second_list)
                break

        return sorted_list

def bubble_sort(data_list):
    """
    Sort a list using the bubble sort algorithm (swap adjacent elements
    if element is less than preceding)
    :param data_list: list of elements to sort
    :return: sorted list from minimum to maximum
    """
    if not data_list:
        return []

    elif len(data_list) == 1:
        return data_list

    else:
        # keep track of preceding element
        previous_element = data_list[0]

        # iterate through each element in list and swap if necessary
        for i in range(1, len(data_list)):
            element = data_list[i]

            if element < previous_element:
                # swap element with previous element
                data_list[i-1] = element
                data_list[i] = previous_element

            else:
                # set previous element to current element
                previous_element = element

        # perform bubble sort up to the element
        data_list[:len(data_list) - 1] = bubble_sort(data_list[:len(data_list) - 1])

        return data_list

def insertion_sort(data_list):
    """
    Sort a list using insertion sort (insert each element where it belongs,
    found by iterating through the list)
    :param data_list: list of elements to sort
    :return: sorted list of elements from least to greatest
    """
    if not data_list:
        return []

    # iterate through list and see if any elements are out of order
    for i in range(1, len(data_list)):
        element = data_list[i]

        # out of order
        if element < data_list[i-1]:
            # iterate through previous elements to find where element belongs
            for j in range(i):
                # find where element belongs (index j)
                if element < data_list[j]:
                    data_list[j+1:i+1] = data_list[j:i]
                    data_list[j] = element
                    break

    return data_list

def heap_sort(data_list):
    heap = Heap(max_heap=False)
    for element in data_list:
        heap.add_element(element)
    # TODO: implement rest of heapsort

def counting_sort(data_list):
    counts = {}
    sorted_list = []

    # iterate through elements in data list to get counts
    for element in data_list:
        counts[element] = counts.get(element, 0) + 1

    # iterate through sorted keys and append to sorted list
    for element in sorted(counts.keys()):
        frequency = counts[element]
        sorted_list += [element] * frequency

    return sorted_list

def radix_sort(data_list):
    pass

if __name__ == '__main__':
    _list = [3, 2, 1]
    print(heap_sort(_list))
