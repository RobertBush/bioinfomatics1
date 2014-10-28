def pattern_count(sequence, pattern):
    sequence_len = len(sequence)
    pattern_len = len(pattern)
    count = 0
    range_length = sequence_len - pattern_len + 1
    for index in xrange(range_length ):
        sub_sequence = sequence[index : index + pattern_len]
        if(sub_sequence == pattern):
            count = count + 1
            print index
    return count

if __name__ == '__main__':
    sequence = 'atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaacctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgaccacggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgacttgtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggattacgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttaggatagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaattgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaagatcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtttccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc'
    pattern = 'atga'
    print pattern_count(sequence, pattern)