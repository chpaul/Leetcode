# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 ==None:
            if l2 != None:return l2
            else: return  None
        elif l2 == None:
            if l1 !=None:return  l1
            else: return None
        elif l1 == None and l2 == None:
            return None

        l1Corrent = l1
        l2Corrent = l2

        if l1Corrent.val <= l2Corrent.val:
            resultHead = l1Corrent
            l1Corrent = l1Corrent.next
        else:
            resultHead = l2Corrent
            l2Corrent = l2Corrent.next

        resultCorrent = resultHead
        while l1Corrent != None  and l2Corrent!=None:
            if l1Corrent.val <= l2Corrent.val:
                resultCorrent.next = l1Corrent
                l1Corrent = l1Corrent.next
            else:
                resultCorrent.next = l2Corrent
                l2Corrent = l2Corrent.next
            resultCorrent =resultCorrent.next
        if l1Corrent!=None:
            resultCorrent.next = l1Corrent
        else: #L2 last
            resultCorrent.next = l2Corrent
        return resultHead
if __name__ == "__main__":
    solution = Solution
    L1 = ListNode(1)
    L1.next = ListNode(2)
    #L1.next.next = ListNode(5)
    #L1.next.next.next = ListNode(9)
    #L1.next.next.next.next = ListNode(10)

    L2 = ListNode(2)
    #L2.next = ListNode(4)
    #L2.next.next = ListNode(6)
    #L2.next.next.next = ListNode(8)

    a = solution.mergeTwoLists(solution, L1, L2)
    curNode = a
    while curNode != None:
        print(curNode.val)
        curNode = curNode.next
