import sys

from pathlib import Path

from stats import get_word_count


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    words = get_word_count(text)
    characters = get_characters(text)
    characters_sorted = sort_dict_to_list(characters)
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    print()
    for character in characters_sorted:
        print(f"{character['char']}: {character['count']}")
    print("--- End report ---")


def get_book_text(path: str) -> str:
    file_path = Path(path)

    try:
        with file_path.open("r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File not found at path: {file_path}")
        return ""
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return ""


def get_characters(text: str) -> dict:
    lower = text.lower()
    chars = {}

    for char in lower:
        if char.isalpha():
            chars[char] = chars.get(char, 0) + 1

    return chars


def sort_by(dictionary: dict) -> int:
    return dictionary["count"]


def sort_dict_to_list(dictionary: dict) -> list:
    sorted_list = []
    for item in dictionary:
        sorted_list.append({"char": item, "count": dictionary[item]})
    sorted_list.sort(reverse=True, key=sort_by)
    return sorted_list


if __name__ == "__main__":
    main()
