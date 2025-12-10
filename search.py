# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).




"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in search_agents.py).
"""

from builtins import object
from game import Directions
import util
import heuristics

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import NamedTuple
    class Transition(NamedTuple):
        state: tuple[int,int]
        action: str
        cost: float



class SearchProblem(object):
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def get_start_state(self) -> tuple[int,int]:
        """
        Returns the start state for the search problem.
        """
        util.raise_not_defined()
        return (0, 0)
   
    def is_goal_state(self, state: tuple[int,int]) -> bool:
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raise_not_defined()

    def get_successors(self, state: tuple[int,int]) -> list[Transition]:
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, step_cost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'step_cost' is
        the incremental cost of expanding to that successor.
        """
        util.raise_not_defined()

    def get_cost_of_actions(self, actions:list[str]) -> float:
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raise_not_defined()



def tiny_maze_search(problem: SearchProblem) -> list[str]:
    """
    Returns a sequence of moves that solves tiny_maze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tiny_maze.
    """

    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]

def example_maze_search(problem: SearchProblem) -> list[str]:
    # What does this function need to return?
    #     list of actions (actions shown below) that reaches the goal
    #
    # What data is available?
    #     start_state = problem.get_start_state() # returns a string
    #
    #     problem.is_goal_state(start_state) # returns boolean
    #
    #     transitions = problem.get_successors(start_state)
    #     transitions[0].state
    #     transitions[0].action
    #     transitions[0].cost
    #
    #     print(transitions) # would look like the list-of-lists on the next line
    #     [
    #        [ state=(34, 15), action=South, cost=1, ],
    #        [ state=(33, 16), action=West, cost=1, ]
    #     ]
    #
    # Explaination:
    #     coordinate 34,15 is reachable from the start by walking south
    #     coordinate 33,16 is reachable from the start by walking west
    #     in the example, the cost to move to either coordinate is 1

    start_state = problem.get_start_state()
    transitions = problem.get_successors(start_state)
    print(transitions)
    example_path = [transitions[0].action]
    return example_path

def depth_first_search(problem: SearchProblem) -> list[str]:
    # Du behöver en datastruktur för att hålla koll på upptäckta noder som du inte än har besökt
    # Du kan använda en Stack som finns i util.py
    # När du gör stack.push(node) läggs en nod till längst upp på stacken
    # När du gör node = stack.pop() plockar du ut den senaste tillagda noden

    stack = TODO  # skapa en util.Stack()

    # Du behöver en datastruktur för att hålla koll på redan upptäckta noder
    # så att du inte lägger till samma nod flera gånger. Du kan använda lista eller set.
    # lista ut hur man gör en lista i python
    # ... hehehe

    discovered = TODO  # skapa en lista

    # För att hålla koll på vilken väg din sökning tog behöver du alltså spara undan
    # för varje nod, vem som upptäckte den och vilken rörelse som rör roboten från
    # "upptäckare" till "den upptäckta"

    # En map, key-value store, eller dictionary som det heter i python är bra
    # Då kan "nyckeln" vara den "upptäckta noden", och för varje "upptäckt nod"
    # kan värdet vi sparar vara "upptäckaren" och "rörelsen"
    # Två värden kan slås ihop till en variabel med hjälp av en tupel.

    # t.ex.

    # discovered_path["b"] = ("a","north")
    # indikerar att vår dictionary, discovered_path (som också skulle kunna kallas parents)
    # har sparat informationen att för att nå noden "b" så kan vår robot gå "north" från "a"

    discovered_path = TODO  # skapa en dictionary

    # lägg till startnoden till stacken
    # klassen problem har en funktion för att hämta startnoden.

    start = problem.TODO
    stack.push(TODO)

    # lägg till startnoden till de upptäckta noderna

    discovered.TODO

    # indikera att det inte finns någon nod som används för att ta oss till startnoden

    discovered_path[TODO] = (
        None,
        None,
    )  # startnoden har alltså ingen (upptäckare,rörelse) tupel

    while stack is not empty:  # TODO kolla i util.py vilka funktioner stack har.
        node = TODO  # hämta ut senaste tillagda noden på stacken (SÅ FUNGERAR DFS!)

        # utforska grannar om vi inte nått målet
        if node is not goal:
            # för varje hittad granne, hitta:
            # namnet på grannen, rörelsen för att ta sig dit, kostnaden att ta sig dit
            # Kolla på klassen SearchProblem.
            # Vad heter funktionen för att hitta alla grannar till en nod?
            for neighbor, action, cost in problem.TODO(node):
                if neighbor not in discovered:
                    # lägg till grannen som upptäckt
                    discovered.TODO
                    # lägg till vilken nod som upptäckte grannen, och via vilken rörelse
                    discovered_path[neighbor] = (node, action)
                    # lägg till grannen på stacken
                    stack.TODO

        else:  # målet funnet!!
            # Dags att hämta alla åtgärder för att nå målet!
            path = TODO  # ny tom lista
            current = (
                node  # variabeln current håller koll på vilken nod vi "backat" till
            )
            # backa hela vägen till starten
            while current is not start:
                # för varje nod, hämta vilken nod den upptäcktes ifrån och via vilken rörelse
                parent_node, action = discovered_path[current]
                # lägg till "rörelsen" längst fram i den "path" du skapar
                path.TODO(action)
                # backa till föregående nod
                current = parent_node
            # När loopen är över har vi backat hela vägen till starten och kan ge en korrekt "path"
            return path

    # Sökningen är över utan att en nod upptäckts som är slutnoden
    raise Exception("Failed to find a solution")

def breadth_first_search(problem: SearchProblem) -> list[str]:
    # BFS använder en kö (Queue) för att hålla koll på upptäckta noder som vi inte än har besökt.
    # Detta är den stora skillnaden mot DFS!
    # En kö fungerar enligt "först in, först ut"-principen.
    # När du gör queue.push(node) läggs en nod till sist i kön.
    # När du gör node = queue.pop() plockar du ut den nod som lades till först.

    queue = TODO  # skapa en util.Queue()

    # Precis som i DFS behöver vi hålla koll på redan upptäckta noder
    # så att vi inte hamnar i en oändlig loop om det finns cykler i grafen.
    #
    #
    discovered = TODO  # skapa en lista eller ett set

    # Vi behöver också spara vägen. En dictionary är perfekt för detta,
    # där nyckeln är en nod och värdet är en tupel med (föregående_nod, åtgärd).
    # t.ex. discovered_path["b"] = ("a", "north")

    discovered_path = TODO  # skapa en dictionary

    # Börja med att lägga till startnoden i kön och markera den som upptäckt.

    start_node = problem.TODO
    queue.push(start_node)
    discovered.append(start_node)  # Lägg till i listan över upptäckta

    # Startnoden har ingen föregångare.
    discovered_path[start_node] = (None, None)

    # Sökningen fortsätter så länge det finns noder kvar att besöka i kön.
    while not queue.is_empty():
        # Hämta ut den första noden som lades till i kön (SÅ FUNGERAR BFS!)
        node = queue.pop()

        # Har vi nått målet?
        if problem.is_goal_state(node):
            # Målet är funnet! Dags att återskapa vägen.
            path = []  # Skapa en tom lista för vår väg
            current = node

            # Backa från målnoden till startnoden med hjälp av vår dictionary.
            while current != start_node:
                parent_node, action = discovered_path[current]
                # Lägg till varje åtgärd i början av listan för att få rätt ordning.
                path.insert(0, action)
                current = parent_node

            return path  # Returnera den färdiga vägen

        # Om vi inte nått målet, utforska grannarna.
        # problem.getSuccessors(node) ger oss en lista med (granne, åtgärd, kostnad).
        for neighbor, action, cost in problem.get_successors(node):
            if neighbor not in discovered:
                # Om vi hittar en ny, oupptäckt granne:
                # 1. Markera den som upptäckt.
                discovered.append(neighbor)
                # 2. Spara hur vi kom hit (från vilken nod och med vilken åtgärd).
                discovered_path[neighbor] = (node, action)
                # 3. Lägg till den sist i kön för att besöka den senare.
                queue.push(neighbor)

    # Sökningen är över utan att en nod upptäckts som är slutnoden
    raise Exception("Failed to find a solution")

def uniform_cost_search(problem: SearchProblem) -> list[str]:
    # UCS använder en prioritetskö (Priority Queue) för att alltid utforska
    # den billigaste vägen först.
    # När du gör pq.push(item, priority) läggs ett objekt till med en viss prioritet (kostnad).
    # När du gör item = pq.pop() plockar du ut objektet med LÄGST prioritet (kostnad).

    priority_queue = TODO  # skapa en util.PriorityQueue()

    # Vi behöver fortfarande hålla koll på upptäckta noder för att undvika cykler.
    # Här kan vi också passa på att spara kostnaden till noden, så vi kan uppdatera
    # om vi hittar en billigare väg. En dictionary är perfekt: {nod: kostnad}.
    discovered = TODO  # skapa en dictionary

    # Precis som tidigare sparar vi vägen i en separat dictionary.
    discovered_path = TODO  # skapa en dictionary

    # Vi behöver också hålla koll på besökta noder.
    # Algoritmen garanterar att första gången en nod besöks är det via
    # den billigaste vägen att besöka noden.
    # Men prioritetskön kommer kunna lägga till flera vägar till en nod
    # om sökningen t.ex. hittar en sämre väg innan den hittar den bästa
    #
    # Därför behöver vi se till att vi struntar i att besöka en nod som redan
    # blivit besökt. Vi kan spara besökta noder i en lista.

    visited = TODO  # skapa en lista

    # Börja med startnoden. Den har kostnad 0.
    start_node = problem.get_start_state()

    # Vi lägger till en tupel (nod, kostnad) i prioritetskön.
    priority_queue.push(start_node, 0)

    # vad är kostnaden att nå startnoden?
    discovered[start_node] = TODO

    # Samma som tidigare, startnoden har ingen "upptäckare"
    discovered_path[start_node] = (None, None)

    while not priority_queue.is_empty():
        # Hämta ut noden med lägst total kostnad hittills.
        node = priority_queue.pop()

        # Om vi redan har hittat en billigare väg till denna nod, hoppa över den.
        # Detta kan hända eftersom vi kan lägga till samma nod flera gånger i kön
        # med olika kostnader. Vi bryr oss bara om den första (billigaste) gången vi poppar den.
        if node in visited:
            continue

        # Lägg till noden i listan över besökta noder.
        visited.add(node)

        # Har vi nått målet? Då vet vi att detta är den billigaste vägen dit!
        if problem.is_goal_state(node):
            # Återskapa vägen precis som i BFS/DFS.
            path = []
            current = node
            while current != start_node:
                parent_node, action = discovered_path[current]
                path.insert(0, action)
                current = parent_node
            return path

        # Utforska grannar.
        for neighbor, action, cost in problem.get_successors(node):
            # Beräkna den nya totala kostnaden för att nå grannen via den nuvarande noden.
            new_cost = TODO  # kostnad för att nå noden (finns i discovered dict) + kostnad att nå granne

            # Om vi inte har upptäckt grannen förut, ELLER om vi har hittat en billigare väg dit:
            if neighbor not in discovered or new_cost < TODO:
                # 1. Spara (eller uppdatera) den billigaste kostnaden till grannen.
                discovered[neighbor] = TODO
                # 2. Spara (eller uppdatera) vägen till grannen.
                discovered_path[neighbor] = TODO
                # 3. Lägg till grannen i prioritetskön med den nya, låga kostnaden som prioritet.
                priority_queue.push(TODO)

    # Sökningen är över utan att en nod upptäckts som är slutnoden
    raise Exception("Failed to find a solution")

def a_star_search(problem : SearchProblem, heuristic=heuristics.your_heuristic) -> list[str]:
    # A* använder också en prioritetskö, precis som UCS.
    # Skillnaden är hur vi beräknar prioriteten för varje nod.
    # sökningen använder en funktion som argument (ovan "heuristic")
    # Den används som följer h_value = heuristic(node,problem)

    priority_queue = TODO  # skapa en util.PriorityQueue()

    # Vi behöver en dictionary för att spara den hittills billigaste kostnaden från start (g-värdet).
    # Detta är identiskt med `cost_to_reach` i UCS.
    # t.ex. g_cost["c"] = 12
    g_cost = TODO  # skapa en dictionary

    # Precis som tidigare sparar vi vägen för att kunna återskapa den på slutet.
    discovered_path = TODO  # skapa en dictionary

    # Vi behöver också hålla koll på noder vi redan har besökt,
    # för att inte göra dubbelarbete, på samma sätt som i UCS
    visited = TODO  # skapa en lista eller ett set

    # Allt börjar vid startnoden.
    start_node = problem.get_start_state()

    # Startnoden har ingen "upptäckare".
    discovered_path[start_node] = (None, None)

    # Vad är kostnaden (g-värdet) att nå startnoden från sig själv?
    g_cost[start_node] = TODO

    # Här kommer den stora skillnaden mot UCS!
    # Vi måste också beräkna den uppskattade kostnaden från start till mål (h-värdet).
    # Funktionen `heuristic` tar en nod och problemet som input.
    h_value = heuristic(TODO, problem)

    # A*s prioritet är f-värdet = g-värdet + h-värdet.
    f_value = g_cost[start_node] + h_value

    # Lägg till startnoden i kön med dess f-värde som prioritet.
    priority_queue.push(TODO, TODO)

    while not priority_queue.is_empty():
        # Hämta ut noden med lägst f-värde (bäst kombination av redan rest och uppskattat kvar).
        node = priority_queue.pop()

        # Om vi redan har besökt denna nod, hoppa över den.
        if node in visited:
            continue

        # Lägg till noden i listan över besökta noder.
        visited.add(node)

        # Om vi poppar målet har vi hittat den optimala lösningen (om heuristiken är "tillåten").
        if problem.is_goal_state(node):
            # Återskapa vägen precis som i de andra algoritmerna.
            path = []  # ny tom lista
            current = node
            # backa hela vägen till starten
            while current != start_node:
                # för varje nod, hämta vilken nod den upptäcktes ifrån och via vilken rörelse
                parent_node, action = discovered_path[current]
                # lägg till "rörelsen" längst fram i den "path" du skapar
                path.insert(0, action)
                # backa till föregående nod
                current = parent_node
            # När loopen är över har vi backat hela vägen till starten och kan ge en korrekt "path"
            return path

        # Utforska grannar.
        # Vad heter funktionen för att hitta alla grannar till en nod?
        for neighbor, action, step_cost in problem.TODO(node):
            # Beräkna grannens nya g-värde (kostnad från start) om vi går via den nuvarande noden.
            new_g_cost = g_cost[TODO] + step_cost

            # Om vi inte sett denna granne förut, ELLER om vi hittat en ny, billigare väg dit:
            if neighbor not in g_cost or new_g_cost < g_cost[neighbor]:
                # 1. Spara (eller uppdatera) det nya, lägre g-värdet.
                g_cost[neighbor] = new_g_cost

                # 2. Spara (eller uppdatera) vägen som ledde hit.
                discovered_path[neighbor] = (TODO, TODO)

                # 3. Beräkna det nya f-värdet för grannen.
                new_h_value = heuristic(TODO, problem)
                new_f_value = TODO  # f(n) = g(n) + h(n)
                # 4. Lägg till grannen i kön med dess nya f-värde som prioritet.
                priority_queue.push(TODO, TODO)

    # Sökningen är över utan att en nod upptäckts som är slutnoden
    raise Exception("Failed to find a solution")


# Abbreviations
bfs = breadth_first_search
dfs = depth_first_search
astar = a_star_search
ucs = uniform_cost_search
ems = example_maze_search
