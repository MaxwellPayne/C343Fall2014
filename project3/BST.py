import itertools

from stack import ArrayStack

class BSTNode(object):
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = None

    def __str__(self):
        return 'Node(%s)' % self.key

    def __repr__(self):
        return self.__str__()

    @property
    def left(self):
        return self._left
    
    @left.setter
    def left(self, node):
        if node:
            node.parent = self
        self._left = node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        if node:
            node.parent = self
        self._right = node


def less_than(x,y):
    return x < y

class BinarySearchTree(object):
    def __init__(self, root = None, less=less_than):
        self.root = root
        self.less = less

    def __str__(self):
        # recursive function that creates a list of nodes
        # for each level, None if node doesn't exist at that slot
        from itertools import chain

        # recursively accumulates nodes at each level of tree
        def drill_down(node_list, accumulated):
            if any(isinstance(n, BSTNode) for n in node_list):
            # there are leaves left to explore
                this_layer = [(n.left, n.right) if n else (None,) for n in node_list]
                this_layer = tuple(chain(*this_layer))
                accumulated.append(this_layer)
                return drill_down(this_layer, accumulated)
            else:
                # last level was all leaves, remove it and return
                accumulated.pop()
                return accumulated

        if not self.root:
            return '<NullTree>'

        levels = drill_down([self.root], [(self.root,)])
        
        WIDTH = 10
        bottom_width = int(pow(2, len(levels)-1)) * WIDTH

        # center all the nodes
        stringified_layers = []
        for level in levels:
            level_str = ' '.join(map(lambda n: str(n).center(WIDTH) if n else '<Null> ', level))
            stringified_layers.append(level_str.center(bottom_width))

        return '\n'.join(stringified_layers) + '\n'

    def __repr__(self):
        return '<BinarySearchTree>\n %s' % self.__str__()

    # takes value, returns node with key value
    def insert(self, k):
        new_node = BSTNode(k)
        if not self.root:
            self.root = new_node
        else:
            location, parent = self.root, None
            while location is not None:
                parent = location
                location = location.left if self.less(new_node.key, location.key) else location.right
        
            if self.less(new_node.key, parent.key):
                parent.left = new_node
            else:
                parent.right = new_node

    # takes node, returns node
    # return the node with the smallest key greater than n.key
    def successor(self, n):
        pass

    # return the node with the largest key smaller than n.key
    def predecessor(self, n):
        pass

    # takes key returns node
    # can return None
    def search(self, k):
        pass
            
    # takes node, returns node
    def delete_node(self, n):
        pass

