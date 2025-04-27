def get_word_count(book_content):
    word_count = book_content.split()
    return len(word_count)

def get_character_count(book_content):
    character_dict = {}
    book_content = book_content.lower()
    #print(book_content)
    #print statement just checks if I am giving it the correct argument
    for char in book_content:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict