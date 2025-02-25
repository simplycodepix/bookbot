import sys
from stats import (
    get_num_words,
    get_chars_count,
    chars_count_to_sorted_list
)

def main():
    if len(sys.argv) < 2:
        return print("Usage: python3 main.py <path_to_book>")

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = get_num_words(book_text)
    chars_count = get_chars_count(book_text)
    sorted_chars_count = chars_count_to_sorted_list(chars_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in sorted_chars_count:
        print(f"{entry['char']}: {entry['count']}")
    print("============ END ============")


def get_book_text(path: str):
    with open(path, 'r') as file:
        book_text = file.read()
        return book_text

main()
