def getKmerDictionary(sequence, k):
    sequence_len = len(sequence)
    range_length = sequence_len - k + 1
    sequences = {}
    for index in xrange(range_length):
        sub_pattern = sequence[index:index + k]
        if sub_pattern in sequences:
            sequences[sub_pattern].append(index)
        else:
            sequences[sub_pattern] = [index]
    return sequences

def getMostFrequentKmer(sequence, k):
    kmer_dictionary = getKmerDictionary(sequence, k)
    highest_frequency = 0
    result = []
    for key in kmer_dictionary.keys():
        value = len(kmer_dictionary[key])
        if value == highest_frequency:
            result.append((key, value))
            continue
        if value > highest_frequency:
            result = []
            result.append((key, value))
            highest_frequency = value
    return result

if __name__ == '__main__':
    k = 9
    sequence = ''
    line_count = 0
    for line in open('/Users/rbush/PycharmProjects/coursera/Thermotoga-petrophila.txt', 'r'):
        sequence = line
        line_count += 1
        if line_count > 1:
            raise Exception('input file should be just one line')
    print getMostFrequentKmer(sequence, k)