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
        def drill_down(node_list, accumulated):
            nones_filtered_out = filter(lambda x: x is not None, node_list)

            if len(nones_filtered_out) > 0:
                this_layer = [(n.left, n.right) for n in nones_filtered_out]
                this_layer = tuple(itertools.chain(*this_layer))
                accumulated.append(this_layer)
                return drill_down(this_layer, accumulated)
            else:
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
            level_str = ' '.join(map(lambda n: str(n).center(WIDTH) if n else ' <Leaf> ', level))
            stringified_layers.append(level_str.center(bottom_width))

        return '\n'.join(stringified_layers)

    def __repr__(self):
        return '<BinarySearchTree>\n %s' % self.__str__()

    # takes value, returns node with key value
    def insert(self, k):
        pass

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

