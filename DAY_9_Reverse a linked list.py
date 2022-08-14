# A simple Python program to find the top view of a binary tree

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class contains a Node object
class LinkedList:

    #Function to initialize head
    def __init__(self):
        self.head = None

    # Function to print contents of the linked list
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next

    # Function to insert a new node at the beginning
    def insert(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Function to reverse linked list iteratively
    def reverse_Iteratively(self):
        prev = None
        curr = self.head    
        while(curr is not None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev


llist = LinkedList()
llist.insert(5)
llist.insert(4)
llist.insert(3)
llist.insert(2)
llist.insert(1)
llist.printList() # Printing original linked list 1->2->3->4->5
print("\n")
llist.reverse_Iteratively() # Reversing via iterative method
llist.printList()