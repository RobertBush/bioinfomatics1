from most_common_kmers import getKmerDictionary
from reverse_complement import get_reverse_complement
def find_clumps(sequence, window_length, kmer_length, kmer_reps):
    kmers = getKmerDictionary(sequence, kmer_length)
    results = []
    for kmer in kmers:
        frequency = len(kmers[kmer])
        if frequency < kmer_reps:
            continue
        hits = kmers[kmer]
        start_index = 0
        end_index = kmer_reps - 1
        while end_index <= len(hits) -1 :
            if hits[end_index] - hits[start_index] <= (window_length - kmer_length) and kmer not in results:
                results.append(kmer)
            start_index += 1
            end_index += 1
    return results

if __name__ == '__main__':
    sequence = ''
    line_count = 0
    for line in open('/Users/rbush/git/coursera/bioinfomatics1/E-coli.txt', 'r'):
        sequence = line
        line_count += 1
        if line_count > 1:
            raise Exception('input file should be just one line')
    clump_kmers = find_clumps(sequence, 500, 9, 3)
    print len(clump_kmers)