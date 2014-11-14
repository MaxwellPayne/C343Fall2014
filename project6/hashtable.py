
#Linked list class will be how we handle chaining
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

class Hashtable(object):
    doubling_factor = 0.5

    def __init__(self, dict):
        self.n, self.m = 0, len(dict) * 4
        self.array = [None for _ in xrange(self.m)]
        self._keys = set(dict.keys())
        for k, v in dict.iteritems():
            self[k] = v

    @property
    def cls(self):
        """convenience method that returns
        the class of self"""
        return self.__class__

    @property
    def load_factor(self):
        return self.n / float(self.m)

    def _hash_key(self, key):
        return hash(key) % self.m

    def _double(self):
        print 'doubling!'
        old_array = self.array
        old_hashkeys = map(lambda k: self._hash_key(k), self.keys())
        # cloning keys this way does not handle collisions

        # double m, create a doubled array
        self.m *= 2
        self.array = [None for _ in xrange(self.m)]
        
        for key, old_hashkey in (self.keys(), old_hashkeys):
            # copy all the (key, value) pairs over to new array
            self.array[self._hash_key] = old_array[old_hashkey]


    def __getitem__(self, key):
        hashkey = self._hash_key(key)
        if self.array[hashkey] is None:
            raise KeyError('key %s is not in hashtable' % str(key))
        return self.array[self._hash_key(key)]

    def __setitem__(self, key, value):
        # does not handle collisions!
        idx = self._hash_key(key)
        
        #trying to handle collisions... definitely not right yet.
        if self.array[idx] is not None:
            node = Node(value)
            node.next = self.array[idx].head.next
            self.array[idx].head.next = node
        else:
            llist = LinkedList()
            llist.head = self.array[idx]
            node = Node(value)
            nnode = Node(self.array[idx])
            nnode.next = node  
            self.array[idx] = value
        self.n += 1
        self._keys.add(key)

        if self.load_factor >= self.cls.doubling_factor:
            self._double()

    def __delitem__(self, key):
        # {insert delete code here}
        self.n -= 1
        self._keys.remove(key)

    def keys(self):
        return tuple(self._keys)

    def __str__(self):
        return str(self.array)


if __name__ == '__main__':
    import random

    INIT_KEY_COUNT = 10 # number of keys initially inserted
    ks = tuple((random.randrange(10000) for _ in xrange(INIT_KEY_COUNT)))
    vs = tuple((random.randrange(10000) for _ in xrange(INIT_KEY_COUNT)))
    d = {}
    for k, v in zip(ks, vs):
        d[k] = v

    h = Hashtable(d)

    # filling the Hashtable with these extra keys will
    # force it to hit the doubling threshold
    ks2 = tuple((random.randrange(10000) for _ in xrange(INIT_KEY_COUNT)))
    vs2 = tuple((random.randrange(10000) for _ in xrange(INIT_KEY_COUNT)))
    for k, v in zip(ks2, vs2):
        h[k] = v
    
    print h.keys()
