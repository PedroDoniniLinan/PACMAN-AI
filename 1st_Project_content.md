# *Subject* : Search

**Problem** : Pacman agent needs to find paths through his maze world, both to reach a particular location and to collect food efficiently 
wtih general search algorithms and apply them to Pacman scenarios.

All algorithms can be found in the "searchAgents.py" and "search.py" files.

## **Reflex agent**

The simplest agent in searchAgents.py which always goes West (a trivial reflex agent). 

**Commands**

* python pacman.py --layout testMaze --pacman GoWestAgent
* python pacman.py --layout tinyMaze --pacman GoWestAgent

## **Depth First Search (DFS)**

**Commands**

* python pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch
* python pacman.py -l tinyMaze -p SearchAgent
* python pacman.py -l mediumMaze -p SearchAgent
* python pacman.py -l bigMaze -z .5 -p SearchAgent

## **Breadth First Search (BFS)**

**Commands**

* python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
* python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
* python eightpuzzle.py

## **Uniform Cost Search (UCS)**

**Commands**

* python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
* python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
* python pacman.py -l mediumScaryMaze -p StayWestSearchAgent

## **A star Search**

**Commands**

* python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

## **Passing by all corners with minimum cost path**

**Commands**

* python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
* python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
* python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5

## **Eating all dots**

### **Optimal solution**

**Commands**

* python pacman.py -l testSearch -p AStarFoodSearchAgent
* python pacman.py -l trickySearch -p AStarFoodSearchAgent

### **Glutton algorithm**

**Commands**

* python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5 
