class TreeNode(object):
    def __init__(self, version, typeId, value=0, children=None):
        self.version = version
        self.type = typeId
        self.value = value
        self.children = []
        if children:
            for child in children:
                self.add_child(child)

    def add_child(self, child):
        assert isinstance(child, TreeNode)
        self.children.append(child)

    def plot(self):
        strout = '{}(v{})'.format(self.type, self.version)
        # print(strout)
        for child in self.children:
            # print(child.type)
            strout += '\n    --> ' + child.plot()
        return strout
