class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if self.top:
            wanted = self.top
            self.top = self.top.next
            wanted.next = None
            return wanted.value

    def is_empty(self):
        # return self.top is None
        if self.top is None:
            return True
        else:
            return False

    def peek(self):
        if self.top is None:
            raise AttributeError('The Stack is Empty')
        else:
            return self.top.value


class Queue:


