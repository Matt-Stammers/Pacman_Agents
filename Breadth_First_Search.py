# Ok so here is one possible implementation of the BFS algorithm:

# First function starts by working out if a path exists:

# 1) Define path_exists function to see if a path exists first. Not this function will only return True if there is. That's all.

def path_exists(P, node1, node2):
    """
    This function checks whether a path exists between two nodes (node1, node2) in graph P = Pacman.
    """
    visited_nodes = set()
    
    # Initialize the queue of cells to visit with the first node: queue
    queue = [node1]
    
    # Iterate over the nodes in the queue
    for node in queue:
    
        # Get neighbors of the node
        neighbors = P.neighbors(node) 
        
        # Check to see if the destination node is in the set of neighbors
        if node2 in neighbors:
            print('Path exists between nodes {0} and {1}'.format(node1, node2))
            return True
            break
            
# 2) ok so now in order to compute the shortest path we can add a list of currently visited nodes            
            
def path_exists(P, node1, node2):
    """
    This function checks whether a path exists between two nodes (node1, node2) in graph P = Pacman.
    """
    visited_nodes = set()
    queue = [node1]
    
    for node in queue:  
        neighbors = P.neighbors(node)
        if node2 in neighbors:
            print('Path exists between nodes {0} and {1}'.format(node1, node2))
            return True
            break
        
        else:
            # Add current node to visited nodes
            visited_nodes.add(node)
            
            # Add neighbors of current node that have not yet been visited
            queue.extend([n for n in neighbors if n not in visited_nodes])
            
# 3) ok so now we just need to add return False if no path can be reached after the last leaf is explored.

def path_exists(P, node1, node2):
    """
    This function checks whether a path exists between two nodes (node1, node2) in graph P = Pacman.
    """
    visited_nodes = set()
    queue = [node1]
    
    for node in queue:  
        neighbors = P.neighbors(node)
        if node2 in neighbors:
            print('Path exists between nodes {0} and {1}'.format(node1, node2))
            return True
            break

        else:
            visited_nodes.add(node)
            queue.extend([n for n in neighbors if n not in visited_nodes])
        
        # Check to see if the final element of the queue has been reached
        if node == queue[-1]:
            print('Path does not exist between nodes {0} and {1}'.format(node1, node2))

            # Place the appropriate return statement
            return False
