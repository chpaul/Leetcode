class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        CarryToNext = 0
        Result = ListNode(-1)
        l1node = l1
        l2node = l2
        CurrentNode = Result
        while True:
            sum = (l1node.val + l2node.val + CarryToNext) % 10
            CarryToNext = (l1node.val + l2node.val + CarryToNext)//10
            CurrentNode.next=ListNode(sum)
            CurrentNode = CurrentNode.next
            if l1node.next == None and l2node.next == None:
                if CarryToNext != 0:
                    CurrentNode.next=ListNode(CarryToNext)
                break
            l1node = l1node.next if l1node.next != None else ListNode(0)
            l2node = l2node.next if l2node.next != None else ListNode(0)
        return Result.next

if __name__ == "__main__":
    l1 = ListNode(5)
    l2 = ListNode(5)
    solution = Solution
    a = solution.addTwoNumbers(solution, l1, l2)