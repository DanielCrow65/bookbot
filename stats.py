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

def sort_on(dict):
    return dict["num"]

def sort_characters(character_dict):
    sorted_character_list = []

    for char in character_dict:
        temp_dict = {}
        #if I declare this outside of the loop append will reference the first value I ever give it
        #while in the loop, it is thrown away at the end of every iteration letting a fresh value be put in 
        temp_dict["char"] = char
        temp_dict["num"] = character_dict[char]
        sorted_character_list.append(temp_dict)

    sorted_character_list.sort(reverse=True, key=sort_on)
    
    return sorted_character_list
"""   
    character_keys = []
    character_values = []
    assigned_character_dict = {}

    for char in character_dict:
        character_keys.append(char)
        character_values.append(character_dict[char])
    
    for k in character_keys:
        assigned_character_dict["char"] = k
    
    for v in character_values:
        assigned_character_dict["num"] = v

    return assigned_character_dict
"""    
    #I was trying to create a single dictionary with all key-value pairs but since the keys do not have unique names 
    #('char' and 'num'), the loop just overwrites them every time
    #Boots advised me to instead create a LIST OF DICTIONARIES. Since each character is its own dictionary, no overwriting
    #should happen!