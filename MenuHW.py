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

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_rec(self.root, data)
    def _insert_rec(self, node, data):
        if data < node.data:
            if node.leftNode is None:
                node.leftNode = TreeNode(data)
            else:
                self._insert_rec(node.leftNode,data)
        else:
            if node.rightNode is None:
                node.rightNode = TreeNode(data)
            else:
                self._insert_rec(node.rightNode,data)


def main():
    tree = BinaryTree()
    while True:
        print("\nMenu:")
        print("1. Create Tree")
        print("2. Inorder Traversal")
        print("3. Preorder Traversal")
        print("4. Postorder Traversal")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            while True:
                key = int(input("Please enter your value to insert or -1 to stop: "))
                if key == -1:
                    break
                else:
                    tree.insert(key)
                    print("Inserted value " , key)
        
        elif choice == '2':
            print("Inorder Traversal")
            if tree.root:
                tree.root.InorderTraversal()
            else:
                print("Tree is empty")
        elif choice == '3':
            print("Preorder Traversal")
            if tree.root:
                tree.root.PreorderTraversal()
            else:
                print("Tree is empty")
        elif choice == '4':
            print("Postorder Traversal")
            if tree.root:
                tree.root.PostorderTraversal()
            else:
                print("Tree is empty")
            
        elif choice == '5':
            print("Exiting")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
