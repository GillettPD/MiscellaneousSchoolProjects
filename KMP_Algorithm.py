
my_txt = 'ACDEFAGGGAVCDABCAGABCADCCCCCDABABCAGABCADDFAAOOOBBBB'

my_pat = 'ABCAGABCADDG'

pi_table = [-1, -1, -1, 0, -1, 0, 1, 2, 3, -1, -1, -1]


def kmp_prefix_matcher (txt, pat, pi_table):
    (n, m) = len(txt), len(pat)
    i = -1
    j = -1
    f = -1
    g = 0
    while i < n-1:
        if pat[j+1] == txt[i+1]:
            (i, j) = (i+1, j+1)
            if j + 1 > g:
                f = i
                g = j + 1
        else:
            if j == -1:
                i = i+1
            else:
                j = pi_table[j]
        if j == m-1:
            print(f'Pattern matched at position {i}')
            j = pi_table[j]
        else:
            if i == n-2:
                print(f'Longest match of length {g} ends at position {f}')


kmp_prefix_matcher(my_txt, my_pat, pi_table)
