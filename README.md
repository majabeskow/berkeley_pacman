# What is this?
- This is an updated version (from python2 to python3) of the [Berkeley Pacman](https://inst.eecs.berkeley.edu/~cs188/fa24/projects/) project. Its nearly 1-to-1 so you should be able to follow along with their general ideas.
Changes:
- It has been formatted using Black (pypi)
- The casing has been standardized to snake case
- A light version of wumpus world has been added

# How do I get this code to run?

All the setup instructions are inside [documentation/setup.md](./documentation/setup.md)

# What are the important files?

- `main/` contains all the code, however you can ignore many of the python files
- `main/search.py` is where all your search algorithms should be.<br>(search for `*** YOUR CODE HERE ***`)
- `main/search_agents.py` is where all of your agents should be.


# What commands are there?

    python pacman.py
    python pacman.py -h
    python pacman.py -l tiny_maze -p SearchAgent -a fn=tiny_maze_search
    python pacman.py -l tiny_maze -p SearchAgent -a fn=depth_first_search
    python pacman.py -l medium_maze -p SearchAgent -a fn=bfs
    python pacman.py -l tiny_maze -p SearchAgent -a fn=uniform_cost_search
    python pacman.py -l test_maze --pacman GoWestAgent
    python pacman.py -l tiny_maze --pacman GoWestAgent
    python pacman.py -l big_maze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattan_heuristic 
    python pacman.py -l tiny_corners -p SearchAgent -a fn=bfs,prob=CornersProblem
    python pacman.py -l medium_corners -p SearchAgent -a fn=bfs,prob=CornersProblem
    python pacman.py -l tiny_maze -p SearchAgent
    python pacman.py -l medium_maze -p SearchAgent
    python pacman.py -l big_maze -z .5 -p SearchAgent
    python pacman.py -l big_maze -p SearchAgent -a fn=bfs -z .5
    python pacman.py -l medium_maze -p SearchAgent -a fn=ucs
    python pacman.py -l medium_dotted_maze -p StayEastSearchAgent
    python pacman.py -l medium_scary_maze -p StayWestSearchAgent
    python pacman.py -l medium_corners -p AStarCornersAgent -z 0.5
    python pacman.py -l test_search -p AStarFoodSearchAgent
    python pacman.py -l tricky_search -p AStarFoodSearchAgent
    python pacman.py -l big_search -p ClosestDotSearchAgent -z .5 
    python pacman.py -l big_search -p ApproximateSearchAgent -z .5 -q 
