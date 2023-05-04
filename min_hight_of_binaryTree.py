class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def min_hight_binary(root):
    if root == None:
        return 0
    else:
        lDepth = min_hight_binary(root.left)
        rDepth = min_hight_binary(root.right)

        if lDepth > rDepth:
            return 1+rDepth
        else:
            return 1+lDepth


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.right = Node(7)
root.right.right = Node(6)


print("Minimum Hieght of binary tree is :", min_hight_binary(root))
