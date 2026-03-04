class Node: #class Node which contains all the data
    def __init__ (self, data): #the init function which saves all the data parameters within the class
        self.data = data #where the numbers are initially stored
        self.left = None #left of the tree, starting with None because empty
        self.right = None #right of the tree, starting with None because empty
        
def tree_sort(node, val, path="root"): #the function with three parameters, node which passes through the root, val which passes through user input, with the starting point set to the root
    if node is None: #this is to check in the recursion when the bottom of the tree is hit. when the bottom is hit, it places the value and prints
        print(f"{val} has been added to {path}")
        return Node(val) #this stops the recursion once it finds the right place to put the value
    if val < node.data: #if the second input is less than the first input, or if the value is less than the root
        node.left = tree_sort(node.left, val, path + f" -> to the left of {node.data}") #node.left is defined, node becomes node.left, value is inputted in, passes the string down to the next call, and states where it was added
    elif val > node.data: #if the second input is more than the first input, or if value > root
        node.right = tree_sort(node.right, val, path + f" -> to the right of {node.data}") #node.right is the same as node.left just opposite direction
    else:
        print(f"{val} is already on the tree") #if the number already exists, don't add it (because tree's cant take duplicates)
    return node

root_val = input("Enter root number (or q to quit): ") #users first input becomes root
if root_val == "q": #if the input is q, stop
    quit()
root = Node(int(root_val)) #converts input to root, calls the class Node for storage

while True: #while loop keeps the program running. This is put after the first input because if it was not, the user would have to enter a new root every time and the program would just perpetually restart
    val = input("Enter a number (or q to quit): ") #second input becomes val
    if val == "q": #same quit statement as above
        break
    tree_sort(root, int(val)) #calls the function above 



     













    
# root = Node(10)
# nodeA = Node(5)
# nodeB = Node(20)
# nodeC = Node(3)
# nodeD = Node(7)

# root.left = nodeA
# root.right = nodeB
# root.left.left = nodeC
# root.left.right = nodeD



# def add(node):
#     if node is None:
#         return 0
#     return node.data + add(node.left) + add(node.right)

# def multiply(node):
#     if node is None:
#         return 1
#     return node.data * multiply(node.left) * multiply(node.right)

# def divide(node):
#     if node is None:
#         return 1
#     return node.data / divide(node.left) / divide(node.right)

# def subtract(node):
#     if node is None:
#         return 0
#     return node.data - subtract(node.left) - subtract(node.right)



# print(add(root))
# print(multiply(root))
# print(divide(root))
# print(subtract(root))