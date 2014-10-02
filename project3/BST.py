import itertools

from stack import ArrayStack

class BSTNode(object):
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = None
        #self.height = 1

    def __str__(self):
        return 'Node(%s)' % str(self.key)

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

    # returns the minimum from this node down
    @property
    def minimum(self):
        frontier = self
        while frontier.left:
            frontier = frontier.left
        return frontier

    # returns the maximum from this node down
    @property
    def maximum(self):
        frontier = self
        while frontier.right:
            frontier = frontier.right
        return frontier


def less_than(x,y):
    return x < y

class BinarySearchTree(object):
    def __init__(self, root = None, less=less_than, node_class=BSTNode):
        self._root = root
        self.less = less
        self._node_class = node_class

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, node):
        node.parent = None
        self._root = node
        
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

    # to be used for avl.py when it is working
    '''
    def calculate_height(self):
        if not self.root.left:
            if not self.root.right:
                return 1
            else:
                return 1 + self.root.right.height
        else:
            if not self.root.right:
                return 1 + self.root.left.height
            else:
                return max(self.root.left.height,self.root.right.height)+1
    '''

    # takes value, returns node with key value
    def insert(self, k):
        new_node = self._node_class(k)
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
        return new_node

    @property
    def minimum(self):
        return self.root.minimum

    # takes node, returns node
    # return the node with the smallest key greater than n.key
    def successor(self, n):
        # Succ is min(right subtree) if exists
        if n.right:
            return n.right.minimum
        
        # ascend the tree until you take a right->left upward jump
        # at which point the current node is the left child of
        # the parent and the parent is greater than n
        above_me, current = n.parent, n
        while above_me and above_me.right is current:
            current = above_me
            above_me = above_me.parent
        return above_me

    # return the node with the largest key smaller than n.key
    def predecessor(self, n):
        if n.left:
            return n.left.maximum
        # search up the tree until find a parent to the left
        # where the node is the right child and smaller than
        # the parent node.
        if n.left == None and n.right == None:
            return None
        else:
            while n.parent and n.parent.left is n:
                n = n.parent
                n.parent = n.parent.parent
            return n.parent

    # helper function to check every node
    def search_node(self,n,key):
        if n.key == key:
            return n
        if self.less(n.key,key) and n.right:
            return self.search_node(n.right,key)
        elif n.left:
            return self.search_node(n.left,key)


    # takes key returns node
    # can return None
    def search(self, k):
        #if not self.root:
        #    return
        #search_stack = ArrayStack()
        #search_stack.push((self.root,self.root.key))
        #while not search_stack.is_empty():
        if self.root.key == k:
            return self.root
        else:
            return self.search_node(self.root,k)

            
    # a function we discussed in class
    # takes two nodes and replaces the first with the second
    def transplant(self, n, n2):
        n2.left = n.left
        n2.right = n.right




        if n2 is n2.parent.left:
            n2.parent.left = None
        elif n2 is n2.parent.right:
            n2.parent.right = None


        if n is self.root:
            self.root = n2

        else:
            if n is n.parent.left:
                n.parent.left = n2
            elif n is n.parent.right:
                n.parent.right = n2
     


    # uses the transplant helper function to replace a node
    # and essentially delete it
    def delete_node(self, n):
        if n.right:
            new_top = n.right.minimum
            self.transplant(n, new_top)
            return new_top
        elif n.left:
            new_top = n.left.maximum
            self.transplant(n, new_top)
            return new_top
        else:
            if n.parent.left is n:
                n.parent.left = None
            else:
                n.parent.right = None
            return n.parent

