def get_book_test(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()  
        return file_contents

def split_words_from_books(file_path):
    book_string = get_book_test(file_path)
    list_of_words = book_string.split()
    num_words = len(list_of_words)
    return num_words, list_of_words

def character_count(file_path):
    count_dict = {}
    num_words, list_of_words = split_words_from_books(file_path)
    for i in range(num_words):
        temp_word = list_of_words[i]
        temp_characters = list(temp_word)
        num_char = len(temp_characters)
        for j in range(num_char):
            chr = str(temp_characters[j].lower())
            if chr in count_dict:
                count_dict[chr] += 1
                count_dict[" "] += 1
            else:
                count_dict[chr] = 1
                count_dict[" "] = 1
    return num_words, list_of_words, count_dict

def sort_on(items):
    return items["num"]

def dict_sort(file_path):
    num_words, list_of_words, count_dict = character_count(file_path)
    sorted_list = []
    keys = ["char", "num"]
    for key in count_dict:
        values = [key, count_dict[key]]
        sorted_list.append(dict(zip(keys, values)))
    sorted_list.sort(reverse=True, key =sort_on)
    return sorted_list


