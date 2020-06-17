class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):

        self.head = Node(value, self.head)


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
