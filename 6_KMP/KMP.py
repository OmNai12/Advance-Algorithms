# By :- Om Nai


def LPS_Table(p, m):
    # The first one will be default zero as if no prefix and suffix for 0^th index.
    lpsTable = [0]
    # Hence, starting counter => i form the very next index.
    i = 1
    # Here k = 0 so if the match is to be found from the starting element
    k = 0
    while i != m:
        # Now if they are equal then for the longest common proper prefix which is also suffix we do the
        # following approach.
        if p[i] == p[k]:
            val = lpsTable[i - 1] + 1
            lpsTable.append(val)
            k += 1
        else:
            # If they are not equal then simply reset the k to 0.
            lpsTable.append(0)
            k = 0
        i += 1

    # Returning the LPS (THE LONGEST COMMON PROPER PREFIX WHICH IS ALSO SUFFIX) TABLE.
    # Also, called 𝝿 table.
    return lpsTable


def KMP(t, p):
    n = len(t)
    m = len(p)
    # Getting the LPS TABLE / 𝝿 TABLE.
    lpsTable = LPS_Table(p, m)
    # init to 0 used further for comparing.
    j = i = 0
    # Till the length of text.
    while i < n:
        # If text and pattern character matched.
        if t[i] == p[j]:
            i += 1
            j += 1
        # This means the pattern is matched.
        if j == m:
            # So, (i - m) will be the shift value as if i, will be to the last character matched, so it should
            # be to the initial index from where character matched.
            print("Pattern found at shift : ", (i - m))
            # In hope that this many characters are already matched.
            j = lpsTable[j - 1]
        elif (i < n) and (p[j] != t[i]):
            # Now if j > 0 so this sense that hope that this many characters are already matched, and so i
            # will be stayed at that place only.
            if j != 0:
                j = lpsTable[j - 1]
            else:
                # Now if j == 0 so means no character matched now let i to be incremented.
                i += 1

    pass


if __name__ == '__main__':
    text = "acaabcabaabccaaabcabaabccbbaa"
    pattern = "aab"
    KMP(text, pattern)
