from stats import number_of_words
from stats import char_appearances
from stats import sorted_dictionary
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    contents = get_book_text(filepath)
    now = number_of_words(contents)
    print(f"Found {now} total words")
    dictionary = char_appearances(contents)
    #print(dictionary)
    sorted_dict = sorted_dictionary(dictionary)
    for pair in sorted_dict:
        if pair.isalpha():
            print(f"{pair}: {sorted_dict[pair]}")

main()
