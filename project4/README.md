When we started working on project 4, Max had the idea to make each cell of the allignment graph to be its own object, which we call a Cell, and to have each cell keep track of which direction it points back to and what value it has. This made it easier to keep track of the graph and retrace our steps at the end.

However, the way that we implemented it didn't make sense to use the enable_graphics code that was later included in the pdf, and so we have a way of simply printing out the cells in a matrix to view in place of the graph.

More specifically, we have a nested "for" loop that checks the cell above, diagonal, and to the left of it, finds the largest value, and adds it to its own while keeping track of that direction as "I", "M", or "D" as in the pdf example. Then, using those values, we have another function trace the best path back from the end and print out the corresponding best match for the strings.

The code passes all tests in the project folder, as well as all others that we tried.