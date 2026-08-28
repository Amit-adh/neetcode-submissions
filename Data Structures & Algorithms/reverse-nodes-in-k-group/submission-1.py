# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1 or not head.next:
            return head


        def reverse(node):
            curr = node
            prev = None

            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next

            return prev

        new_head = curr = ListNode(0)
        slow, fast = head, head

        i = 0
        while True:
            j = 1
            while fast and j < k:
                fast = fast.next
                j += 1

            if not fast or j != k:
                curr.next = slow
                break

            next_group = fast.next
            fast.next = None

            old_tail = slow
            slow = reverse(slow)

            old_tail.next = next_group
            curr.next = slow

            curr = old_tail
            slow = next_group
            fast = next_group

        return new_head.next  