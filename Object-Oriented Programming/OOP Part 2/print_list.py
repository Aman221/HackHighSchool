from singlyclass import SinglyList
from nodeclass import Node


def print_list(list_head):
	lst = iter(list_head)

	for x in range(3):
		print(next(lst))

	
head = SinglyList()
head.add_head(Node(1))
head.add_head(Node(2))

head.add_head(Node(3))
print_list(head)