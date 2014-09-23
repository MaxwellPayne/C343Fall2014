from BST import BSTNode, BinarySearchTree, less_than

def _main():
    bottom_left_left = BSTNode(1)
    bottom_left_right = BSTNode(3)
    mid_left = BSTNode(2, left=bottom_left_left, right=bottom_left_right)


    bottom_right_right = BSTNode(6)
    mid_right = BSTNode(5, right=bottom_right_right)
    
    root = BSTNode(4, right=mid_right, left=mid_left)

    tr = BinarySearchTree(root=root, less=less_than)

    print tr


if __name__ == '__main__':
    _main()
