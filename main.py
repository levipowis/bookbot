def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    print(f"{num_words} words found in the document")
    print(num_letters)

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

main()