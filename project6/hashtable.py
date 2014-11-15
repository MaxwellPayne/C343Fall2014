from LinkedList import Node, LinkedList

class Hashtable(object):
    """hashtable implementation using
    division method hashing and chaining
    to resolve collisions"""
    doubling_factor = 0.5
    halving_factor  = 0.25

    def __init__(self, dict):
        self._size = len(dict) * 4

        if self._size % 2 == 0:
            # ensure that size is always odd
            self._size += 1

        self.slots_taken = 0
        self.array = [None for _ in xrange(self._size)]
        self._keys = set(dict.keys())
        for k, v in dict.iteritems():
            self[k] = v

    @property
    def cls(self):
        """convenience method that returns
        the class of self"""
        return self.__class__

    @property
    def size(self):
        return self._size

    @property
    def load_factor(self):
        return self.slots_taken / float(self._size)

    def _hash_key(self, key):
        """simple division method hashing"""
        return hash(key) % self._size

    def _double(self):
        #print 'doubling at load factor %s' % str(self.load_factor)
        old_array = self.array

        self._size = self._size * 2 + 1
        # ensure an odd new size

        self.array = [None for _ in xrange(self._size)]
        self.slots_taken = 0

        for old_cell in old_array:
            # copy over all the old keys, re-hashing them because
            # self._hash_key works differently with new self._size
            if old_cell is not None:
                node = old_cell.head
                while node:
                    self[node.key] = node.value
                    node = node.next

    def _halve(self):
        #print 'halving at load factor %s' % str(self.load_factor)
        old_array = self.array

        self._size = self_size / 2 + 1
        #ensure an odd new array size

        self.array = [None for _ in xrange(self._size)]
        self.slots_taken = 0

        for old_cell in old_array:
            # works the same as doubling
            if old_cell is not None:
                node = old_cell.head
                while node:
                    self[node.key] = node.value
                    node = node.next

    def __getitem__(self, key):
        if key not in self._keys:
            # all keys are tracked in this set
            # if it isn't there, it was never inserted
            raise KeyError('key %s is not in hashtable' % str(key))            

        hashslot = self._hash_key(key)
        node = self.array[hashslot].head
        while node:
            if node.key == key:
                return node.value
            node = node.next

    def __setitem__(self, key, value):
        idx = self._hash_key(key)
        self._keys.add(key)
        
        node = Node(key, value)
        
        if self.array[idx] is not None:
             # collision! llist already exists here, add to it
            self.array[idx].head = node
        else: # build a llist at empty slot
            self.slots_taken += 1
            llist = LinkedList(head=node)
            self.array[idx] = llist

        if self.load_factor >= self.cls.doubling_factor:
            self._double()

    def __delitem__(self, key):
        # {insert actual delete code here}

        idx = self._hash_key(key)

        # Only checks the slot in the array that this key could be in,
        # then moves pointers to remove it from chain.
        if self.array[idx].head.key == key:
            self.array[idx].head.next = self.array[idx].head
        else:
            prev = self.array[idx].head
            current = self.array[idx].head.next
            notfound = True
            while(notFound):
                if current.key == key:
                    prev.next = prev.next.next
                    notFound = False
                else:
                    prev = current
                    current = current.next

        self._keys.remove(key)

        if self.load_factor <= self.cls.halving_factor:
            self._halve()

    def keys(self):
        return tuple(self._keys)

    def __str__(self):
        cells = []
        for idx in range(self._size):
            cells.append('[%s] -> %s' % (idx, self.array[idx]))
        return '\n'.join(cells)

    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    import random

    INIT_KEY_COUNT = 10 # number of keys initially inserted
    ks = tuple((random.randrange(10000) for _ in xrange(INIT_KEY_COUNT)))
    vs = tuple((random.randrange(10000) for _ in xrange(INIT_KEY_COUNT)))

    d = {}
    
    for k, v in zip(ks, vs):
        d[k] = v

    h = Hashtable(d)

    print h
    print '\n' * 3

    while True:
        # fills hashtable until it doubles
        begin_size = h.size
        k, v = random.randrange(10000), random.randrange(10000)
        h[k] = v
        if h.size != begin_size:
            break
        
    # print doubled hashtable
    print h

    for k in h.keys():
        # print all keys and their values
        print '%s : %s' % (k, h[k])
