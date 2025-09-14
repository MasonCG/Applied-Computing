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
        """ Add value to Tree"""

        if self.root == None:
            self.root = TreeNode(value)
        else:
            node = self.root

            while True:
                if value < node.value:                  #=== new value is left of current node ===
                    if node.left == None:               # is there a value left of current Node?
                        node.left = TreeNode(value)     # if not create new node and assign it to current nodes left
                        break                           
                    else: 
                        node = node.left                # if ther is a value assign it as current node
                elif value > node.value:                #=== new value is right of current node ===
                    if node.right == None:              # is there a value to the right of current Node?
                        node.right = TreeNode(value)    # if not create new Node and assign it to current node's right
                        break                       
                    else:
                        node=node.right                 # if there is a value assign it as current Node
                else:
                    break

    def find(self, value):
        """ Find value in Tree"""

        node = self.root

        while True:
            if node == None:
                return False
            
            if node.value == value:
                return True
            
            if node.value > value:
                node = node.left

            if node.value < value: 
                node = node.right

    def items(self):
        """ returns a list that holds values in order"""

        value_list = []
        self._inorder_trav(self.root, value_list)

        return value_list
        
    def _inorder_trav(self, node, value_list):
        """ recursive funtion to add nodes in order to a list"""

        if node == None:
            return
        
        # traverse to the left
        self._inorder_trav(node.left, value_list)
        
        # adds own self
        value_list.append(node.value)

        # traverse to the right
        self._inorder_trav(node.right, value_list)


