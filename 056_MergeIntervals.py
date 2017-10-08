# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals)<=1:
            return intervals

        intervals = sorted(intervals, key= lambda i:i.start)
        pnt = 0

        while(pnt<len(intervals)-1):

            if (intervals[pnt].start <= intervals[pnt+1].start <= intervals[pnt].end) and (intervals[pnt].start <= intervals[pnt+1].end <= intervals[pnt].end): #remove next
                intervals.pop(pnt + 1)
            elif intervals[pnt].start <= intervals[pnt + 1].start <= intervals[pnt].end:  # merge
                intervals[pnt].end = intervals[pnt + 1].end
                intervals.pop(pnt + 1)
            else:
                pnt+=1

        return intervals


if __name__ == "__main__":
    solution = Solution()
    intervals = []
    intervals.append(Interval(1,4))
    intervals.append(Interval(2, 3))
    # intervals.append(Interval(8, 10))
    # intervals.append(Interval(15, 18))

    a = solution.merge(intervals)
    print(a)