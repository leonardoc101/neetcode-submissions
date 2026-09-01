class Solution:
    def insert(self, intervals: List[List[int]], newInterval : List[int]) -> List[List[int]]:
        start = None
        added = False
        idx = 0
        new_interval = []
        while idx < len(intervals):
            if intervals[idx][1] < newInterval[0] or added:
                new_interval.append(intervals[idx])
                idx += 1
                continue
            if intervals[idx][0] > newInterval[1]:
                new_interval.append(newInterval)
                added = True
                continue

            if not start:
                start = min(intervals[idx][0], newInterval[0])
                while idx < len(intervals):
                    if newInterval[1] < intervals[idx][0]:
                        new_interval.append([start, newInterval[1]])
                        added = True
                        break
                    if intervals[idx][0] <= newInterval[1] <= intervals[idx][1]:
                        new_interval.append([start, intervals[idx][1]])
                        added = True
                        idx += 1
                        break
                    idx += 1
        if not added:
            if start:
                new_interval.append([start, newInterval[1]])
            else:
                new_interval.append(newInterval)
        return new_interval