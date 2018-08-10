'''
Word count script with counter
'''
from itertools import groupby  # import groupby from itertools
from collections import Counter  # import Counter from collections
import string


def word_count(file):
    '''
    Receive a file and read all lines counting each word into the file
    '''

    # create a function to get the tuple value
    def get_value(item):
        return item[1]

    # transform the dictionary in a list
    def return_key_value_dictionary(dic):
        return [(key, value) for key, value in dic.items()]

    # clean punctuation of a list
    def clean_punctuation(string_list):
        return list(map(lambda x: x.translate(str.maketrans('', '', string.punctuation)), string_list))

    # open the file in another directory
    with open(file) as my_file:
        # get all lines from the file
        lines = my_file.readlines()

        # flat map the lists of lines
        flatten_list = ' '.join(lines)

        # clean words with punctuation
        cleaned_list = clean_punctuation(flatten_list.split())

        # create the result dictionary using Counter
        result_dictionary = Counter(cleaned_list)

        # create a list based on result_dictionary
        result_list = return_key_value_dictionary(result_dictionary)

        # return the list of counted words sorted by the highest number
        return sorted(result_list, key=get_value, reverse=True)


# create a list of strings. the model is used when you read a file with a lot of lines
NUMBER_OF_WORDS = word_count('..\\iofile\\myfile.txt')

# print into console the result
print(NUMBER_OF_WORDS)
