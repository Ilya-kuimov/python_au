# Tree

+ [ Maximum Depth of Binary Tree](#maximum-depth-of-binary-tree)
+ [ Binary Tree Inorder Traversal](#binary-tree-inorder-traversal)
+ [ Invert Binary Tree](#invert-binary-tree)
+ [ Binary Search Tree Iterator](#binary-search-tree-iterator)
+ [ Binary Tree Level Order Traversal](#binary-tree-level-order-traversal)
+ [ Kth Smallest Element in a BST](#kth-smallest-element-in-a-bst)
+ [ Validate Binary Search Tree](#validate-binary-search-tree)
+ [ Symmetric Tree](#symmetric-tree)

##  Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/
```python
class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
   def maxDepth(self, root):
      if not root:
          return 0
      ldepth = self.maxDepth(root.left)
      rdepth = self.maxDepth(root.right)
      return max(ldepth, rdepth) + 1
```
##  Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/
```python
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val)
        printInorder(root.right)

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val)

def printPreorder(root):
    if root:
        print(root.val)
        printPreorder(root.left)
        printPreorder(root.right)

# Driver code
root = Node(1)
root.left      = Node(2)
root.right     = Node(3)
root.left.left  = Node(4)
root.left.right  = Node(5)
print "Preorder traversal of binary tree is"
printPreorder(root)

print "\nInorder traversal of binary tree is"
printInorder(root)

print "\nPostorder traversal of binary tree is"
printPostorder(root)
```
##  Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/
```python
class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root is None:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
```
##  Binary Search Tree Iterator
https://leetcode.com/problems/binary-search-tree-iterator/
```python
LEFT = 0
RIGHT = 1
VALUE = 2
SORT_KEY = -1

class BinarySearchTree(object):

    def __init__(self, sort_key=None):
        self._root = []  
        self._sort_key = sort_key
        self._len = 0  

def insert(self, val):
    if self._sort_key is None:
        sort_key = val // if no sort key, sort key is value
    else:
        sort_key = self._sort_key(val)

    node = self._root
    while node:
        if sort_key < node[_SORT_KEY]:
            node = node[LEFT]
        else:
            node = node[RIGHT]

    if sort_key is val:
        node[:] = [[], [], val]
    else:
        node[:] = [[], [], val, sort_key]
    self._len += 1

def minimum(self):
    return self._extreme_node(LEFT)[VALUE]

def maximum(self):
    return self._extreme_node(RIGHT)[VALUE]

def find(self, sort_key):
    return self._find(sort_key)[VALUE]

def _extreme_node(self, side):
    if not self._root:
        raise IndexError('Empty')
    node = self._root
    while node[side]:
        node = node[side]
    return node

def _find(self, sort_key):
    node = self._root
    while node:
        node_key = node[SORT_KEY]
        if sort_key < node_key:
            node = node[LEFT]
        elif sort_key > node_key:
            node = node[RIGHT]
        else:
            return node
    raise KeyError("%r not found" % sort_key)
```
##  Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/
```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def BFS(self, root) -> int:
        level=1
        current=(root, level)
        s=set()
        result=[]
        Q = [current]
        while Q:
            current=Q.pop()
            level=current[1]
            if current[0] not in s:
                result.append([current[0].val, level])
                s.add(current[0])
            if current[0].left:
                Q.insert(0,(current[0].left, level+1))
            if current[0].right:
                Q.insert(0,(current[0].right, level+1))
        output=[]
        temp=[]
        level=1
        for val in result:
            if val[1]==level:
                temp.append(val[0])
            elif val[1] > level:
                output.append(temp)
                temp=[val[0]]
                level+=1
        output.append(temp)
        return output
```
##  Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
```python
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root == None:
            return None

        i, stack = 0, [(root, False)]

        while stack or node:
            cur, visited = stack.pop()
            if cur:
                if visited:
                    i +=1
                    if i == k:
                        return cur.val
                else:
                    stack.append((cur.right, False))
                    stack.append((cur, True))
                    stack.append((cur.left, False))
```
##  Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/
```python
def isValidBst(node):
    # Empty tree is valid (or sub-tree, for that matter
    # but, since we never descend into a null, that's a
    # moot point).

    if node is null: return true

    # Check left value and sub-tree.

    if node.left is not null:
        if node.left.value >= node.value: return false
        if not isValidBst(node.left): return false

    # Check left value and sub-tree.

    if node.right is not null:
        if node.right.value <= node.value: return false
        if not isValidBst(node.right): return false

    # If there were no failures, including the possibility
    # we're at a leaf node, everything below this node is
    # okay.

    return true
```
##  Symmetric Tree
https://leetcode.com/problems/symmetric-tree/
```python
class Solution:
    def isSymmetric(self, root: 'TreeNode') -> 'bool':
        if not root:
            return True
        return self.isSymmetricHelper(root.left, root.right)

    def isSymmetricHelper(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.val != node2.val: # early stopping - two nodes have different value
            return False 
        out = True
        out = out and self.isSymmetricHelper(node1.left, node2.right)
        if not out: # early stopping
            return False
        out = out and self.isSymmetricHelper(node1.right, node2.left)
        return out
```