from stats import get_word_count
from stats import get_character_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = "books/frankenstein.txt"
    book_content = get_book_text(book_path)
    #test_string = "I am a test string, ya hoser...!"
    print(f"{get_word_count(book_content)} words found in the document")
    print(get_character_count(book_content))


main()

