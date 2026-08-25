"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new = temp = Node(0)
        curr = head
        nodes = {}

        while curr:
            temp.next = Node(curr.val)
            nodes[curr] = temp.next
            curr = curr.next
            temp = temp.next

        curr = new.next
        temp = head
        while curr:
            curr.random = nodes.get(temp.random)
            curr = curr.next
            temp = temp.next

        return new.next