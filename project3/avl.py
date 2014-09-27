from BST import BSTNode, BinarySearchTree

# AVL Trees, by Elizabeth Feicke

class AVLNode(BSTNode):
    pass
        
def less_than(x,y):
    return x < y

class AVLTree(BinarySearchTree):


    def rotate_right(self, old_top):
        switch_branch = old_top.left.right
        new_top = old_top.left
        parent_above = old_top.parent
        
        if not parent_above: # old_top is root
            self.root = new_top
        elif old_top is parent_above.right:
            parent_above.right = new_top
        else: # old_top is old_top.parent.left
            parent_above.left = new_top
            
        new_top.right = old_top
        old_top.left = switch_branch

    def rotate_left(self, old_top):
        switch_branch = old_top.right.left
        new_top = old_top.right
        parent_above = old_top.parent

        if not parent_above: # old_top is root
            self.root = new_top
        elif old_top is parent_above.right:
            parent_above.right = new_top
        else: # old_top is old_top.parent.left
            parent_above.left = new_top

        new_top.left = old_top
        old_top.right = switch_branch

    # doesn't work yet
    def is_balanced(self,n):
        if not n.left:
            if not n.right:
                return 0
            else:
                return -(n.right.height)
        else:
            if not n.right:
                return n.left.height
            else:
                return (n.left.height-n.right.height)

    # also doesn't work yet
    def rebalance(self,n):
        if(self.is_balanced(n) == 2):
            if(self.is_balanced(n.left) == 1):
                right_rotate(n)
            else:
                left_rotate(n.left)
                right_rotate(n)
        elif(self.is_balanced(n) == -2):
            if(self.is_balanced(n.right) == -1):
                left_rotate(n)
            else:
                right_rotate(n.right)
                left_rotate(n)

    # takes value, returns node with key value
    def insert(self, k):
        inserted_node = super(AVLTree, self).insert(k)
        #self.rebalance()
        print 'inserted %s' % inserted_node

    # takes node, returns node
    def delete_node(self, n):
        deleted_node = super(AVLTree, self).delete_node(n)
        #self.rebalance()
        print 'deleted %s' % deleted_node
