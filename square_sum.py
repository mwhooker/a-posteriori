"""
arrange the numbers 1-15 such that each adjacent pair of numbers sums to
a square

[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]

[
(1, 3), (1, 8), (2, 2), (2, 7), (2, 14), (3, 1), (3, 6), (3, 13), (4, 5),
(4, 12), (5, 4), (5, 11), (6, 3), (6, 10), (7, 2), (7, 9), (8, 1), (8, 8),
(9, 7), (10, 6), (11, 5), (11, 14), (12, 4), (12, 13), (13, 3), (13, 12),
(14, 2), (14, 11)
]

(1, (3, (6, 10), (13, 12)), (8), (15, 10))
"""


from collections import defaultdict
from pprint import pprint as pp
from itertools import izip_longest


def do(lhs, pairs):
    ret = [lhs]
    for p in pairs:
        if p[0] == lhs:
            pairs_cp = [x for x in pairs if x != p]
            ret.append(do(p[1], pairs_cp))

    return ret


def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

def find_paths(head, tail):
    if not tail:
        return

    for lhs, rhs in grouper(tail, 2):
        print lhs
        if lhs not in head:
            head.append(lhs)
            find_paths(head, rhs)
    return
    if len(head) == 15:
        pp( head)



if __name__ == '__main__':
    size = 15
    squares = [i *i for i in xrange(1, size+1)]
    map = defaultdict(list)
    for i in xrange(1, size+1):
        for j in xrange(1, size+1):
            if i + j in squares:
                map[i + j].append( (i, j))

    pairs = []
    for p in map:
        pairs.extend(map[p])

    pairs.sort()
    print "pairs:", pairs
    paths = []
    for i in xrange(1, size+1):
        find_paths([], do(i, pairs))


    """
    for i in xrange(15):
        x = paths[i]
        if isinstance(x, list):
            x = x[0]
        pp(x)
    """

