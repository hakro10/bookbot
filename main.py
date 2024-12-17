#! /usr/bin/env python3

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        return file_contents
        

def count_words():
    words= main().split() 
    return len(words)
        

def count_characters():
    chars_dict = {}
    words = main().split()
        
    for word in words:          
        for char in word:
            if char.isalpha():          
                if char.lower() not in chars_dict:
                    chars_dict[char.lower()] = 1                  
                else:
                    chars_dict[char.lower()] += 1
    # print(chars_dict)  
    # for key, value in chars_dict.items():
    #     print(f"The '{key}' character was found {value} times")
        
    return chars_dict
        
# code under this line is not sorted:

# sorted

chars_dict = count_characters()  

def sort_on(dict): # sort dictionary by how many times a character appears   
    for key, value in dict.items():  
        return value
    
chars_of_dicts = []

for key, value in chars_dict.items():
    new_dict = {key:value}
    chars_of_dicts.append(new_dict)
    
chars_of_dicts.sort(reverse=True, key=sort_on)

def report():
    for letter in chars_of_dicts:
        for key, value in letter.items():
            print(f"The '{key}' character was found {value} times")
    # return chars_of_dicts

print('--- Begin report of books/frankenstein.txt ---')
print(f'{count_words()} words found in the document')
report()
print('--- End report ---')


main()
