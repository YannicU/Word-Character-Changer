# By YannicU

import os.path
import codecs

subdirectory = "word_ids"
output_directory = "output"

change_char = 'g'  # the character that will replace the original
remove_char_amount = 1  # this number will remove the letters of the original words
filter_length = 4  # the length of the changed words have to be greater or equal than this number to be accepted

to_change_word_ids = []  # this inherits the ids of the words that will be changed
to_change_word_list = []  # this inherits the words that need to be changed and checked
word_reference_list = []  # this will be used to see if the changed words are valid
original_words = []  # inherits all original words that have been changed
dictionary = {}  # this inherits the words that have been changed and are valid with their originals
flipped_dictionary = {}  # "dictionary" but flipped

file_path = f"output\\{change_char}.txt"
file = ''
file_sorted = ''
if os.path.isfile(file_path) is True:
    print(f'File with "{change_char}" characters already exist!')
    user_input = input('Overwrite existing file? [y/n]: ')
    continue_condition = False
    while not continue_condition:
        if user_input == 'y':
            file = open(os.path.join(output_directory, f'{change_char}.txt'), 'w')
            file_sorted = open(os.path.join(output_directory, f'{change_char}_sorted.txt'), 'w')
            continue_condition = True
            pass
        elif user_input == 'n':
            quit()
        else:
            print('Wrong input')
            user_input = input('Overwrite existing file? [y/n]: ')
else:
    file = open(os.path.join(output_directory, f'{change_char}.txt'), 'x')
    file_sorted = open(os.path.join(output_directory, f'{change_char}_sorted.txt'), 'x')

word_ids = open("word_ids.txt", "r").read().split(" ")
for word_id in word_ids:
    # this will find the ids of the character that you want to be changed
    if change_char not in word_id[0:1]:
        to_change_word_ids.append(word_id)
    # this will compare the new words to the originals, to see if they are valid
    word_references = codecs.open(os.path.join(subdirectory, f'w_{word_id}.txt'), 'r', 'utf-8').read().splitlines()
    for word_reference in word_references:
        word_reference_list.append(word_reference.lower())

for ids in to_change_word_ids:  # this will look for all words that need to be changed
    to_change_words = codecs.open(os.path.join(subdirectory, f'w_{ids}.txt'), 'r', 'utf-8').read().splitlines()
    for to_change_word in to_change_words:
        to_change_word_list.append(to_change_word.lower())

print(f'Total Words: {len(word_reference_list)}')  # all words from the files
print(f'Words that need to be changed and checked: {len(to_change_word_list)}')

reset_counter = 0  # for controlling the update period of the progress
for word in to_change_word_list:
    reset_counter += 1
    progress = round(((100 / len(to_change_word_list)) * (to_change_word_list.index(word) + 1)), 2)
    if str(progress * 10).split('.')[1] == '0':
        progress = f'{progress}0'
    if int(str(progress).split('.')[0]) < 10:
        progress = f'0{progress}'
    if reset_counter == 500:
        print(f'Progress: {progress}%')
        reset_counter = 0
    if word[len(word) - 1:] == '-':
        word = word[:-1]
    if word[0:1] == '-':
        word = word[1:]
    original_word = word.lower()
    changed_word = f'{change_char}{word[remove_char_amount:]}'.lower()  # this will be the changed word
    if changed_word in word_reference_list:  # this looks if the words are valid
        if original_word not in original_words:  # this will look for duplicates
            if len(changed_word) >= filter_length:  # this will filter out all words under a certain length
                dictionary[original_word] = changed_word
                original_words.append(original_word)
                print(f'Progress: {progress}%    {len(dictionary)}. {original_word} ===> {changed_word}')
                reset_counter = 0

for key in dictionary:
    flipped_dictionary[key] = [dictionary[key]]
    file.write(f'{key} ===> {dictionary[key]}\n')

sorted_dictionary = {k: v for k, v in sorted(flipped_dictionary.items(), key=lambda item: item[1])}
sort_number = 0
for key, value in sorted_dictionary.items():
    sort_number += 1
    file_sorted.write(f'{value[0]} ===> {key}\n')

file.close()
file_sorted.close()
print(f'{len(dictionary)} changed words!')

