class newNode: 
    def __init__(self, data):  
        self.data = data  
        self.left = self.right = None

   
def diameter(root):
    if root is None:
        return 0,0
    ld,lh = diameter(root.left)
    rd,rh = diameter(root.right)
    h = max(lh,rh)+1
    d = max(ld,rd,lh+rh+1)
    return d,h
  
# Driver code  
if __name__ == '__main__': 
    root = newNode(1)  
    root.left = newNode(2)  
    root.right = newNode(3)  
    root.left.left = newNode(4)  
    root.left.right = newNode(5)
    root.left.left.left = newNode(6)  
    d,h = diameter(root)
  
    print("Diameter is", d,h) 