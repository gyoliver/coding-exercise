class MyTree:
    
    ## A traditional rooted tree object.
    ## No enforcement of tree structure is performed (i.e., a MyTree object can
    ## be instantiated with cycles).
    
    ## Constructor
    def __init__ (self, root_node, nodes):
        self.root_node = root_node
        self.nodes = nodes
    
    ## String representation
    def __str__(self):
        node_list = []
        for node in self.nodes:
            node_list.append(node.name)
        return "MyTree object:\n\troot_node: '" + str(self.root_node.name) + \
                "'\n\tnodes: " + str(node_list)
   
    ## Functions
    def find_node(self, search_name):

        ## Searches for a MyNode object with the name search_name in a MyTree object.  Returns
        ## the node if found, returns None otherwise.  This function and visit_node together
        ## implement a classic depth-first search.  This function initiates the searching of 
        ## each tree in a forest.
        
        visited_nodes = {}
        ## Saves names of visited nodes.  Since Python passes a reference to the
        ## list when a new object isn't saved to the variable, there's no need
        ## to return visited_nodes from calls to visit_node, below.
        
        return_node = None
        i = 0
        print("\nNodes visited:")
        while i < len(self.nodes):

            current_node = self.nodes[i];

            if current_node.name not in visited_nodes: 
                return_node = self.visit_node(current_node, visited_nodes, search_name)
                if return_node is not None:
                    break
            
            i += 1

        ## If the named node isn't found, return None.
        return return_node

    def visit_node(self, node, visited_nodes, search_name):
        
        ## Works with function find_node to find a MyNode object of a particular
        ## name in a MyTree object.  This function effects recursive exploration
        ## of the MyNode object "node"'s children.
        
        print("\t" + node.name)
        visited_nodes[node.name] = True
        
        ## Return the current MyNode object if its name matches search_name.
        if node.name == search_name:
            return node
        
        ## Otherwise recursively search for the node.
        i = 0
        while i < len(node.children):
            if node.children[i].name not in visited_nodes:
                
                ## Recursively call visit_node if child node hasn't been visited.
                return self.visit_node(node.children[i], visited_nodes, search_name);
            
            i += 1

        return None
    
class MyNode:
    
    ## MyNode class.  Each node has a String name and an array containing
    ## the names of other children MyNode objects.
    
    ## Constructor
    def __init__(self, name, children):
        self.name = name
        self.children = children
    
    ## String representation
    def __str__(self):
        node_list = []
        for node in self.children:
            node_list.append(node.name)
        return "MyNode object:\n\tname: " + self.name + \
                "\n\tchild nodes: " + str(node_list)
    
    ## Getters/setters
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
        
    def get_children(self):
        return self.children
    
    def set_children(self, node_array):
        self.children = node_array
