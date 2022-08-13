# A simple Python program to find the top view of a binary tree

class newNode:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.hd = 0

# Function to print top view of a BT
def topview(root):
 
    if(root == None):
        return
    q = []
    m = dict()
    hd = 0
    root.hd = hd
    q.append(root)
 
    while(len(q)):
        root = q[0]
        hd = root.hd
        if hd not in m:
            m[hd] = root.data
        if(root.left):
            root.left.hd = hd - 1
            q.append(root.left)
 
        if(root.right):
            root.right.hd = hd + 1
            q.append(root.right)
 
        q.pop(0)

    for i in sorted(m):
        print(m[i], end="")


# Driver code
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.right = newNode(4)
root.left.right.right = newNode(5)
root.left.right.right.right = newNode(6)
print("Following are nodes in top-view of Binary Tree")
topview(root)