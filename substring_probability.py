from itertools import product

from sequence_finder import sequence_finder

def substring_probability(string_length, alphabet_length, substring, appearances_of_pattern):
    # create an iterable of all possibilities as strings based on parameters
    alphabet = []
    for i in xrange(alphabet_length):
        alphabet.append(str(i))
    possibilities = product(alphabet, repeat=string_length)

    # count the number of substrings where the search pattern appears
    occurrences = 0
    total_possibilities = 0
    for i in possibilities:
        total_possibilities += 1
        possibility = ''.join(i)
        if possibility.count(substring) >= appearances_of_pattern:
        #if len(sequence_finder(possibility, substring)) >= appearances_of_pattern:
            occurrences += 1

    return (occurrences * 1.0) / total_possibilities


if __name__ == '__main__':
    print substring_probability(25, 2, '01', 1)