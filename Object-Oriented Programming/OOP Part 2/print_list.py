from singlyclass import SinglyList
from nodeclass import Node



def print_list(list_head):
	SinglyList.head = list_head
	Node1 = SinglyList.head
	Node2 = "3"
	Node3 = "7"
	Node4 = "10"
	Node.content = Node2
	Node.content = Node3
	Node.content = Node4
	Node1.nextNode = Node2 

print_list("1")