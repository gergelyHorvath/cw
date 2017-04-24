def recoverSecret(triplets):
    chars = []
    for t in triplets:
        chars += t
    chars = list(set(chars))
    dummy = chars[:]
    dummy = []
    while dummy != chars:
        dummy = chars[:]
        for t in triplets:
            i0 = chars.index(t[0])
            i1 = chars.index(t[1])
            i2 = chars.index(t[2])
            i0, i1, i2 = sorted([i0, i1, i2])
            chars = chars[:i0] + [t[0]] + chars[i0+1: i1] + [t[1]] + chars[i1+1: i2] + [t[2]] + chars[i2+1:]
    return ''.join(chars)


triplets = [['t', 's', 'f'], ['a', 's', 'u'], ['m', 'a', 'f'], ['a', 'i', 'n'], ['s', 'u', 'n'], ['m', 'f', 'u'], ['a', 't', 'h'], ['t', 'h', 'i'], ['h', 'i', 'f'], ['m', 'h', 'f'], ['a', 'u', 'n'], ['m', 'a', 't'], ['f', 'u', 'n'], ['h', 's', 'n'], ['a', 'i', 's'], ['m', 's', 'n'], ['m', 's', 'u']]

print(recoverSecret(triplets))
