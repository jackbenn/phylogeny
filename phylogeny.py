

class Tree:
    def __init__(self, root):
        self.root = root
        self.node_dict = {}

    def add_node(self, node):
        self.node_dict[node.name] = node
        for child in node.children:
            self.add_node(child)

    def __get_item__(self, name):
        return self.node_dict[name]

    def __contains__(self, name):
        return name in self.node_dict

    def update_node(self, node, parent):



class Node:
    def __init__(self, name, level=None, description=None):
        self.children = []
        self.parent = None
        self.name = name
        self.level = level
        self.description = description

    def add_clade(self, parent):

        assert
