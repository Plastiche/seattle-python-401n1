from linked_list.linked_list import LinkedList, Node

def test_instance():
    ll = LinkedList()
    assert ll

def test_head():
    ll = LinkedList()
    assert ll.head == None


def test_node_instance():
    node = Node('apples')
    actual = node.value
    expected = 'apples'
    assert actual == expected


# def test_node_next():
#     apples = Node('apples')

#     bananas = Node('bananas', apples)

#     assert bananas.next.value == 'apples'

def test_insert_empty():
    ll = LinkedList()
    ll.insert('apples')
    actual = ll.head.value
    expected = 'apples'
    assert actual == expected

def test_insert_not_empty():
    ll = LinkedList()
    ll.insert('bananas')
    ll.insert('apples')
    actual = ll.head.value
    expected = 'apples'
    assert actual == expected
    assert ll.head.next.value == 'bananas'
