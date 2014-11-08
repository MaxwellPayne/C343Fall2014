We talked about heaps in great detail in lecture, so a lot of this assignment was just adapting the max_heap functions we discussed in lab and on the written homework to work for a min_heap instead.

Our function for min_heapify() uses recursion to loop through the heap at each level and check if one of the children is smalled. If so, it swaps them and continues to check downward if the tree is still a heap. build_min_heap() loops through the data and uses min_heapify() to create the heap for each key. Our function minimum() simply returns the first data point since it is a min_heap and the smallest value is the root of the tree. And extract_min() removes the first element, replaces it with the last element in the data set, calls min_heapify, and then returns the removed first value.

Overall, we each spend about two hours working on the code, debugging, and writing this README. So about 4 hours total.
