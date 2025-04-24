def countWordContribution(input: str) -> list:
    lines = input.splitlines()
    word_counts: dict[str, int] = {}
    curr_username = ""
    for line in lines:
        if line != "":
            line = line.strip()
            parts = line.split(" ")
            if parts[0].startswith("[") and parts[0].endswith("]"):
                username = parts[0]
                curr_username = username
                words = parts[1:]
            else:
                words = parts
            word_count = len(words)
            if curr_username not in word_counts:
                word_counts[curr_username] = 0
            word_counts[curr_username] += word_count

    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return [item[0] for item in sorted_word_counts]

def main():
    input = """
    [user1] hello world
    [user2] hi there
    [user1] how are you
    [user3] good morning
    [user2] what's up
    [user1] i'm fine
    [user3] nice to meet you
    [user2] same here
    [user1] see you later
    [user3] bye
    """
    print(countWordContribution(input))


if __name__ == "__main__":
    main()
