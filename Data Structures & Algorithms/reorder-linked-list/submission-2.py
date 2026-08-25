# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l1 = head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        #reverse
        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        l2 = prev

        flag = False

        while l1 and l2:
            if not flag:
                next1 = l1.next
                l1.next = l2
                l1 = next1
                flag = True

            else:
                next2 = l2.next
                l2.next = l1
                l2 = next2
                flag = False
        return None