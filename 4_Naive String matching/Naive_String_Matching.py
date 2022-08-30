# By :- Om Nai


# This the naive string matching algorithm which takes text and pattern as a parameters to the function
def Naive_String_Matching(t, p):
    # N is the length of text
    n = len(t)
    # m is the length of pattern
    m = len(p)
    # Here s is the shift
    s = 0

    # Now n - m + 1, as if the last matching sting's will not be covered as if,
    # range(5) means 0, 1, 2, 3, 4 so the last matching string's
    # index we want to cover
    for s in range(n - m + 1):
        # i = j = 1
        i = 0
        j = 0
        while j < m and (t[s + i] == p[j]):
            i += 1
            j += 1

        # As if, after last pass in while loop j will having same value as of m
        if j == m:
            print("Pattern found at shift : ", s)

    pass


if __name__ == "__main__":
    text = "acaabcabaabccaaabcabaabccbbaa"
    pattern = "aab"
    Naive_String_Matching(text, pattern)
