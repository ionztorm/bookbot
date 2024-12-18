def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_word_count(text)
    characters = get_characters(text)
    characters_sorted = sort_dict_to_list(characters)
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    print()
    for character in characters_sorted:
        print(f"'{character['char']}' appeared '{character['count']}' times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

def get_characters(text):
    lower = text.lower()
    chars = {}

    for char in lower:
        if char.isalpha():
            chars[char] = chars.get(char,0) + 1

    return chars

def sort_by(dict):
    return dict["count"]

def sort_dict_to_list(dict):
    sorted_list = []
    for item in dict:
        sorted_list.append({ "char": item, "count": dict[item] })
    sorted_list.sort(reverse = True, key = sort_by)
    return sorted_list

main()