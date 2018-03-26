from mytree import MyTree, MyNode

def main(search_name):
    
    ## Searches for the node named search_name in the instantiated MyTree object using
    ## MyTree function find_node.  Prints information about the node if found,
    ## as well as names of nodes visited during the search.
    
    ## Instantiate nodes
    e1 = MyNode("E1", [])
    find_me = MyNode("FindMe", [])
    c1 = MyNode("C1", [])
    d1 = MyNode("D1", [e1])
    b1 = MyNode("B1", [find_me])
    b2 = MyNode("B2", [c1])
    a1 = MyNode("A1", [d1])
    a2 = MyNode("A2", [b1, b2])
    start = MyNode("Start", [a1, a2])

    ## Instatiate tree
    tree_nodes = [start, a1, a2, d1, b1, b2, e1, find_me, c1]
    my_tree = MyTree(start, tree_nodes)
    
    ## Find the node named search_name
    target_node = my_tree.find_node(search_name)
    
    ## If found, return node.  Otherwise return null.
    ## In either case, print result.
    if target_node:
        print("\nThe node named " + search_name + " was found.")
        print(target_node)
    else:
        print("\nNo node named " + search_name + " was found.")
    
if __name__ == "__main__":
    
    search_name = "FindMe"
    
    main(search_name)