from singlyclass import SinglyList
from nodeclass import Node


def print_list(list_head):
	while list_head:
		list_head = list_head.next()
		print list_head.content()


	
head = SinglyList()
node1 = Node(1)
head.add_head(node1)
node2 = Node(2)
node3 = Node(3)

print_list(head)