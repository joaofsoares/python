import itertools  # import itertools to use groupby


def word_count(input_list):
    # create a function to get the tuple key
    def getKey(item):
        return item[0]

    # create a function to get the tuple value
    def getValue(item):
        return item[1]

    # flatmap the lists of input_list
    flatten_list = ''.join(list(map(lambda line: line + ' ', input_list)))

    # group by the word encountered into flatten_list
    result_list = [(key, sum(y for x, y in value)) for key, value in itertools.groupby(
        sorted(map(lambda w: (w, 1), flatten_list.split())), lambda x: x[0])]

    # return the list of counted words sorted by the highest number
    return sorted(result_list, key=getValue, reverse=True)


# create a list of strings. the model is used when you read a file with a lot of lines
counted_list = word_count(['this is a long string to test the development',
                           'here is another string just to test'])

# print into console the result
print(counted_list)
