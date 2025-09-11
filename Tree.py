# tree class


class TreeNode(object):
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value

class SearchTree(object):
    def __init__(self):
        self.root = None

    def add(self, value):
        """ Adds value to Tree"""

        #if root is empty, make a node put the value there and leave.
        # since the root istn empty, start with node at the root.
        # while TRUE:
            # if our value is smaller then check left brance
                # if theres nothing to the left then
                    # make a new node put the value there and leave
                    # something already to the left,
                    # so follow the branch by updating the node.
            # else if our value is larger then check right brance
                # if there snothing to the right hen
                    #make a new node put the value ther and leave
                # something already to the right
                    # so follow the bracnh by updating the node
            # else our value is equal
                # ignore it (equal values are discarded) and leave.

        if self.root == None:
            self.root = TreeNode(value)
        else:
            node = self.root
            while True:
                if value < node.value:
                    if node.left == TreeNode(value):
                        break
                else: 


    def checkValue(self, value)