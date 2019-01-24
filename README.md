# PACMAN-AI
Several AI mini-projects with Pacman.

To run the algorithms:
1. Open command-line terminal;
2. Go to the desired mini-project directory;
3. Type the desired test.

---------------------------------  1st Project  ---------------------------------

-Simple agents
python pacman.py --layout testMaze --pacman GoWestAgent
python pacman.py --layout tinyMaze --pacman GoWestAgent

-Finding minimum path

  *DFS
  
  python pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch
  
  python pacman.py -l tinyMaze -p SearchAgent
  
  python pacman.py -l mediumMaze -p SearchAgent
  
  python pacman.py -l bigMaze -z .5 -p SearchAgent
  
  *BFS
  
  python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
  
  python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
  
  python eightpuzzle.py
  
  *UCS
  
  python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
  
  python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
  
  python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
  
  *A* search
  
  python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
 
-Passing by all corners with minimum cost path

python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem

python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem

python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5

-Eating all dots

  - Optimal solution
  
  python pacman.py -l testSearch -p AStarFoodSearchAgent
  
  python pacman.py -l trickySearch -p AStarFoodSearchAgent
  
  - Glutton algorithm
  
  python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5 

  
