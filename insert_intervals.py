
def insert(intervals, newInterval):
    if not intervals:
        return [newInterval]
    if not newInterval:
        return intervals

    result = []
    i = 0

    # Add intervals that do not overlap with the newInterval
    while i < len(intervals) and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Merge intervals that overlap with the newInterval
    while i < len(intervals) and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    result.append(newInterval)

    # Add remaining intervals
    while i < len(intervals):
        result.append(intervals[i])
        i += 1

    return result

def main():
    interval_result = insert([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]], [2, 5])

    print(interval_result)



if __name__ == "__main__":
    main()
