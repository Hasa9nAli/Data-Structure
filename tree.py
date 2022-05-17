class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def in_order(root):
    if root is not None:
        in_order(root.left)
        print(root.key, end=" ")
        in_order(root.right)


def insert(node, key):
    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node


def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left

    return current



def deleteNode(root, key):
    if root is None:
        return 

    if key < root.key:
        root.left = deleteNode(root.left, key)

    elif key > root.key:
        root.right = deleteNode(root.right, key)

    else:
        if root.left is None:
            temp = root.right
            return temp

        elif root.right is None:
            temp = root.left
            return temp

        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)

    return root


tree = None
tree = insert(tree, 5)
tree = insert(tree, 4)
tree = insert(tree, 1)
tree = insert(tree, 0)
tree = insert(tree, 3)
tree = insert(tree, 2)
tree = insert(tree, 6)
print ("the tree before deleting")
in_order(tree)
print("\n")
print ("the tree before deleting ")

tree = deleteNode(tree, 3)
tree = deleteNode(tree, 0)
tree = deleteNode(tree, 6)
in_order(tree)


            

                

