from graphviz import Digraph

def visualize_tree_with_graphviz(tree_nodes):
    """
    Visualizes a tree using Graphviz. Expects a list of dicts with 'id', 'parent', and 'label'.
    """
    dot = Digraph(comment='System Hierarchy')
    for node in tree_nodes:
        dot.node(node['id'], node['label'])
        if node['parent']:
            dot.edge(node['parent'], node['id'])
    dot.render('system_hierarchy_tree', view=True)  # Opens the diagram