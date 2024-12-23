# Binary_Tree
Binary Tree! This repository contains a simple implementation of a binary tree in Python. The Node class represents each node in the tree, with methods to add left and right children and to display the tree in an in-order traversal. 
# Features
Node Initialization: Each Node object has data, a left child, and a right child.
Dynamic Node Creation:
The left_side() method creates a left child with a value decreased by 1 from the parent node.
The right_side() method creates a right child with a value increased by 1 from the parent node.
In-Order Traversal: The show() method recursively prints the tree values in an in-order traversal pattern.
# Code Overview
Class Node
This class is the building block of the binary tree. It has three main methods:

__init__(self, data): Initializes the node with a value (data) and sets the left and right pointers to None.
left_side(self): Creates a left child node with the value data - 1.
right_side(self): Creates a right child node with the value data + 1.
show(self): Recursively traverses and prints the binary tree in in-order traversal.
# How to Run
Clone this repository:
git clone <repository-link>
cd <repository-folder>
Make sure you have Python installed (preferably version 3.x).
Run the code:
python binary_tree.py
# Example Output
When you run the code, you will see the following output:
99
100
101
# Use Cases
Learning Tool: Great for understanding binary tree structure and recursive traversal.
Algorithm Building Block: Useful for exploring more complex tree-based algorithms (e.g., binary search trees, AVL trees).
# Contributing
Contributions, issues, and feature requests are welcome! Feel free to fork this repository and submit a pull request.
# CODE:
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
