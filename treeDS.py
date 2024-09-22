class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftNode = None
        self.rightNode = None
    
    def InorderTraversal(self):
        if self.leftNode is not None:
            self.leftNode.InorderTraversal()
        print(self.data,end=" -> ")
        if self.rightNode is not None:
            self.rightNode.InorderTraversal()
    
    def PreorderTraversal(self):
        print(self.data,end=" -> ")
        if self.leftNode is not None:
            self.leftNode.PreorderTraversal()
        if self.rightNode is not None:
            self.rightNode.PreorderTraversal()

    def PostorderTraversal(self):
        if self.leftNode is not None:
            self.leftNode.PostorderTraversal()
        if self.rightNode is not None:
            self.rightNode.PostorderTraversal()
        print(self.data,end=" -> ")


root = TreeNode(5)
root.leftNode = TreeNode(4)
root.leftNode.leftNode = TreeNode(2)
root.rightNode = TreeNode(8)
root.rightNode.leftNode = TreeNode(7)
root.rightNode.rightNode = TreeNode(9)

# Inorder traversal (left -> root -> right)
print("InorderTraversal")
root.InorderTraversal()
# Preorder traversal (root -> left -> right)
print()
print("PreorderTraversal")
root.PreorderTraversal()
# Postorder traversal (left -> right -> root)
print()
print("PostorderTraversal")
root.PostorderTraversal()
        

        

