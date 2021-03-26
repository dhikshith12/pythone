class newNode():
    def __init__(self,value):
        self.value = value
        self.left = self.right = None

def buildTree(arr,root,i,n):
    if i<n:
        root = newNode(arr[i])
        root.left = buildTree(arr,root.left,2*i+1,n)
        root.right = buildTree(arr,root.right,2*i+2,n)
    return root

def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.value)
        inOrder(root.right)

arr = list(range(1,11))
root = None
root = buildTree(arr,root,0,len(arr))
inOrder(root)