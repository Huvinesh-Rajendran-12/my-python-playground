def first_unique_char_idx(s: str) -> int:
    char_counts = {}
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i
    return -1

def main():
    print(first_unique_char_idx("aabbb"))

if __name__ == "__main__":
    main()
