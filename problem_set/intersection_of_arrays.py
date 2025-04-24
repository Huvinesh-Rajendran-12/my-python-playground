def intersection_of_arrays(l1: list[int], l2: list[int]) -> list[int]:
    assert 1 <= len(l1) <= 1000, "Length of l1 must be between 1 and 1000"
    assert 1 <= len(l2) <= 1000, "Length of l2 must be between 1 and 1000"

    i = 0
    intersected = []
    while i < len(l1):
        if l1[i] in l2:
            intersected.append(l1[i])
        i += 1
    intersected = set(intersected)
    return list(intersected)

def main():
    print(intersection_of_arrays([1, 2, 2, 1], [2, 2, 2]))
    print(intersection_of_arrays([1, 2, 3, 3], [2, 3]))
    print(intersection_of_arrays([4, 9, 5], [9, 4, 9, 8, 4, 5]))


if __name__ == "__main__":
    main()

