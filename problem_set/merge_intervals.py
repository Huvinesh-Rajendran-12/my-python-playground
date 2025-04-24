def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged_intervals = []
    merged_intervals.append(intervals[0])
    for i in range(1, len(intervals)):
        curr_interval = intervals[i]
        last_merged_interval = merged_intervals[-1]
        if curr_interval[0] <= last_merged_interval[1]:
            last_merged_interval[1] = max(last_merged_interval[1], curr_interval[1])
        else:
            merged_intervals.append(curr_interval)

    return merged_intervals

def main():
    interval_result = merge_intervals([[1, 3], [2, 6], [2, 6], [8, 10], [15, 18]])
    print(interval_result)

if __name__ == "__main__":
    main()

