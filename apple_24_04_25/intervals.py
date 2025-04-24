def merge_intervals_func(nums: list[list[int]]) -> list[int]:
    assert 1 <= len(nums) <= 10e4, "The length of the array of intervals should be within 1 and 10e4"
    assert len(nums[0]) == 2, "The length of an interval should just be 2."

    # set an initial counter 
    i = 0
    # set an empty list for merging 
    merged_intervals = []
    # add all the intervals which are not overlapping 
    while i < len(nums) and nums[i][1] < nums[i + 1][0]:
        merged_intervals.append(nums[i])
        i += 1

    # check for all the intervals which are overlapping and then merge
    while i < len(nums) and nums[i][1] <= nums[i + 1][0]:
        last_merged_interval = merged_intervals[-1]
        last_merged_interval[0] = min(nums(i)[0], nums[i + 1][0])
        last_merged_interval[1] = max(nums[i][1], nums[i + 1][1])
        merged_intervals.append(last_merged_interval)
        i += 1 

    # add all the remaining intervals 
    while i < len(nums):
        merged_intervals.append(nums[i])
        i += 1

    return merged_intervals

def main():
    print(merge_intervals_func([[1,3],[2,6],[8,10],[15,18]]))
    

if __name__ == "__main__":
    main()

