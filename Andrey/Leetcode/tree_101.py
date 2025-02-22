"""
101. Symmetric Tree
https://leetcode.com/problems/symmetric-tree/description/?envType=problem-list-v2&envId=tree
"""

"""
Given the root of a binary tree, check whether it is a mirror of itself
(i.e., symmetric around its center).

Можно пройти дерево слева и справа и сравнить резуьтаты, но тогда придется делать 2 прохода. 
Можно во время прохода сравнивать деревья между собой, что сделает лучше.
Можно сделать дипкопи двух поддеревьев, но сравнив их мы не получим ничего хорошего т.к. "хорошее"
дерево будет отражено. В итоге лучше сравнивать на месте
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root) -> bool:
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        if root.left == None or root.right == None:
            return False
        return self.check_symmetry(root.left, root.right)
        
    def check_symmetry(self, left, right):
            if left == None and right == None:
                return True
            if left == None or right == None:
                return False
            if left.val != right.val:
                return False
            return self.check_symmetry(left.left, right.right) and self.check_symmetry(left.right, right.left)

        