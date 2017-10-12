# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None

        if head.next == None:
            return head
        slowpnt, fastpnt, interval, listlen = head, head, 0, 1
        while (fastpnt.next != None or interval<k):
            if(fastpnt.next ==None and interval<k):
                slowpnt, fastpnt =head, head
                interval =  listlen * int(k / listlen)

            fastpnt = fastpnt.next
            listlen+=1
            if interval==k:
                slowpnt = slowpnt.next
            else:
                interval += 1
        #switch
        fastpnt.next = head
        newhead = slowpnt.next
        slowpnt.next =None
        return newhead

if __name__ == "__main__":
    solution = Solution()

    Lst = ListNode(1)
    n =Lst
    for i in range(2,6):
        n.next = ListNode(i)
        n = n.next
    a = solution.rotateRight(Lst ,7)
    print(a)