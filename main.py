def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(book_content):
    word_count = book_content.split()
    return len(word_count)

def main():
    book_path = "books/frankenstein.txt"
    #print(get_book_text("books/frankenstein.txt"))
    print(f"{get_word_count(get_book_text(book_path))} words found in the document")

main()