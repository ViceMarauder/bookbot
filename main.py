from stats import get_num_words,get_num_chars,sort_dict
import os
import sys

def get_book_text(file_path: str|bytes|os.PathLike) -> str:
    with open(file_path, "r") as f:
        file_content = f.read()
        return file_content

def main():
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
        book_data = get_book_text(book_path)
        print("="*12 + " BOOKBOT " + "="*12)
        print(f"Analyzing book found at {book_path}...")
        print("-"*11 + " Word Count " + "-"*11)
        print(f"Found {get_num_words(book_data)} total words")
        print("-"*9 + " Character Count " + "-"*9)
        for item in sort_dict(get_num_chars(book_data)):
            if item.get('char').isalpha():
                print(f"{item.get('char')}: {item.get('num')}")
            else:
                pass
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()
