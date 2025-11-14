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

    run pacman --layout test_maze --pacman GoWestAgent
    run pacman --layout tiny_maze --pacman GoWestAgent
    run pacman --layout tiny_maze -p SearchAgent -a fn=depth_first_search
    run pacman --layout tiny_maze -p SearchAgent -a fn=uniform_cost_search
    run pacman -h
    run pacman -l tiny_maze -p SearchAgent -a fn=tiny_maze_search
    run pacman -l tiny_maze -p SearchAgent
    run pacman -l medium_maze -p SearchAgent
    run pacman -l big_maze -z .5 -p SearchAgent
    run pacman -l medium_maze -p SearchAgent -a fn=bfs
    run pacman -l big_maze -p SearchAgent -a fn=bfs -z .5
    run pacman -l medium_maze -p SearchAgent -a fn=ucs
    run pacman -l medium_dotted_maze -p StayEastSearchAgent
    run pacman -l medium_scary_maze -p StayWestSearchAgent
    run pacman -l big_maze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattan_heuristic 
    run pacman -l tiny_corners -p SearchAgent -a fn=bfs,prob=CornersProblem
    run pacman -l medium_corners -p SearchAgent -a fn=bfs,prob=CornersProblem
    run pacman -l medium_corners -p AStarCornersAgent -z 0.5
    run pacman -l test_search -p AStarFoodSearchAgent
    run pacman -l tricky_search -p AStarFoodSearchAgent
    run pacman -l big_search -p ClosestDotSearchAgent -z .5 
    run pacman -l big_search -p ApproximateSearchAgent -z .5 -q 
