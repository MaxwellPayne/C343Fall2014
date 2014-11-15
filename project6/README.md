The hashtable.py file provided was basically completely empty, so we had a lot of freedom to implement it the way we wanted. We designed our hashtable to always be of odd size in order to increase the number of slots that will be used when hashing, and defined our doubling and halving factors to optimize space used.

After initializing our hash table, we added some helpful properties to help us easily access certain information about our table using the @property command. Then, we defined our hash function to simply use the division method. The double and halve functions copy the values into a new array of different size, based upon the size of the load factor we defined.

For the rest of the code, we implemented chaining using the LinkedList and Node classes that we include in a seperate file. __getitem__ finds where the key would be inserted based on its hash value, and searches the linked list for it. __setitem__ either creates a new node with the key and value in the index it is hashed too, or adds to the chain of nodes already there. Lastly, __delitem__ finds an item and changes the linked list in that slot to remove it.

This project was a little more challenging than the last and probably took us a combined 6 hours from when we started thinking about it to having finished code that passed all the tests.
