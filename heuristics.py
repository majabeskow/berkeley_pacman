import search


#
# heuristics
#
def a_really_really_bad_heuristic(position, problem):
    from random import random, sample, choices

    return int(random() * 1000)


def null_heuristic(state, problem=None):
    return 0


def your_heuristic(state, problem=None):
    from search_agents import FoodSearchProblem

    #
    # heuristic for the find-the-goal problem
    #
    if isinstance(problem, search.SearchProblem):
        # data
        pacman_x, pacman_y = state
        goal_x, goal_y = problem.goal

        # YOUR CODE HERE (set value of optimisitic_number_of_steps_to_goal)

        optimisitic_number_of_steps_to_goal = 0
        return optimisitic_number_of_steps_to_goal
    #
    # traveling-salesman problem (collect multiple food pellets)
    #
    elif isinstance(problem, FoodSearchProblem):
        # the state includes a grid of where the food is (problem isn't ter)
        position, food_grid = state
        pacman_x, pacman_y = position

        # YOUR CODE HERE (set value of optimisitic_number_of_steps_to_goal)

        optimisitic_number_of_steps_to_goal = 0
        return optimisitic_number_of_steps_to_goal
