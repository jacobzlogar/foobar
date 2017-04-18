def tree_index(top_node, value, node_below):

    node_below = node_below/2
    node_right = top_node - 1
    node_left = top_node - 1 - node_below
    
    if (node_right == value or node_left == value):
        return top_node
    else:
        if value <= node_left:
            return tree_index(node_left, value, node_below)
        else:
            return tree_index(node_right, value, node_below)

def answer(h, q):

    top_node = (2**h) - 1
    result = []

    for index in q:
        if index < top_node and index >= 1:
            result.append(tree_index(top_node, index, top_node - 1))
        else:
            result.append(-1)

    return result
