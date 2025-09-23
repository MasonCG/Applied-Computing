# tree class


class Node(object):
    def __init__(self, text:str, yes=None, no=None):
        self.yes = yes
        self.no = no
        self.text = text

class DecisionTree(object):
    def __init__(self):
        self.root = None


    def nextNode(self, prevNode: Node =Node(text=None), decision : str =None):
        """Takes the previous node and goes to the next node in the tree based on the given decision
            Remember: animal nodes are on the end of the tree they will NOT have a nextNode
            prevNode: "Node instance" previous node in tree
            decision: "String" Answer to previous nodes question
        """

        # raising parameter errors 

        if (not isinstance(prevNode, Node)):
            raise TypeError('preNode must be an instance of the Node class.')
        if (not isinstance(decision, str)):
            raise TypeError('decision must be a string of "Y" or "N".')
        if (decision != 'Y' or decision != 'N'):
            raise ValueError('decision must be a string of "Y" or "N" ')
        

        # if node not given start at self.root
        if not preNode.text:
            preNode = self.root

        if (decision == "Y"):
            return prevNode.yes
        else:
            return prevNode.no
        
    def addNode(self, prevAnimalNode:Node, text: str, q=True: bool):
        """
            Takes given text and adds a new Node of type q. 
            prevAnimalNode: "Node instance" the animal node that was guessed wrong. 
            text: "str" of question or animal
            q: "boolean" tells wheather or not node is a question 
        """

        # raising parameter errors

        if (not isinstance(prevAnimalNode, Node)):
            raise TypeError("'prevAnimalNode' must be an animal Node instance")
        if (prevAnimalNode.yes != None or prevAnimalNode.no != None):
            raise ValueError('"prevAnimalNode" must be an animal not a decision Node instance')
        if (not isinstance(text, str)):
            raise TypeError("'text' must be of type string.")
        if (not isinstance(q, bool)):
            raise TypeError('"q" must be of type boolean.')
        

        


