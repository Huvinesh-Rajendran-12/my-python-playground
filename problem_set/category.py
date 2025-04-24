def count_category(categories: list[tuple[int, str]]) -> int:
    category_counts = {}
    for category in categories:
        if category[1] not in category_counts:
            category_counts[category[1]] = 1
        else:
            category_counts[category[1]] += 1
    sorted_category_counts = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
    ans = [item[0] for item in sorted_category_counts][0]
    return ans

def main():
    print(count_category([(1, "Electronics"), (2, "Basketball"), (3, "Electronics"), (4, "Electronics"), (5, "Tennis")]))

if __name__ == "__main__":
    main()
