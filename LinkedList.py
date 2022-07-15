class Node:


    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:


    def __init__(self):

        self.headval = None


    def _iter__(self):

        currentNode = self.headval
        while currentNode is not None:
            yield node
            node = node.next

    def add_last(self, node):

        if self.headval is None:

            self.headval = node
            return
        for current_node in self:
            pass
        current_node.next = node

        
    def AtEnd(self, newdata):
          NewNode = Node(newdata)
          if self.headval is None:
             self.headval = NewNode
             return
          laste = self.headval
          while(laste.nextval):
            laste = laste.nextval
          laste.nextval=NewNode
      

list1 = SLinkedList()
list1.headval = Node("Mon")

e2 = Node("Tue")
e3 = Node("Wed")

list1.headval.nextval = e2


list1.add_last(Node("Shit"))



