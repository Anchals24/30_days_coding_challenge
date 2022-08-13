# A simple Python program for finding the next greater element

# Brute-Force Method: Using 2 for loops
arr = [11, 13, 21, 3]
for i in range(0, len(arr), 1):
    next = -1
    for j in range(i+1, len(arr), 1):
        if arr[i] > arr[j]:
            next = arr[j]
            break
    print(str(arr[i]) + " -- " + str(next))
    


# Using Stacks

def createStack(): # function for stack creation
    stack = []
    return stack  
  
def isEmpty(stack): # function for checking if stack is empty
    return len(stack) == 0
  
def push(stack, x): # function for pushing element into stack
    stack.append(x)
  
def pop(stack):     # function for popping element out of stack
    return stack.pop()

s = createStack()
element = 0
push(s, arr[0]) # push the first element to stack

for i in range(1, len(arr), 1):
        next = arr[i]
        if isEmpty(s) == False:
            element = pop(s)        # if stack is not empty, then pop an element from stack
            while element < next:   # If the popped element is smaller than next, then print the pair and keep popping while elements are smaller and stck isn't empty
                print(str(element) + " -- " + str(next))
                if isEmpty(s) == True:
                    break
                element = pop(s)
                
            if element > next:  # If element is greater than next, then push the element back
                push(s, element)
            push(s, next)

while isEmpty(s) == False:      # elements in stack which do not have the next greater element print -1 for them 
        element = pop(s)
        next = -1
        print(str(element) + " -- " + str(next))