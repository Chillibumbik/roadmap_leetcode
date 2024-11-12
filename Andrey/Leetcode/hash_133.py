"""
138. Copy List with Random Pointer
https://leetcode.com/problems/copy-list-with-random-pointer/description/?envType=problem-list-v2&envId=hash-table
"""

"""
A linked list of length n is given such that each node contains an additional random pointer, 
which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes,
where each new node has its value set to the value of its corresponding original node. Both the
next and random pointer of the new nodes should point to new nodes in the copied list such that
the pointers in the original list and copied list represent the same list state. None of the
pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then
for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented
as a pair of [val, random_index] where:

    val: an integer representing Node.val
    random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list.


Deepcopy again wins, but i will implement method described in hash_133.py
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

from typing import Optional
class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if head:
            seen_nodes = {}
            root = Node(head.val)
            new_head = root
            
            seen_nodes[hash(head)] = new_head
            older_root = head
            while head.next:
                new_head.next = Node(head.next.val)
                head = head.next
                new_head = new_head.next
                seen_nodes[hash(head)] = new_head
            newer_root = root    
            while older_root:
                if older_root.random is not None:
                    older_hash = hash(older_root.random)
                    newer_root.random = seen_nodes[older_hash]
                older_root = older_root.next
                newer_root = newer_root.next

            return root
            # 1 more last iteration
    