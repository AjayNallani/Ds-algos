class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def AtBeginning(self, newdata):
        new = Node(newdata)
        new.next = self.head
        self.head = new
    
    def AtEnd(self, newdata):
        new = Node(newdata)
        if self.head is None:
            self.head = new
            return 
        laste = self.head
        while(laste.next):
            laste = laste.next
        
        laste.next = new
    
    def InBetween(self, middle, newdata):
        if middle is None:
            print("mentioned node is absent")
            return 
        new = Node(newdata)
        new.next = middle.next
        middle.next = new

    def RemoveNode(self, RemoveKey):
        headVal = self.head
        if headVal is not None:
            if headVal.data == RemoveKey:
                self.head = headVal.next
                headVal = None
                return 
        
        while(headVal is not None):
            if headVal.data == RemoveKey:
                break
            prev = headVal
            headVal = headVal.next 
        
        if (headVal == None):
            return 
        prev.next = headVal.next
        headval = None

    def printList(self):
        temp = self.head
        while(temp):
            print((temp.data))
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third

    llist.AtBeginning(4)
    llist.AtEnd(5)

    middle_node = llist.head.next.next

    llist.InBetween(middle_node, 7)
    llist.RemoveNode(7)

    llist.printList()