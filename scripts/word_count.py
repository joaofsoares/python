from itertools import groupby  # import groupby from itertools


def word_count(file):

    # create a function to get the tuple key
    # def getKey(item):
    #   return item[0]

    # create a function to get the tuple value
    def getValue(item):
        return item[1]

    # open the file in another directory
    with open(file) as my_file:
        # get all lines from the file
        lines = my_file.readlines()

        # flatmap the lists of input_list
        flatten_list = ''.join([line.replace('\n', ' ') for line in lines])

        # create tuple for word and number
        tuple_list = [(word, 1) for word in flatten_list.split()]

        # group by the word encountered into tuple_list
        result_list = [(key, sum(y for x, y in value)) for key,
                       value in groupby(sorted(tuple_list), lambda x: x[0])]

        # return the list of counted words sorted by the highest number
        return sorted(result_list, key=getValue, reverse=True)


# create a list of strings. the model is used when you read a file with a lot of lines
number_of_words = word_count('..\\iofile\\myfile.txt')

# print into console the result
print(number_of_words)
