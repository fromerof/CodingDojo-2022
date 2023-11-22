from multiprocessing.sharedctypes import Value


class SLNode:
    def __init__(self,value):
        self.val = value
        self.next = None
    

class SList:
    def __init__(self):
        self.head = None
    def addToFront(self,val):
        new_node = SLNode(val)
        new_node.next = self.head
        self.head = new_node
        return self
    def printValue(self):
        runner = self.head
        while (runner != None):
            print(runner.val)
            runner = runner.next
        return self
    def addToBack(self,val):
        if self.head == None:
            self.addToFront(val)
            return self
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self
    def removeFromFront(self):
        if self.head != None:
            self.head = self.head.next
            return self

    def removeFromBack(self):
        if self.head == None: #para 1 node
            return self
        elif self.head.next == None:
            self.head = None
            return self
        else:
            runner = self.head    
            while (runner.next.next != None):
                runner = runner.next
            runner.next = None
        return self
    def remove_val(self,val):
        pass





my_list = SList()
my_list.addToFront("Jackson").addToFront("filip").addToBack("juan").removeFromBack()
my_list.printValue()
my_list2 = SList()
