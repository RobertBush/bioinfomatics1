from reverse_complement import get_reverse_complement
from numpy import diff
def sequence_finder(sequence, pattern):
    sequence_len = len(sequence)
    pattern_len = len(pattern)
    results = []
    range_length = sequence_len - pattern_len + 1
    for index in xrange(range_length ):
        sub_sequence = sequence[index : index + pattern_len]
        if(sub_sequence == pattern):
            results.append(index)
    return results

if __name__ == '__main__':
    line_count = 0
    for line in open('/Users/rbush/PycharmProjects/coursera/Vibrio_cholerae.txt', 'r'):
        sequence = line
        line_count+=1
        if line_count > 1:
            raise Exception('input file should be just one line')
    pattern = 'CTTGATCAT'
    hit_count = 0
    for hit_index in sequence_finder(sequence, pattern):
        hit_count+=1
        print("{}".format( hit_index))