import random


class Node:
    """Class to create Nodes in AVL Tree"""

    __slots__ = 'element', 'left_tree', 'right_tree', 'height'

    def __init__(self, element, left_tree, right_tree):
        self.element = element
        self.left_tree = left_tree
        self.right_tree = right_tree
        self.height = 0


class AVLTree:
    """AVL tree class with the following methods:
     - create nodes in the tree (the tree creates nodes and checks it self
     to keep the tree balanced);
     - find height of the tree;
     - search nodes in the tree;
     - display all nodes in the tree;
     - delete nodes in the tree (keeping the tree balanced);
     - display number of all nodes in the tree;
    """

    def __init__(self):
        self.root = None

    def create_tree(self, root, e):
        if root is None:
            n = Node(e, None, None)
            root = n
        else:
            if e == root.element:
                print(f"""The element {e} is already exist in the tree!""")
                return
            elif e < root.element:
                root.left_tree = self.create_tree(root.left_tree, e)
            else:
                root.right_tree = self.create_tree(root.right_tree, e)
        root.height = self.balance_factor(root)
        # If you want to see balance factor for each node
        # print('Balance factor for element:', root.element, 'is', root.height)
        if root.height < -1:
            balanced_left_tree = self.left_rotation(root)
            return balanced_left_tree
        if root.height > 1:
            balanced_right_tree = self.right_rotation(root)
            return balanced_right_tree
        return root

    def height_of_tree(self, root):
        if root is None:
            return 0
        else:
            height_left_tree = 1 + self.height_of_tree(root.left_tree)
            height_right_tree = 1 + self.height_of_tree(root.right_tree)
            return max(height_left_tree, height_right_tree)

    def final_height(self):
        if self.root is None:
            return 0
        height = (self.height_of_tree(self.root)) - 1
        print('The height of the tree is', height)
        return height

    def balance_factor(self, root):
        if root is None:
            return 0
        return self.height_of_tree(root.right_tree) - self.height_of_tree(root.left_tree)

    def left_rotation(self, root):
        parent = root
        child = parent.left_tree

        # left-left rotation
        if parent == self.root and parent.height == -2 and child.height == -1:
            parent.left_tree = child.right_tree
            child.right_tree = parent
            self.root = child
            parent.height = self.balance_factor(child)
            child.height = self.balance_factor(child)
            return child

        elif parent != self.root and parent.height == -2 and child.height == -1:
            parent.left_tree = child.right_tree
            child.right_tree = parent
            parent.height = self.balance_factor(child)
            child.height = self.balance_factor(child)
            return child

        # left-right rotation
        elif parent == self.root and parent.height == -2 and child.height == 1:
            ptr_ptr = child.right_tree
            child.right_tree = ptr_ptr.left_tree
            parent.left_tree = ptr_ptr.right_tree
            ptr_ptr.left_tree = child
            ptr_ptr.right_tree = parent
            self.root = ptr_ptr
            parent.height = self.balance_factor(child)
            child.height = self.balance_factor(child)
            ptr_ptr.height = self.balance_factor(ptr_ptr)
            return ptr_ptr

        elif parent != self.root and parent.height == -2 and child.height == 1:
            ptr_ptr = child.right_tree
            child.right_tree = ptr_ptr.left_tree
            parent.left_tree = ptr_ptr.right_tree
            ptr_ptr.left_tree = child
            ptr_ptr.right_tree = parent
            parent.height = self.balance_factor(child)
            child.height = self.balance_factor(child)
            ptr_ptr.height = self.balance_factor(ptr_ptr)
            return ptr_ptr

        # case for deletion function
        elif parent == self.root and parent.height == -2 and child.height == 0:
            parent.left_tree = child.right_tree
            child.right_tree = parent
            self.root = child
            parent.height = self.balance_factor(parent)
            child.height = self.balance_factor(child)
            return child

        elif parent != self.root and parent.height == -2 and child.height == 0:
            parent.left_tree = child.right_tree
            child.right_tree = parent
            parent.height = self.balance_factor(parent)
            child.height = self.balance_factor(child)
            return child

    def right_rotation(self, root):
        parent = root
        child = parent.right_tree

        # right-right rotation
        if parent == self.root and parent.height == 2 and child.height == 1:
            parent.right_tree = child.left_tree
            child.left_tree = parent
            self.root = child
            parent.height = self.balance_factor(child)
            child.height = self.balance_factor(child)
            return child

        elif parent != self.root and parent.height == 2 and child.height == 1:
            parent.right_tree = child.left_tree
            child.left_tree = parent
            parent.height = self.balance_factor(child)
            child.height = self.balance_factor(child)
            return child

        # right-left rotation
        elif parent == self.root and parent.height == 2 and child.height == -1:
            ptr_ptr = child.left_tree
            child.left_tree = ptr_ptr.right_tree
            parent.right_tree = ptr_ptr.left_tree
            ptr_ptr.left_tree = parent
            ptr_ptr.right_tree = child
            self.root = ptr_ptr
            parent.height = self.balance_factor(child)
            child.height = self.balance_factor(child)
            ptr_ptr.height = self.balance_factor(ptr_ptr)
            return ptr_ptr

        elif parent != self.root and parent.height == 2 and child.height == -1:
            ptr_ptr = child.left_tree
            child.left_tree = ptr_ptr.right_tree
            parent.right_tree = ptr_ptr.left_tree
            ptr_ptr.left_tree = parent
            ptr_ptr.right_tree = child
            parent.height = self.balance_factor(child)
            child.height = self.balance_factor(child)
            ptr_ptr.height = self.balance_factor(ptr_ptr)
            return ptr_ptr

        # case for deletion function
        elif parent == self.root and parent.height == 2 and child.height == 0:
            parent.right_tree = child.left_tree
            child.left_tree = parent
            self.root = child
            parent.height = self.balance_factor(parent)
            child.height = self.balance_factor(child)
            return child

        elif parent != self.root and parent.height == 2 and child.height == 0:
            parent.right_tree = child.left_tree
            child.left_tree = parent
            parent.height = self.balance_factor(parent)
            child.height = self.balance_factor(child)
            return child

    def find_greatest(self, root):
        if root is None:
            return None
        else:
            if root.right_tree is not None:
                return self.find_greatest(root.right_tree)
        return root

    def search_element(self, root, e):
        if root is not None:
            if e == root.element:
                print()
                print(f"""Element {e} is found in the tree!""")
                return True
            elif e < root.element:
                self.search_element(root.left_tree, e)
            else:
                self.search_element(root.right_tree, e)
        else:
            print()
            print(f"""Element {e} is {'not found'.upper()} in the tree""")
            return False

    def removing_element(self, root, e):
        if root is None:
            print(f"""Element {e} is {'not'.upper()} found in the tree""")
            return root
        else:
            if root.left_tree is not None:
                root.left_tree = self.removing_element(root.left_tree, e)
            if root.element == e:
                p = root
                if root.left_tree is None and root.right_tree is None:
                    p = None
                    root = p
                    print(f"""Element {e} was deleted from the tree""")
                    return root
                elif root.left_tree is not None and root.right_tree is None:
                    root = root.left_tree
                    p = root
                    print(f"""Element {e} was deleted from the tree""")
                    return p
                elif root.left_tree is None and root.right_tree is not None:
                    root = root.right_tree
                    p = root
                    print(f"""Element {e} was deleted from the tree""")
                    return p
                elif root.left_tree is not None and root.right_tree is not None:
                    p = self.find_greatest(root.left_tree)
                    root.element, p.element = p.element, root.element
                    root.left_tree = self.removing_element(root.left_tree, e)
            if root.right_tree is not None:
                root.right_tree = self.removing_element(root.right_tree, e)
        root.height = self.balance_factor(root)
        if root.height < -1:
            return self.left_rotation(root)
        elif root.height > 1:
            return self.right_rotation(root)
        return root

    def display_in_order(self, root):
        if root is not None:
            self.display_in_order(root.left_tree)
            print(root.element, end=' ')
            self.display_in_order(root.right_tree)

    def count_number_of_nodes(self, root):
        if root is not None:
            q = self.count_number_of_nodes(root.left_tree)
            w = self.count_number_of_nodes(root.right_tree)
            return q + w + 1
        return 0


testing_array = [0] * 5000

for i in range(len(testing_array)):
    testing_array[i] = random.randint(-1000000, 1000000)

# here again I use set, to create unique values in AVL tree since AVL tree have to have unique keys
unique_values = list(set(testing_array))

x = AVLTree()
x.root = x.create_tree(x.root, unique_values[0])

for j in range(1, len(unique_values)):
    x.create_tree(x.root, unique_values[j])

print(unique_values)

x.display_in_order(x.root)
print()
x.final_height()
print(x.balance_factor(x.root))

for k in range(len(unique_values)):
    x.removing_element(x.root, unique_values[k])
    # Uncomment this if you want to see height, balance factor for each node and
    # number of nodes in the tree after each deletion operation
    # x.final_height()
    # print('Balance factor:', x.balance_factor(x.root))
    # print('Number of nodes in the tree:', x.count_number_of_nodes(x.root))
