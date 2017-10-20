class BinarySearchTree(object):
    """
    Class representing a binary search tree
    """
    class TreeNode(object):
        """
        Class representing a node of a binary search tree
        """
        def __init__(self, value, left=None, right=None, parent=None):
            self.value = value
            self.left = left
            self.right = right
            self.parent = parent

    def __init__(self, root_value):
        """
        Initializes the binary tree with the root value
        :param root_value: number representing the root value
        """
        self.root = self.TreeNode(value=root_value)

    def __str__(self):
        """
        String representation of the tree
        :return: String representation of the tree, where each level is on a different line and 
        each node is separated by a space. If no node exists, it is represented by a dash.
        """
        string = ''

        # gets the nodes at each level and puts the values into a string
        for i in range(self.get_height()+1):
            nodes = self.get_nodes_on_level(i)
            level = [str(node.value) if node else '-' for node in nodes]
            string += '{}\n'.format(' '.join(level))

        return string

    def get_height(self):
        """
        Gets the height of the tree
        :return: int representing height of the tree (only root = height 1)
        """
        def _get_height(node, height=None):
            if not height:
                height = self._get_level(node) + 1
            if node.left:
                height = _get_height(node.left, height+1)
            if node.right:
                height = max(height, _get_height(node.right, height+1))
            if not node.left and not node.right:
                height = self._get_level(node)
            return height
        return _get_height(self.root)


    def _get_level(self, node):
        """
        Gets the level of a node, where the root is at the 0th level
        :param node: TreeNode object in the BST
        :return: int representing the level of the node (starting from 0th level)
        """
        level = 0
        while node.parent:
            node = node.parent
            level += 1
        return level

    def get_nodes_on_level(self, level):
        """
        Returns a list of all nodes on specified level, where level 0 is the root
        :param level: int level >= 0
        :return: a list of nodes on specified level, sorted from left to right (therefore sorted)
        """
        nodes = [self.root]
        for i in range(level):
            children_nodes = []
            while nodes:
                node = nodes[0]
                children_nodes.append(node.left if node else None)
                children_nodes.append(node.right if node else None)
                nodes.remove(node)
            nodes = children_nodes
        return nodes

    # start from root
    def add_element(self, value):
        """
        Mutates the tree to add an element
        :param value: number value of the element
        :return: None
        """
        def _add_element(node, value):
            # go left if smaller than node value
            if value <= node.value:
                if node.left:
                    _add_element(node.left, value)
                else:
                    node.left = self.TreeNode(value, parent=node)

            # go right if larger than node value
            elif value > node.value:
                if node.right:
                    _add_element(node.right, value)
                else:
                    node.right = self.TreeNode(value, parent=node)
                    
        _add_element(self.root, value)

    @staticmethod
    def _find_smallest(node):
        """
        Finds the smallest element of the tree starting from the given node
        :param node: smallest element from the specified node
        :return: TreeNode of the smallest element
        """
        if node.left:
            return BinarySearchTree._find_smallest(node.left)
        else:
            return node

    def find_smallest(self):
        """
        Finds the smallest element in the entire tree
        :return: TreeNode of the smallest element
        """
        return self._find_smallest(self.root)

    def find_successor(self, node):
        """
        Finds the successor of the given node
        :param node: TreeNode element
        :return: TreeNode of the successor element or None if none exists
        """
        try:
            if node.right:
                return self._find_smallest(node.right)
            if node.parent:
                while node == node.parent.right:
                    node = node.parent
                return node.parent
        except AttributeError:
            return

if __name__ == '__main__':
    tree = BinarySearchTree(7)
    tree.add_element(5)
    tree.add_element(3)
    tree.add_element(5)
    tree.add_element(5)
    tree.add_element(7)
    tree.add_element(9)
    print(tree)
    smallest = tree.find_smallest()
    print('smallest', smallest.value)
    successor = tree.find_successor(smallest)
    print('successor', successor.value)
    successor = tree.find_successor(successor)
    print('successor', successor.value)
    successor = tree.find_successor(successor)
    print('successor', successor.value)
    successor = tree.find_successor(successor)
    print('successor', successor.value)
    successor = tree.find_successor(successor)
    print('successor', successor.value)
    successor = tree.find_successor(successor)
    print('successor', successor.value)
    successor = tree.find_successor(successor)
    print('successor', successor.value)