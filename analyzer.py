"""
Dictionary - https://docs.python.org/3/tutorial/datastructures.html
Reading and Writing Files - https://docs.python.org/3/tutorial/inputoutput.html
Sorting - https://docs.python.org/3/howto/sorting.html
"""


def start(filepath_open, check1_value, check2_value, radio1_value, radio2_value, filepath_save):
    """Funckja wykonująca"""
    dictionary = dict()
    if check1_value == 0 and check2_value == 0:
        exit()
    elif check1_value == 1 and check2_value == 0:
        word_count(filepath_open, dictionary)
        sorted_dictionary = sort(dictionary, radio1_value, radio2_value)
        print_in(filepath_save, 1, dictionary, sorted_dictionary)
    elif check1_value == 0 and check2_value == 1:
        letter_count(filepath_open, dictionary)
        sorted_dictionary = sort(dictionary, radio1_value, radio2_value)
        print_in(filepath_save, 2, dictionary, sorted_dictionary)
    else:
        word_count(filepath_open, dictionary)
        sorted_dictionary = sort(dictionary, radio1_value, radio2_value)
        print_in(filepath_save, 1, dictionary, sorted_dictionary)
        dictionary.clear()
        letter_count(filepath_open, dictionary)
        sorted_dictionary = sort(dictionary, radio1_value, radio2_value)
        print_in(filepath_save, 3, dictionary, sorted_dictionary)


def word_count(filepath_open, dictionary):
    """Oblicz wyrazy w tekście"""
    file_get = open(filepath_open, 'r', encoding='utf-8')
    text = file_get.read().lower().split()
    file_get.close()
    chars = [".", ",", "?", "-", ":", ";", "'", '"']

    for char in chars:
        text = [word.replace(char, "") for word in text]

    for word in text:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary


def letter_count(filepath_open, dictionary):
    """Oblicz litery w tekście"""
    file_get = open(filepath_open, 'r', encoding='utf-8')
    text = file_get.read().lower().strip()
    file_get.close()
    chars = [".", ",", "?", "-", ":", ";", "'", '"']

    for char in chars:
        text = [word.replace(char, "") for word in text]

    for letter in text:
        if letter.isalpha():
            if letter in dictionary:
                dictionary[letter] += 1
            else:
                dictionary[letter] = 1
    return dictionary


def sort(dictionary, sort_by, organize):
    """Sortowanie wyrazów/liter w słowniku"""
    if sort_by == 0 and organize == 0:
        sorted_dictionary = sorted(dictionary)
    elif sort_by == 0 and organize == 1:
        sorted_dictionary = sorted(dictionary, reverse=True)
    elif sort_by == 1 and organize == 0:
        sorted_dictionary = sorted(dictionary, key=dictionary.get)
    else:
        sorted_dictionary = sorted(dictionary, key=dictionary.get, reverse=True)
    return sorted_dictionary


def print_in(filepath_save, write, dictionary, sorted_dictionary):
    """Wypisywanie słownika w pliku wyjściowym"""
    if write == 1:
        file_set = open(filepath_save, 'w', encoding='utf-8')
        file_set.write("Liczba słów: " + str(len(dictionary)) + '\n')
        file_set.write("Liczba słów w tekście: " + str(sum(dictionary.values())) + '\n')
        for word in sorted_dictionary:
            file_set.write(word + ' : ' + str(dictionary[word]) + '\n')
        file_set.close()
    elif write == 2:
        file_set = open(filepath_save, 'w', encoding='utf-8')
        file_set.write("Liczba znaków: " + str(len(dictionary)) + '\n')
        file_set.write("Liczba znaków w tekście: " + str(sum(dictionary.values())) + '\n')
        for char in sorted_dictionary:
            file_set.write(char + ' : ' + str(dictionary[char]) + '\n')
        file_set.close()
    elif write == 3:
        file_set = open(filepath_save, 'a', encoding='utf-8')
        file_set.write("Liczba znaków: " + str(len(dictionary)) + '\n')
        file_set.write("Liczba znaków w tekście: " + str(sum(dictionary.values())) + '\n')
        for char in sorted_dictionary:
            file_set.write(char + ' : ' + str(dictionary[char]) + '\n')
        file_set.close()
    else:
        print("error")
