def wspolne_elementy(seq1, seq2):
    return list(set(seq1) & set(seq2))

print(wspolne_elementy([1, 2, 3, 4], [3, 4, 5, 6]))
