import sys
from stats import split_words_from_books, character_count, dict_sort

def main():
    print("Usage: python3 main.py <path_to_book>\n")
    file_path = sys.argv[1]
    num_words, list_of_words, count_dict = character_count(file_path)
    sorted_list = dict_sort(file_path)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found " + str(num_words) + " total words")
    print("--------- Character Count -------")
    for i in range(len(sorted_list)):
        print(str(sorted_list[i]["char"]) + ": " + str(sorted_list[i]["num"]))
    print(sys.argv)
    return

main()
