def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def word_count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

print(word_count())