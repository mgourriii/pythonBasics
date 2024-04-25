     
class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 
 
 
def printPreOrder(root):
    if root == None:
        return
 
    # root, left_subtree, right_subtree 
    print(root.data, end = " ")
    printPreOrder(root.left)
    printPreOrder(root.right)
 
def printInOrder(root):
    if root == None:
        return
 
    # left_subtree, root, right_subtree 
 
    printInOrder(root.left)
    print(root.data, end = " ")
    printInOrder(root.right) 
 
def printPostOrder(root):
    if root == None:
        return
 
    # left_subtree, right_subtree, root
 
    printPostOrder(root.left)
    printPostOrder(root.right) 
    print(root.data, end = " ")
 
 
 
 
 
 
 
 
 
 
 
 
#https://pastebin.com/gu5CduWi
 
def printLevelOrder(root):
    result = []
    Q = [root]
 
    while len(Q) > 0:
        n = len(Q)
        subResult = []
        for i in range(n):
            # step-1: popping
            curr = Q.pop(0)
            subResult.append(curr.data)
 
            # step-2: pushing left child if its not none 
            if curr.left != None:
                Q.append(curr.left)
 
            # step-3: pushing right child if its not none
            if curr.right != None:
                Q.append(curr.right)
 
        result.append(subResult)
 
    #print(result)
    for subLevel in result:
        print(*subLevel)
 
def printZigZagLevelOrder(root):
    result = []
    Q = [root]
    level = 0 
 
    while len(Q) > 0:
        n = len(Q)
        subResult = []
        for i in range(n):
            # step-1: popping
            curr = Q.pop(0)
            subResult.append(curr.data)
 
            # step-2: pushing left child if its not none 
            if curr.left != None:
                Q.append(curr.left)
 
            # step-3: pushing right child if its not none
            if curr.right != None:
                Q.append(curr.right)
 
        if level % 2 == 1:
            subResult = subResult[::-1]
 
        result.append(subResult)
        level += 1 
 
    #print(result)
    for subLevel in result:
        print(*subLevel) 
 
 
def leftViewOfBinaryTree(root):
    result = []
    Q = [root]
 
    while len(Q) > 0:
        n = len(Q)
        for i in range(n):
            # step-1: popping
            curr = Q.pop(0)
            if i == 0:
                result.append(curr.data)
 
            # step-2: pushing left child if its not none 
            if curr.left != None:
                Q.append(curr.left)
 
            # step-3: pushing right child if its not none
            if curr.right != None:
                Q.append(curr.right)
 
    print("Left view is:")
    print(result)
 
 
 
def rightViewOfBinaryTree(root):
    result = []
    Q = [root]
 
    while len(Q) > 0:
        n = len(Q)
        for i in range(n):
            # step-1: popping
            curr = Q.pop(0)
            if i == n - 1:
                result.append(curr.data)
 
            # step-2: pushing left child if its not none 
            if curr.left != None:
                Q.append(curr.left)
 
            # step-3: pushing right child if its not none
            if curr.right != None:
                Q.append(curr.right)
 
    print("Right view is:")
    print(result)
 
# 1. objects creation (memory allocation) 
root = TreeNode(18)
# root:
# data = 15 
# left = None 
# right = None 
obj2 = TreeNode(15)
obj3 = TreeNode(20)
obj4 = TreeNode(25)
obj5 = TreeNode(30)
obj6 = TreeNode(45)
obj7 = TreeNode(80)
 
#    18 
#   15  20 
# 25 30 45 80
 
 
# 2- establishing links between nodes 
root.left = obj2 
root.right = obj3 
 
obj2.left = obj4 
obj2.right = obj5 
 
obj3.left = obj6 
obj3.right = obj7
leftViewOfBinaryTree(root)
rightViewOfBinaryTree(root)
#printPostOrder(root)

