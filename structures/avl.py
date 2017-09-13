class AVLTree(object):
    def __init__(self):
        self.data = {}
        # {root: {'left': left_child, 'right': right_child, 'predecessor': predecessor}}

    def add_element(self, value):
        if not self.data:
            pass