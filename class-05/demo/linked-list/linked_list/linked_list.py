class Node:
    """
    This is the Node Class
    """

    def __init__(self, value, next_=None):
        """
        This is my initialize of the Node
        """
        self.value = value
        self.next_ = next_

    def __repr__(self):
        return f"{self.value} : {self.next_}"


class LinkedList:
    """
    This is my Class LinkedList
    """

    def __init__(self):
        """
        This is my initialize of LinkedList
        """
        self.head = None

    def insert(self, value):
        """
        This is my insert
        :return:
        """

        node = Node(value)
        # self.head = Node(value, self.head)
        if self.head is not None:
            node.next_ = self.head
        self.head = node

#
ll = LinkedList()
print(ll)
#
print(ll.insert('Monday'))
print(ll.head)





