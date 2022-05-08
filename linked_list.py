from turtle import pos, position


class Node:
    """
    An object for storing a single node of a linked list
    models two attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data): #constructor
        self.data = data
 

    def __repr__(self):
        return "Node data: %s>" % self.data  

class LinkedList:

    """
    Singly linked list
    """

    def __init__(self):
        self.head = None  

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Returns the number of nodes in the list
        Takes O(n) time
        """
        current = self.head
        count = 0

        while current:
            count +=1
            current = current.next_node

        return count    

    def add(self, data):
        """
        Adds new Node containing data at head of the list
        Takes O(1) time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node   


    def node_at_index(self,index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1

            return current     
