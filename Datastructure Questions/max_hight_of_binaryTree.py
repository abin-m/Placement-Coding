# Find the Maxim depth of Binary tree

# if (A==None):
#     return 0
# else:
#     ldepth=hieght_tree(A.left)
#     rdepth=hieght_tree(A.right)

#     if (ldepth>rdepth):
#         return (1+ldepth)
#     else:
#         return(1+rdepth)


# Creating a New clss for nodes

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def hieght_tree(A):
    if (A == None):
        return 0
    else:
        ldepth = hieght_tree(A.left)
        rdepth = hieght_tree(A.right)

        if (ldepth > rdepth):
            return (1+ldepth)
        else:
            return (1+rdepth)


# Creating the binary tree

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.right = Node(7)
root.right.right = Node(6)


print(hieght_tree(root))
