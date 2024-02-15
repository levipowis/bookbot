def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    sorted_character_list = get_sorted_character_list(num_letters)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    for character in sorted_character_list:
        letter = character["letter"]
        num = character["num"]
        print(f"The {letter} character was found {num} times")
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letters(text):
    letter_counts = {}
    for i in range(0, len(text)):
        letter = text[i].lower()
        if letter not in letter_counts:
            letter_counts[letter] = 0
        letter_counts[letter] += 1
    return letter_counts

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_sorted_character_list(num_letters):
    character_list = []
    for key, value in num_letters.items():
        if key.isalpha():
            character_list.append({"letter": key, "num": value})
    character_list.sort(reverse=True, key=sort_on)
    return character_list

def sort_on(character_list):
    return character_list["num"]

main()
