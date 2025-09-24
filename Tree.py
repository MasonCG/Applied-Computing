# tree class


class Node(object):
    def __init__(self, text:str, yes=None, no=None):
        self.yes = yes
        self.no = no
        self.text = text

class DecisionTree(object):
    def __init__(self):
        self.root = None
        self.cur = self.root


    def nextNode(self, decision : str =None):
        """takes current node and goes to the next
            Remember: animal nodes are on the end of the tree they will NOT have a nextNode
            prevNode: "Node instance" previous node in tree
            decision: "String" Answer to previous nodes question
        """


        # raising parameter errors 
        if not isinstance(decision, str):
            raise TypeError('decision must be a string of "Y" or "N".')
        if decision == 'Y' or decision == 'N':
            pass
        else:
            raise ValueError('decision must be a string of "Y" or "N" ')
        
        # if no nodes have been added
        if not self.root:
            raise LookupError('There are no Nodes in your tree')


        if decision == "Y":
            nextNode = self.cur.yes
        else:
            nextNode = self.cur.no

        if not nextNode.no and not nextNode.yes:
            return nextNode.text
        
        self.cur = nextNode
        return False

        
    def addQuestion(self, text: str, answer: str=None, newAnimal:str=None, guessed:str=None):
        """
            Takes given text and adds a new Node of type q. 
            text: "str" of question or animal
            answer: "str" tells you answer to question
        """

        # if first item is created
        if self.root == None:
            self.root = Node(text)
            self.cur = self.root
            return

        # raising parameter errors

        if not isinstance(text, str):
            raise TypeError("'text' must be of type string.")
        if not isinstance(answer, str):
            raise TypeError("'answer' must be of type string.")
        if answer == 'Y' or answer == 'N':
            pass
        else:
            raise ValueError('answer must be a string of "Y" or "N" ')
        if not isinstance(newAnimal, str):
            raise TypeError("'newAnimal' must be of type string.")
        if not isinstance(guessed, str):
            raise TypeError("'guessed' must be of type string.")

       

        if answer == 'Y':
           newNode = Node(text, yes=Node(newAnimal), no=Node(guessed))
        else:
            newNode = Node(text, yes=Node(guessed), no=Node(newAnimal))

        if self.cur.yes.text == guessed:
            self.cur.yes = newNode
        else:
            self.cur.no = newNode
        

    def restart(self):
        self.cur = self.root
