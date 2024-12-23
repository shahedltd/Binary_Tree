class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def left_side(self):
        self.left = Node(self.data - 1)

    def right_side(self):
        self.right =  Node(self.data+ 1)
    def show(self):
        if self.left:
            self.left.show()
        print(self.data)
        if self.right:
            self.right.show()

root = Node(100)
root.left_side()
root.right_side()
root.show()