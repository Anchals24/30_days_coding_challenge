# A simple Python program for deletion of element in a linked list

# Node class
class Node:

	# Function to initialise the node object
	def __init__(self, data):
		self.data = data
		self.next = None


# Linked List class contains a Node object
class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	# Function to print contents of the linked list
	def printList(self):
		temp = self.head
		while (temp):
			print (temp.data)
			temp = temp.next

	# Function to delete node from the front of the linked list
	def deleteFront(self):
		temp = self.head
		self.head = temp.next
		temp = None
		return

	# Function to delete node from the end of the linked list
	def deleteEnd(self):
		temp = self.head
		while (temp.next.next):
			temp = temp.next
		temp.next = None

	# Function to delete node from the middle of the linked list
	def deleteMiddle(self):
		temp = self.head
		cnt = 0 # Calculating the length of linked list
		while (temp):
			cnt += 1
			temp = temp.next
		mid = cnt//2 # Identifying the mid node
		cnt = 1
		temp = self.head
		while(cnt != mid):
			cnt += 1
			temp = temp.next
		temp.next = temp.next.next

	

#Creating a linked list with 3 nodes
llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
llist.head.next = second
second.next = third
third.next = fourth 
llist.printList() # 1 -> 2 -> 3 -> 4
print("\n")

#Deleting element at the beginning of the linked list
llist.deleteFront()  # 2 -> 3 -> 4
llist.printList() 
print("\n")

#Deleting element at the end of the linked list
llist.deleteEnd() # 2 -> 3
llist.printList() 
print("\n")

#Deleting element at the middle of the linked list
llist.deleteMiddle() # 2 
llist.printList() 