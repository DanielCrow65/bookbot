from stats import get_word_count
from stats import get_character_count
from stats import sort_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = "books/frankenstein.txt"
    book_content = get_book_text(book_path)
    book_word_count = get_word_count(book_content)
    character_count = get_character_count(book_content)
    sorted_character_count = sort_characters(character_count)

    #test_string = "I am a test string, ya hoser...!"
    #print(f"{book_word_count} words found in the document")
    #print(character_count)
    #print(sorted_character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    print("--------- Character Count -------")
    for c in sorted_character_count:
        if c["char"].isalpha():
            print(f"{c["char"]}: {c["num"]}")
    print("============= END ===============")

    #since this is a LIST of DICTIONARIES, read it as 'for each DICT in the LIST'. Thus c can use all dict-related functions

main()

