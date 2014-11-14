"""Linked list class will be how we handle chaining"""

class Node(object):
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.next = None

    def __str__(self):
        return '<Node %s : %s>' % (self.key, self.value)

    def __repr__(self):
        return str(self)


class LinkedList(object):
    def __init__(self, head=None):
        self._head = head

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, node):
        """automatically links the new 
        head to the old head"""
        node.next = self.head
        self._head = node

    def __str__(self):
        all_nodes = []
        current_node = self.head
        while current_node:
            all_nodes.append(str(current_node))
            current_node = current_node.next
        all_nodes.append(str(None))
        return ' -> '.join(all_nodes)

    def __repr__(self):
        return str(self)
