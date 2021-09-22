class Tree:
    def __init__(self, tree_dict=None, directed=True):
        self.tree_dict = tree_dict or {}
        self.directed = directed
    
    # Connect Edges of parent and thier childes
    def addEdge(self, A, B, distance=1):
        self.tree_dict.setdefault(A, {})[B] = distance

    #Get childes
    def get(self, a, b=None):
        links = self.tree_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)

class Node:
    def __init__(self, node:str, parent:str):
        self.node = node
        self.parent = parent
        self.startdist = 0   # Distance to start node
        self.goaldist = 0    # Distance to goal node
        self.totalcost= 0    # Total cost
    
    # Compare nodes
    def __eq__(self, other):
        return self.node == other.node
    
    # Sort nodes
    def __lt__(self, other):
         return self.goaldist < other.goaldist

def BestFirstSearch(tree, heuristics, start, goal):
    open = []       # Create lists for open nodes 
    closed = []     #Create lists for closed nodes
    start_node = Node(start, None)      # Create a start node
    goal_node = Node(goal, None)        # Create a goal node
    open.append(start_node)             # Add the start node
    
    # Loop until the open list is empty
    while len(open) > 0:
        # Sort the open list to get the node with the lowest cost first
        open.sort()
        current_node = open.pop(0)      # Get the node with the lowest cost
        closed.append(current_node)     # Add the current node to the closed list
        
        # Check if we have reached the goal, return the path
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.node + ': ' + str(current_node.startdist))
                current_node = current_node.parent
            path.append(start_node.node + ': ' + str(start_node.startdist))
            # Return reversed path
            return path[::-1]
        
        # Get neighbours
        child = tree.get(current_node.node)
        for key, value in child.items():
            # Create a child node
            child = Node(key, current_node)
            # Check if the child is in the closed list
            if(child in closed):
                continue
            # Calculate cost to goal
            child.startdist = current_node.startdist + tree.get(current_node.node, child.node)
            child.goaldist = heuristics.get(child.node)
            child.totalcost = child.totalcost

            # Check if child is in open list and if it has a lower cost value
            if(add_to_open(open, child) == True):              
                open.append(child)      # add child to open list
    # Return None, no path is found
    return None

# Check if a child should be added to open list
def add_to_open(open, child):
    for node in open:
        if (child == node and child.totalcost >= node.totalcost):
            return False
    return True

# main function
def main():
    tree = Tree()
    # create tree connections with actual distance
    tree.addEdge('S', 'A', 3)
    tree.addEdge('S', 'B', 2)
    tree.addEdge('A', 'C', 4)
    tree.addEdge('A', 'D', 1)
    tree.addEdge('B', 'E', 3)
    tree.addEdge('B', 'F', 1)
    tree.addEdge('E', 'H', 5)
    tree.addEdge('F', 'I', 2)
    tree.addEdge('F', 'G', 3)

    # Create heuristics 
    heuristics = {
        'A': 12,
        'B': 4,
        'C': 7,
        'D': 3,
        'E': 8,
        'F': 2,
        'H': 4,
        'I': 9,
        'S': 13,
        'G': 0
    }

    print("\nStarting Point is:  S")
    print("\nGoal Node is:  G\n")

    # Run search algorithm
    path = BestFirstSearch(tree, heuristics, 'S', 'G')
    print(path)     # print path with distance
    final_path = []
    for i in path:
        j = i[0]
        final_path.append(j)
    print("\nFinal Path of Best First Search: ", " --> ".join(final_path))  # print final path


if __name__ == "__main__": main()
