from linked_list import __version__
from linked_list.linked_list import LinkedList


def test_version():
    assert __version__ == '0.1.0'


def test_linked_list():
    assert LinkedList()


def test_add_node_to_empty_list():
    ll = LinkedList()
    ll.insert('Monday')
    assert ll.head.value == "Monday"
    assert ll.head.next_ == None

def test_add_node_to_non_empty_list():
    # Head: Sunday -> Monday -> Tuesday
    ll  = LinkedList()
    ll.insert('Tuesday')
    ll.insert('Monday')
    ll.insert('Sunday')
    assert ll.head.value == "Sunday"
    assert ll.head.next_.value == 'Monday'
