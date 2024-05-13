def get_book_info(words: list[str]) -> dict[str, int]:
    char_counts = {}
    for word in words:
        for letter in word.lower():
            if letter in char_counts:
                char_counts[letter] += 1
            else:
                char_counts[letter] = 0
    
    return [{"char":k, "count": v} for (k,v) in char_counts.items()]


def print_report(book_info: list[dict], word_count: int, path: str) -> None:
    book_info.sort(reverse=True, key=lambda char_info: char_info["count"])
    print(f"--- Begin report of {path}---")
    print(f"{word_count} words found in the document")
    print()
    for info in book_info:
        if info["char"].isalpha():
            print(f"The {info["char"]} character was found {info["count"]} times")
    print("--- End report ---")


if __name__ == '__main__':
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        words = file_contents.split()
        book_info = get_book_info(words)
        print_report(book_info, len(words), path)

