def pig_latin(word):
    first_letter = word[0]
    return word + 'ay' if first_letter in 'aeiou' else word[1:] + word[0] + 'ay'