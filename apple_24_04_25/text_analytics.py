def analyse_text(s: str) -> list:
    words_count = {}
    curr_username = ""
    lines = s.strip().splitlines()
    for line in lines:
        parts = line.strip().split(" ")
        if parts[0].startswith("<") and parts[0].endswith(">"):
            curr_username = parts[0]
            words = parts[1:]
            word_count = len(words)
        else:
            words = parts
            word_count = len(words)

        if curr_username not in words_count:
            words_count[curr_username] = 0
        words_count[curr_username] += word_count

    sorted_word_counts = sorted(words_count.items(), key=lambda x: x[1], reverse=True)
    return [item[0] for item in sorted_word_counts]

def main():
    print(analyse_text("""
    <user1> this is some chat words
    <user2> the sky is blue
    This line is still attributed to the user above haha
    <user1> more chat from me! 38gad81
    """
    ))

if __name__ == "__main__":
    main()

