'''
Word count script
'''
from itertools import groupby  # import groupby from itertools
import string  # import string


def transform_tuple(value):
    '''
    transform value in a tuple (value, 1)
    '''
    return value.translate(str.maketrans('', '', string.punctuation)), 1


def word_count(file):
    '''
    Receive a file and read all lines counting each word into the file
    '''
    # create a function to get the tuple key
    # def getKey(item):
    #   return item[0]

    # create a function to get the tuple value
    def get_value(item):
        return item[1]

    # open the file in another directory
    with open(file) as my_file:
        # get all lines from the file
        lines = my_file.readlines()

        # flat map the lists of lines
        flatten_list = ' '.join(lines)

        # create tuple for word and number
        tuple_list = list(map(transform_tuple, flatten_list.split()))

        # group by the word encountered into tuple_list
        result_list = [(key, sum(y for x, y in value)) for key, value
                       in groupby(sorted(tuple_list), lambda x: x[0])]

        # return the list of counted words sorted by the highest number
        return sorted(result_list, key=get_value, reverse=True)


# create a list of strings. the model is used when you read a file with a lot of lines
NUMBER_OF_WORDS = word_count('..\\iofile\\myfile.txt')

# print into console the result
print(NUMBER_OF_WORDS)
