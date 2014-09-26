#from termcolor import colored

from avl import AVLNode, AVLTree

def _main():

    def build_rr_tree(subtree_placement='root'):
        tr = AVLTree()
        tr.root = AVLNode('placeholder')
        
        node_a = AVLNode('A')
        node_x = AVLNode('X')
        node_y = AVLNode('Y')
        
        node_a.left = node_x
        node_a.right = node_y
        
        node_b = AVLNode('B')
        node_z = AVLNode('Z')
        
        node_b.left = node_a
        node_b.right = node_z


        if subtree_placement == 'right':
            tr.root.right = node_b
        elif subtree_placement == 'left':
            tr.root.left = node_b
        else: # tr.root is b
            tr.root = node_b
        
        return tr

    def build_rl_tree(subtree_placement='root'):

        tr = AVLTree()
        tr.root = AVLNode('placeholder')
        
        node_a = AVLNode('A')
        node_x = AVLNode('X')
        node_y = AVLNode('Y')
        
        
        node_b = AVLNode('B')
        node_z = AVLNode('Z')
        

        node_b.right = node_z
        node_b.left = node_y

        node_a.right = node_b
        node_a.left = node_x
        

        if subtree_placement == 'right':
            tr.root.right = node_a
        elif subtree_placement == 'left':
            tr.root.left = node_a
        else: # tr.root is a
            tr.root = node_a
        
        return tr


    

    #print colored('rotate_right test', 'blue')
    print 'rotate_right test'

    rr_tree = build_rr_tree()

    rr_tree.rotate_right(rr_tree.root)

    #print rr_tree

    #print colored('rotate_left test', 'blue')
    print 'rotate_left test'


    rl_tree = build_rl_tree()

    #print rl_tree

    rl_tree.rotate_left(rl_tree.root)

    print rl_tree


    print rl_tree.delete_node(rl_tree.root)

    print rl_tree.insert('Q')

    print rl_tree


    tr = AVLTree()
    tr.insert(30)
    tr.insert(21)
    tr.insert(0)
    tr.insert(3)
    tr.insert(5)
    tr.insert(8)

    tr.delete_node(tr.search(5))

    print tr


if __name__ == '__main__':
    _main()