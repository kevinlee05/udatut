class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_node(new_val, self.root)
        return

    def insert_node(self, new_val, node):
        if new_val > node.value:
            if node.right is None:
                node.right = Node(new_val)
                return
            self.insert_node(new_val, node.right)
        if new_val < node.value:
            if node.left is None:
                node.left = Node(new_val)
                return
            self.insert_node(new_val, node.left)
        return

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        traversal = self.inorder_print(self.root, [])
        return "-".join(str(e) for e in traversal)

    def inorder_print(self, start, traversal):
        """Helper method - use this to create a
        recursive print solution."""
        if start.left:
            self.inorder_print(start.left, traversal)
        traversal.append(start.value)
        if start.right:
            self.inorder_print(start.right, traversal)
        return traversal

    def search(self, find_val):
        return self.search_node(find_val, self.root)

    def search_node(self, find_val, node):
        if not node:
            return False
        if node.value == find_val:
            return True
        if find_val > node.value:
            return self.search_node(find_val, node.right)
        if find_val < node.value:
            return self.search_node(find_val, node.left)
        return False

# Set up tree
tree = BST(8)

# Insert elements
tree.insert(2)
tree.insert(13)
tree.insert(4)
tree.insert(5)
tree.insert(9)
tree.insert(11)
tree.insert(15)

print(tree.print_tree())

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
print(tree.search(15))
