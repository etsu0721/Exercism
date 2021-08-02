def distance(strand_a, strand_b):
    if len(strand_a) == len(strand_b):
        diffs = 0
        strands_zipped = [*zip(strand_a, strand_b)]
        for char1, char2 in strands_zipped:
            if char1 != char2:
                diffs += 1
        return diffs
    else:
        raise ValueError('The strands are of different lengths, so the Hamming distance cannot be computed.')