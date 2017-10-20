class BinarySearchTree(object):
    class TreeNode(object):
        def __init__(self, value, left=None, right=None, parent=None):
            self.value = value
            self.left = left
            self.right = right
            self.parent = parent

    def __init__(self, root_value):
        self.root = self.TreeNode(value=root_value)

    def __str__(self):
        string = ''
        for i in range(self.get_height()+1):
            nodes = self.get_nodes_on_level(i)
            level = [str(node.value) if node else '-' for node in nodes]
            string += '{}\n'.format(' '.join(level))
        return string

    def get_height(self):
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
        level = 0
        while node.parent:
            node = node.parent
            level += 1
        return level

    def get_nodes_on_level(self, level):
        nodes = [self.root]
        for i in range(level):
            children_nodes = []
            while nodes:
                node = nodes[0]
                children_nodes.append(node.left)
                children_nodes.append(node.right)
                nodes.remove(node)
            nodes = children_nodes
        return nodes

    # start from root
    def add_element(self, value):
        def _add_element(node, value):
            if value < node.value:
                if node.left:
                    _add_element(node.left, value)
                else:
                    node.left = self.TreeNode(value, parent=node)

            elif value >= node.value:
                if node.right:
                    _add_element(node.right, value)
                else:
                    node.right = self.TreeNode(value, parent=node)
        _add_element(self.root, value)

    @staticmethod
    def _find_smallest(node):
        if node.left:
            return BinarySearchTree._find_smallest(node.left)
        else:
            return node

    def find_smallest(self):
        return self._find_smallest(self.root)

    def find_successor(self, node):
        if node.right:
            return self._find_smallest(node.right)
        if node.parent:
            if node == node.parent.right:
                return
            return node.parent

if __name__ == '__main__':
    tree = BinarySearchTree(5)
    tree.add_element(7)
    tree.add_element(3)
    tree.add_element(9)
    smallest = tree.find_smallest()