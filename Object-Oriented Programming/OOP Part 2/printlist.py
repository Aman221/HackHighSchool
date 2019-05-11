class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = linked_list.head
        while node:
            yield node
            node = node.next

    def add(self, node):
        if self.head:
            self.tail.next = node
        else:
            self.head = node

        self.tail = node

linked_list = SinglyLinkedList()
linked_list.add(Node('Alice'))
linked_list.add(Node('Chad'))
linked_list.add(Node('Debra'))

print [node.value for node in linked_list]  # ['Alice', 'Chad', 'Debra']