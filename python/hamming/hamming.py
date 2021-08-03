def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('The strands are of different lengths, so the Hamming distance cannot be computed.')
    return sum([1 for char1, char2 in zip(strand_a, strand_b) if char1 != char2])
