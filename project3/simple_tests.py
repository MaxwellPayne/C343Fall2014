from BST import BSTNode, BinarySearchTree, less_than

def _main():
    bottom_left_left = BSTNode(1)
    bottom_left_right = BSTNode(3)
    mid_left = BSTNode(2, left=bottom_left_left, right=bottom_left_right)


    bottom_right_right = BSTNode(6)
    mid_right = BSTNode(5, right=bottom_right_right)
    
    root = BSTNode(4, right=mid_right, left=mid_left)

    tr = BinarySearchTree(root=root, less=less_than)
    
    #print tr

    tr.insert(20)

    #print tr

    newTree = BinarySearchTree()
    newTree.insert(10)
    newTree.insert(8)
    newTree.insert(12)
    newTree.insert(14)
    newTree.insert(16)

    assert newTree.root.key == 10
    assert newTree.root.left.key == 8
    assert newTree.root.right.key == 12
    assert newTree.root.right.right.key == 14
    assert newTree.root.right.right.right.key == 16

    print newTree


if __name__ == '__main__':
    _main()
