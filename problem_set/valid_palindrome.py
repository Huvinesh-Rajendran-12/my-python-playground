def check_valid_palindrome(s: str) -> bool:
    line = s.lower()
    cleaned_words = [c for c in line if c.isalpha()]
    cleaned_line = "".join(cleaned_words)
    return cleaned_line == cleaned_line[::-1]

def main():
    print(check_valid_palindrome("A man, a plan, a canal: Panama"))

if __name__ == "__main__":
    main()
