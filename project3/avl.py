from BST import BSTNode, BinarySearchTree

# AVL Trees, by Elizabeth Feicke

class AVLNode(BSTNode):
    @property
    def height(self):
        if (not self.left) and (not self.right):
            return 1
        
        l = self.left.height if self.left else 0
        r = self.right.height if self.right else 0
        return max(l, r) + 1
        
def less_than(x,y):
    return x < y

class AVLTree(BinarySearchTree):

    def __init__(self, root = None, less=less_than):
        super(AVLTree, self).__init__(root=root, less=less_than, node_class=AVLNode)

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
        return new_top

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
        return new_top

    @staticmethod
    def is_balanced(n):
        left_height = n.left.height if n.left else 0
        right_height = n.right.height if n.right else 0
        balance_factor = abs(left_height - right_height)
        return balance_factor < 2
        """    
        if not n.left:
            if not n.right:
                return True
            else:
                return -(n.right.height)
        else:
            if not n.right:
                return n.left.height
            else:
                return (n.left.height-n.right.height)"""


    def rebalance(self, possible_offender):
        if not possible_offender.parent or not possible_offender.parent.parent:
            return
        
        top = possible_offender.parent.parent
        new_top = possible_offender.parent

        if not self.is_balanced(top):

            if top.left and top.left.left and possible_offender is top.left.left:
                print 'r right case'
                new_top = self.rotate_right(top)
            elif top.right and top.right.right and possible_offender is top.right.right:
                print 'r left case'
                new_top = self.rotate_left(top)
            elif top.left and top.left.right and possible_offender is top.left.right:
                print 'r left then right case'
                self.rotate_left(top.left)
                new_top = self.rotate_right(top)
            elif top.right and top.right.left and possible_offender is top.right.left:
                print 'r right then left case'
                self.rotate_right(top.right)
                new_top = self.rotate_left(top)
            else:
                raise Exception("we're doing this wrong")


        if new_top:
            self.rebalance(new_top)
        """
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
        self.calculate_height(n)
        """
        

    # takes value, returns node with key value
    def insert(self, k):
        inserted_node = super(AVLTree, self).insert(k)
        self.rebalance(inserted_node)

    # takes node, returns node
    def delete_node(self, n):
        raise NotImplementedError('cant do delete')
        deleted_node = super(AVLTree, self).delete_node(n)
        #self.rebalance()
        print 'deleted %s' % deleted_node
