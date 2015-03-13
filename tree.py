o = object
class TreeNode(o):
    """
    Represents a Node of the Tree
    A Node will have some value and a list of children.
    Each child in turn would have a value and a list of children.
    A child could have no children too.
    """

    def __init__(self, value=None):
        self.value = value
        self.children = []

    def __iter__(self):
        return iter(self.children)

    def add_child(self, tree_node):
        self.children.append(tree_node)

    def print_tree_node(self, spaces=0):
        preceded = " " * spaces
        #print preceded + str(self.value)
        spaces += 1
        for child in self.children:
            child.print_tree_node(spaces)

    def return_tree_node(self, spaces=0, created_list=[]):
        preceded = " " * spaces
        created_list.append((preceded, self))
        spaces += 1
        for child in self:
            child.return_tree_node(spaces, created_list)
        return created_list

    def do_depth_first(self):
        yield self
        for each in self.children:
            # This works with python3
            yield from each.do_depth_first()



class Tree(o):
    """
    Represents a Tree of TreeNode(s)
    A Tree only keeps track of root TreeNode
    From root TreeNode we can reach it's children and subsequent children of children
    and so on.
    """

    def __init__(self, root):
        self.root = root

    @classmethod
    def create_tree(cls, root=None):
        return cls(root)

    def print_tree(self):
        self.root.print_tree_node()

    def add_node(self, childe_value, parent_node=None):
        if parent_node is None:
            parent_node = self.root
        node = TreeNode(childe_value)
        parent_node.add_child(node)
        


language = TreeNode("Language")
tree = Tree.create_tree(language)
python = TreeNode("python")
java = TreeNode("java")
javascript = TreeNode("javascript")
language.add_child(python)
language.add_child(javascript)
language.add_child(java)
tree.add_node("classpath", java)
tree.add_node("iteration", python)

for each in language.return_tree_node():
    print(each[0] + "" + each[1].value)