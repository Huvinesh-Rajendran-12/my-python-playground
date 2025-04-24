def rotate_arr(nums: list[int], k: int) -> list[int]:
    assert k >= 0, "K must be greater than or equal to 0"
    k = k % len(nums)
    return nums[-k:] + nums[:-k]

def main():
    nums = [1, 2, 3, 4, 5]
    print("Original array")
    print(rotate_arr(nums, 0))

    print("Array rotated once")
    print(rotate_arr(nums, 1))

    print("Array rotated twice")
    print(rotate_arr(nums, 2))
 
    print("Array rotated thrice")
    print(rotate_arr(nums, 3))

if __name__ == "__main__":
    main()
