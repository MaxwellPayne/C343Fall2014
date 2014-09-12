Floodit.py: a surprisingly challenging tile game

floodit.py currently imports the faster flood function from flood2.py
to run the old, crappy version, import flood from flood1.py instead

To view a plot of flood1's performance compared to that of flood2, run the command "python plotter.py times1.csv times2.csv"

Analysis:

Based on the graph that our program produces, it looks as if our first try at the flood function (flood1.py) is closest to f(n)=n^2 because it curves upward faster as the number of tiles increases. The graph of our second attempt at the function (flood2.py) has almost no curve at all and seems to increase linearly, so it is closest to f(n)=n.

We expected the function to take more time as the tiles increased, due to the fact that checked_tiles is stored as a list and takes longer and longer to check as the board size increases. This is probably the section of our algorithm that is taking up the most time and causing the execution time to grow exponentially.

We did not expect our new function to improve the test time that drastically, but it definitely made a difference based on the efficient changes we implemented. We split our flood function into two different files, one being a helper to calculate all the adjacent squares before the game is played. This saved time, as well as our storing checked_tiles as a set to decrease the amount of time the program takes on searching. This imporved the growth rate and it now appears to be linear based on the graph.
