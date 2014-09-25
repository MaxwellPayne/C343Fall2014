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


    # takes value, returns node with key value
    def insert(self, k):
        pass

    # takes node, returns node
    def delete_node(self, n):
        pass

