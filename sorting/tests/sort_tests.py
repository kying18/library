import unittest
from sorting import sort


# merge sort
def test_merge_sort_sorted_even():
    data = [1, 2, 3, 4]
    expected = [1, 2, 3, 4]
    output = sort.merge_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)

def test_merge_sort_sorted_odd():
    data = [1, 2, 3]
    expected = [1, 2, 3]
    output = sort.merge_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)

def test_merge_sort_unsorted_even():
    data = [4, 2, 6, 1]
    expected = [1, 2, 4, 6]
    output = sort.merge_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)

def test_merge_sort_unsorted_odd():
    data = [7, 8, 3, 5, 5]
    expected = [3, 5, 5, 7, 8]
    output = sort.merge_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)

def test_merge_sort_single():
    data = [-1]
    expected = [-1]
    output = sort.merge_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)

def test_merge_sort_empty():
    data = []
    expected = []
    output = sort.merge_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)


# bubble sort
def test_bubble_sort_sorted_even():
    data = [1, 2, 3, 4]
    expected = [1, 2, 3, 4]
    output = sort.bubble_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)

def test_bubble_sort_sorted_odd():
    data = [1, 2, 3]
    expected = [1, 2, 3]
    output = sort.bubble_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)

def test_bubble_sort_unsorted_even():
    data = [4, 2, 6, 1]
    expected = [1, 2, 4, 6]
    output = sort.bubble_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)

def test_bubble_sort_unsorted_odd():
    data = [7, 8, 3, 5, 5]
    expected = [3, 5, 5, 7, 8]
    output = sort.bubble_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)

def test_bubble_sort_single():
    data = [-1]
    expected = [-1]
    output = sort.bubble_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)

def test_bubble_sort_empty():
    data = []
    expected = []
    output = sort.bubble_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)


# insertion sort
def test_insertion_sort_sorted_even():
    data = [1, 2, 3, 4]
    expected = [1, 2, 3, 4]
    output = sort.insertion_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)

def test_insertion_sort_sorted_odd():
    data = [1, 2, 3]
    expected = [1, 2, 3]
    output = sort.insertion_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)

def test_insertion_sort_unsorted_even():
    data = [4, 2, 6, 1]
    expected = [1, 2, 4, 6]
    output = sort.insertion_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)

def test_insertion_sort_unsorted_odd():
    data = [7, 8, 3, 5, 5]
    expected = [3, 5, 5, 7, 8]
    output = sort.insertion_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)

def test_insertion_sort_single():
    data = [-1]
    expected = [-1]
    output = sort.insertion_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)

def test_insertion_sort_empty():
    data = []
    expected = []
    output = sort.insertion_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)


# counting sort
def test_counting_sort_sorted_even():
    data = [1, 2, 3, 4]
    expected = [1, 2, 3, 4]
    output = sort.counting_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)

def test_counting_sort_sorted_odd():
    data = [1, 2, 3]
    expected = [1, 2, 3]
    output = sort.counting_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)

def test_counting_sort_unsorted_even():
    data = [4, 2, 6, 1]
    expected = [1, 2, 4, 6]
    output = sort.counting_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)

def test_counting_sort_unsorted_odd():
    data = [7, 8, 3, 5, 5]
    expected = [3, 5, 5, 7, 8]
    output = sort.counting_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)

def test_counting_sort_single():
    data = [-1]
    expected = [-1]
    output = sort.counting_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)

def test_counting_sort_empty():
    data = []
    expected = []
    output = sort.counting_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)


# heap sort
def test_heap_sort_sorted_even():
    data = [1, 2, 3, 4]
    expected = [1, 2, 3, 4]
    output = sort.heap_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)

def test_heap_sort_sorted_odd():
    data = [1, 2, 3]
    expected = [1, 2, 3]
    output = sort.heap_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)

def test_heap_sort_unsorted_even():
    data = [4, 2, 6, 1]
    expected = [1, 2, 4, 6]
    output = sort.heap_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)

def test_heap_sort_unsorted_odd():
    data = [7, 8, 3, 5, 5]
    expected = [3, 5, 5, 7, 8]
    output = sort.heap_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)

def test_heap_sort_single():
    data = [-1]
    expected = [-1]
    output = sort.heap_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)

def test_heap_sort_empty():
    data = []
    expected = []
    output = sort.heap_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)


# bst sort
def test_bst_sort_sorted_even():
    data = [1, 2, 3, 4]
    expected = [1, 2, 3, 4]
    output = sort.bst_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)

def test_bst_sort_sorted_odd():
    data = [1, 2, 3]
    expected = [1, 2, 3]
    output = sort.bst_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)

def test_bst_sort_unsorted_even():
    data = [4, 2, 6, 1]
    expected = [1, 2, 4, 6]
    output = sort.bst_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)

def test_bst_sort_unsorted_odd():
    data = [7, 8, 3, 5, 5]
    expected = [3, 5, 5, 7, 8]
    output = sort.bst_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)

def test_bst_sort_single():
    data = [-1]
    expected = [-1]
    output = sort.bst_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)

def test_bst_sort_empty():
    data = []
    expected = []
    output = sort.bst_sort(data)
    assert (output == expected), "Got: {}; Expected: {}".format(output, expected)


if __name__ == '__main__':
    test_merge_sort_sorted_even()
    test_merge_sort_sorted_odd()
    test_merge_sort_unsorted_even()
    test_merge_sort_unsorted_odd()
    test_merge_sort_single()
    test_merge_sort_empty()

    test_bubble_sort_sorted_even()
    test_bubble_sort_sorted_odd()
    test_bubble_sort_unsorted_even()
    test_bubble_sort_unsorted_odd()
    test_bubble_sort_single()
    test_bubble_sort_empty()

    test_insertion_sort_sorted_even()
    test_insertion_sort_sorted_odd()
    test_insertion_sort_unsorted_even()
    test_insertion_sort_unsorted_odd()
    test_insertion_sort_single()
    test_insertion_sort_empty()

    test_counting_sort_sorted_even()
    test_counting_sort_sorted_odd()
    test_counting_sort_unsorted_even()
    test_counting_sort_unsorted_odd()
    test_counting_sort_single()
    test_counting_sort_empty()

    test_heap_sort_sorted_even()
    test_heap_sort_sorted_odd()
    test_heap_sort_unsorted_even()
    test_heap_sort_unsorted_odd()
    test_heap_sort_single()
    test_heap_sort_empty()

    test_bst_sort_sorted_even()
    test_bst_sort_sorted_odd()
    test_bst_sort_unsorted_even()
    test_bst_sort_unsorted_odd()
    test_bst_sort_single()
    test_bst_sort_empty()
