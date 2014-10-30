from swap import swap

def less(x, y):
    return x < y

def less_key(x, y):
    return x.key < y.key

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * (i + 1)

def parent(i):
    return (i-1) / 2

# Student code -- fill in all the methods that have pass as the only statement
class Heap:
    def __init__(self, data, 
                 less = less):
        self.data = data
        self.less = less
        self.heap_size = 0
        self.build_min_heap()
        
    def __repr__(self):
        """ ignore this for now, we can
        use it if we want to debug
        parent-child relationships later
        
        for idx, data in enumerate(self.data):
            l, r = left(idx), right(idx)
            s = "%s" % data
            if l < self.heap_size:
                s += ' left is %s' % self.data[l]
            if r < self.heap_size:
                s += ' right is %s' % self.data[r]
            if s == "%s" % data:
                s += ' has no children'
            print s
        return 'done printing heap'"""
        
        # only print as much data as
        # self.heap_size cares about
        return repr(self.data[:self.heap_size])

    def minimum(self):
        pass

    def insert(self, obj):
        self.heap_size += 1
        idx = self.heap_size - 1

        if self.heap_size >= len(self.data):
            # expand the array if insert would
            # overflow the array bounds
            self.data += [obj]
        else:
            self.data[idx] = obj

        lessThan = self.less
        while idx >= 0 and lessThan(self.data[idx], self.data[parent(idx)]):
            # start with data at the bottom, percolate up
            # while parent is greater than
            swap(self.data, idx, parent(idx))
            idx = parent(idx)

    def extract_min(self):
        pass
        
    def min_heapify(self, i):
        lessThan = self.less
        smallest = i
        l_idx, r_idx = left(i), right(i)
            
        if l_idx < self.heap_size and lessThan(self.data[l_idx], self.data[i]):
            smallest = l_idx
        if r_idx < self.heap_size and lessThan(self.data[r_idx], self.data[smallest]):
            smallest = r_idx
        if smallest != i:
            swap(self.data, i, smallest)
            return self.min_heapify(smallest)
    
    def build_min_heap(self):
        self.heap_size = len(self.data)
        for i in xrange(self.heap_size / 2, -1, -1):
            self.min_heapify(i)


class PriorityQueue:
    def __init__(self, less=less_key):
        self.heap = Heap([], less)

    def __repr__(self):
        return repr(self.heap)

    def push(self, obj):
        self.heap.insert(obj)

    def pop(self):
        return self.heap.extract_min()

if __name__ == "__main__":

    def compare_heaps(data):
        import heapq, copy
        library_heap = copy.copy(data)

        heapq.heapify(library_heap)
        our = Heap(data)
        
        for i in range(45, 49):
            
            heapq.heappush(library_heap, i)
            our.insert(i)

        print '    our heap: %s' % our
        print 'library heap: %s' % library_heap



    # unit tests here
    from random import shuffle
    d = range(0, 20, 2)
    shuffle(d)

    compare_heaps(d)

