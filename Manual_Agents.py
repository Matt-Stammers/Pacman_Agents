# These are the very basic first level search agents in the Berkeley PacMan AI Course (CS188)

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]
    
def crazyAgent(problem):
    """
    This Agent takes some crazy turns whilst exploring tinyMaze.
    He can also detect the start State, Goal State and Successors but doesn't actually make use of them yet.
    """
    from game import Directions
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    return  [s, s, w, s, w, w, n, n, n, s, s, s, w, s, w]
