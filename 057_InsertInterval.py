# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda i: i.start)
        pnt = 0

        while (pnt < len(intervals) - 1):

            if (intervals[pnt].start <= intervals[pnt + 1].start <= intervals[pnt].end) and (
                    intervals[pnt].start <= intervals[pnt + 1].end <= intervals[pnt].end):  # remove next
                intervals.pop(pnt + 1)
            elif intervals[pnt].start <= intervals[pnt + 1].start <= intervals[pnt].end:  # merge
                intervals[pnt].end = intervals[pnt + 1].end
                intervals.pop(pnt + 1)
            else:
                pnt += 1

        return intervals

if __name__ == "__main__":
    solution = Solution()

    intervals = []
    intervals.append(Interval(1,3))
    intervals.append(Interval(6, 9))
    a = solution.insert(intervals, Interval(2,5))
    print(a)