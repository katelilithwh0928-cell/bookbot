import sys
from stats import get_num_words, get_num_char, sort_in_order


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")

    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    num_char = get_num_char(text)

    sorted_list = sort_in_order(num_char)

    for item in sorted_list:
        ch = item["char"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {item['num']}")

    print("============= END ===============")


main()
