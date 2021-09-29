

class Tree:
    def __init__(self):
        self.root = Node('',
                         level='',
                         description='all life')
        self.node_dict = {'': self.root}

    def add_node(self, node):
        self.node_dict[node.name] = node
        for child in node.children:
            self.add_node(child)
        # find parent and add

    def __getitem__(self, name):
        return self.node_dict[name]

    def __setitem__(self, name, value):
        self.node_dict[name] = value

    def __contains__(self, name):
        return name in self.node_dict

    def update_node(self, node, parent):
        pass

    def load_nodes(self, file):
        # format:
        # name, parent, level, description
        
        for line in file:
            name, parent, level, description = line.split(',', maxsplit=4)
            if parent in self:
                node = Node(name=name, level=level, description=description)
                node.parent = self[parent]
                node.parent.children.append(node)
                self[name] = node
            
        #self.add_node(node)
        
    #def __str__(self):


class Node:
    def __init__(self, name, level=None, description=None):
        self.children = []
        self.parent = None
        self.name = name
        self.level = level
        self.description = description

    def to_string(self, offset=''):
        string = offset + self.name + '\n'
        for child in self.children:
            string += child.to_string(offset + '  ')
        return string
    
    def __str__(self):
        return self.to_string()

    def add_clade(self, parent):

        pass


if __name__ == '__main__':
    tree = Tree()
    with open('test.csv') as file:
        tree.load_nodes(file)
    
    print(tree.root)
