def getNumberUniqueKmers(kmer_length):
    result = 1
    for x in xrange(kmer_length):
        result *= 4
    return result


if __name__ == '__main__':
    unique_kmers = getNumberUniqueKmers(9)

    prob_of_specific_kmer = 1 / (unique_kmers * 1.0)
    print prob_of_specific_kmer
    print prob_of_specific_kmer * prob_of_specific_kmer
