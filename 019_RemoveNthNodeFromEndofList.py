# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n ==0:
            return head
        Len = 1 #dummy
        CurrentNode = head
        while CurrentNode.next !=None:
            Len+=1
            CurrentNode = CurrentNode.next
        TargetIdx = Len - n + 1
        if TargetIdx == 0 or TargetIdx >Len:
            return []
        NewChild = ''
        NewParent = ''
        CurrentNode = head
        for i in range(1,Len+1):
            if i == TargetIdx-1:
                NewParent =CurrentNode
            elif i == TargetIdx+1:
                NewChild = CurrentNode
            CurrentNode = CurrentNode.next
        if NewParent !='':
            NewParent.next = NewChild if NewChild != '' else None
        else:
            if NewChild != '': return NewChild
            else: return []

        return head

if __name__ == "__main__":
    solution = Solution
    dummy = ListNode(1)
    dummy.next = ListNode(2)
    dummy.next.next = ListNode(3)
    dummy.next.next.next = ListNode(4)
    dummy.next.next.next.next = ListNode(5)

    a = solution.removeNthFromEnd(solution, dummy,1)
    Current = a
    while True:
        if type(Current) == list:
            print('[]')
            break
        print (str(Current.val) )
        if Current.next == None: break
        Current = Current.next