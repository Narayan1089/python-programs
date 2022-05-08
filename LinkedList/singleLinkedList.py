class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index = index+1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    def traverse(self):
        if self.head == None:
            print("Empty")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def search(self, nodeValue):
        if self.head == None:
            return "Empty"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The value does not exist"

    def delete(self, location):
        if self.head == None:
            print("Empty")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next


sl = SLL()
sl.insertSLL(1, 1)
sl.insertSLL(2, 1)
sl.insertSLL(3, 1)
sl.insertSLL(4, 1)

sl.insertSLL(6, 4)
sl.insertSLL(7, 0)
print([node.value for node in sl])

# sl.traverse()

# print(sl.search(0))

sl.delete(4)
print([node.value for node in sl])
