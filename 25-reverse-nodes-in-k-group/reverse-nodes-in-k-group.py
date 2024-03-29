# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        groupPrev = dummy
        while True:
            kth = self.getKth(groupPrev,k)
            if not kth:
                break
            groupNext = kth.next
            # reverse the linked list
            curr, prev = groupPrev.next, kth.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            tmp=groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k = k - 1
        return curr