# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        if len(lists) == 1:
            return lists[0]

        import heapq
        A = []
        curr = temp = ListNode(0)

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(A, (node.val, i, node))

        while A:
            if not lists[i]:
                lists.pop(i)

            val, i, node = heapq.heappop(A)

            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(A, (node.next.val, i, node.next))

        return temp.next