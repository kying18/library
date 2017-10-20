# # you can write to stdout for debugging purposes, e.g.
# # print "this is a debug message"
#
# def solution(A, B):
#     # in order for B to be a substring of A, all characters of B must
#     # appear in A
#     for char in B:
#         if char not in A:
#             return -1
#
#     # if length of B is less than/equal to length of A, and B does not appear
#     # in 2A, then there is no solution
#     if len(B) <= len(A) and B not in A + A:
#         return -1
#
#     # if length of A is less than length of B, and B does not appear in cA,
#     # where c is number of times such that length of cA > length of B,
#     # then there is no solution
#     length_A = len(A)
#     length_B = len(B)
#     c = length_B / length_A + 1
#     if length_A < length_B:
#         c = length_B / length_A + 1
#         if B not in c * A:
#             return -1
#
#     # otherwise, count number of times that A must be repeated such that B is
#     # a substring
#     count = 1
#     original_A = A
#     while B not in A:
#         count += 1
#         A += original_A
#
#     return count

# print(solution('abc', 'cab'))


from collections import Counter


class Node(object):
    def __init__(self, value, node_number):
        self.value = value
        self.node_number = node_number
        self.edges = []

    def add_edge(self, node):
        self.edges.append(node)


def longest_path_from_node(node, visited=None):
    # get valid nodes that can be reached
    reachable_nodes = node.edges

    # filter based on values
    valid_nodes = [n for n in reachable_nodes if n.value == node.value and (
        (visited and n not in visited) or (not visited))]

    # base case
    if not valid_nodes:
        return 0

    else:
        if visited:
            visited.add(node)
        else:
            visited = set(node)
        longest_path_length = max(
            [longest_path_from_node(valid_node, visited) + 1 for valid_node in valid_nodes])

    return longest_path_length


def solution(A, E):
    # finding the most common item and then the maximum number of times
    # that item repeats (index 0 to index the tuple, and then index 1 to get
    # the number of times it repeats)
    max_occurrences_same_val = Counter(A).most_common(1)[0][1]
    max_length_path = max_occurrences_same_val - 1

    nodes = []
    for i in range(len(A)):
        nodes.append(Node(A[i], i + 1))

    for i in range(0, (len(A) - 1) * 2, 2):
        print(i)
        edge_node = nodes[E[i]-1]
        other_node = nodes[E[i + 1]-1]
        edge_node.add_edge(other_node)
        other_node.add_edge(edge_node)

    longest_path = 0
    for node in nodes:
        longest_path = max(longest_path, longest_path_from_node(node))

    return longest_path


print(solution([1, 1, 1, 2, 2], [1, 2, 1, 3, 2, 4, 2, 5]))