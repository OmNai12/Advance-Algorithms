# By :- Om Nai

def Naive_String_Matching(t, p):

    n = len(t)
    m = len(p)
    s = 0

    for s in range(n - m + 1):
        # i = j = 1
        i = 0
        j = 0
        while j < m and (t[s + i] == p[j]):
            i += 1
            j += 1

        if j == (m):
            print("Pattern found at shift : ", s)

    pass


if __name__ == "__main__":
    text = "acaabcabaabccaaabcabaabccbbaa"
    pattern = "aab"
    Naive_String_Matching(text, pattern)
