# A simple Python program for insertion of element in a linked list

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

	# Function to insert a new node at the beginning
	def insertFront(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
	
	# Function to insert a new node at the end
	def insertEnd(self, new_data):
		new_node = Node(new_data)
		if self.head is None:       # If linked list is empty make a new node
			self.head = new_node
			return
		tail = self.head # Else traverse till the last node
		while (tail.next):
			tail = tail.next
		tail.next = new_node

	# Function to insert a new node at the middle    
	def insertMiddle(self, new_data):
		temp = self.head
		cnt = 0 	# Calculating the length of linked list
		while (temp):
			cnt += 1
			temp = temp.next
		mid = cnt//2    # Identifying the mid node
		new_node = Node(new_data)
		cnt = 1
		temp = self.head
		while (cnt != mid):
			cnt+=1
			temp = temp.next
		new_next = temp.next
		temp.next = new_node
		new_node.next = new_next
        

#Creating a linked list with 3 nodes
llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)
llist.head.next = second
second.next = third 
llist.printList() # 1 -> 2 -> 3
print("\n")

#Inserting element at the beginning of the linked list
llist.insertFront(6)  # 6 -> 1 -> 2 -> 3
llist.printList() 
print("\n")

#Inserting element at the middle of the linked list
llist.insertMiddle(7) # 6 -> 1 -> 7 -> 2 -> 3
llist.printList() 
print("\n")

#Inserting element at the end of the linked list
llist.insertEnd(8)    # 6 -> 1 -> 7 -> 2 -> 3 -> 8
llist.printList() 