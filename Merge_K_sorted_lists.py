# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        if(len(lists)==0):
            return None
        for i in range(len(lists)):
            temp = lists[i]
            if(not temp):
                continue
            while(temp):
                heapq.heappush(heap,temp.val)
                temp = temp.next
        if(heap):
            head = ListNode(heapq.heappop(heap))
            temp = head
            while(heap):
                temp.next = ListNode(heapq.heappop(heap))
                temp = temp.next
            return head
        else:
            return None
            
        
        
