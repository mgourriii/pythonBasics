class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.right = None 
        self.left = None  
 
 
def insertIntoBST(root, ele):
    if root == None:
        newBlock = TreeNode(ele)
        return newBlock 
 
    if root.data < ele:
        root.right = insertIntoBST(root.right, ele)
    else:
        root.left = insertIntoBST(root.left, ele)
    return root
 
def printInorderTraversal(root):
    if root == None:
        return 
 
    printInorderTraversal(root.left)
    print(root.data, end = " ")
    printInorderTraversal(root.right)
 
 
 
nums = [18, 10, 25, 8, 15, 22, 28]
 
#      18 
#   10    25 
# 8  15 22  28
 
# preorder: 18, 10, 8, 15, 25, 22, 28
# inorder: 8 10 15 18 22 25 28
# postorder: 8 15 10 22 28 25 18
 
 
root = None 
for ele in nums:
    root = insertIntoBST(root, ele)
 
printInorderTraversal(root)
 

 
 
