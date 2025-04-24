def merge_linked_list(l1, l2):
    assert 0 <= len(l1) <= 50, "Length of l1 must be between 0 and 50"
    assert 0 <= len(l2) <= 50, "Length of l2 must be between 0 and 50"
    if l1 and l2 is []:
        return l1
    if l1 is [] and l2:
        return l2
    if l1 is [] and l2 is []:
        return []

    merged_list = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merged_list.append(l1[i])
            i += 1
        else:
            merged_list.append(l2[j])
            j += 1

    while i < len(l1):
        merged_list.append(l1[i])
        i += 1

    while j < len(l2):
        merged_list.append(l2[j])
        j += 1

    return merged_list

def main():
    print(merge_linked_list([1, 2, 4], [1, 3, 4]))

if __name__ == "__main__":
    main()
    