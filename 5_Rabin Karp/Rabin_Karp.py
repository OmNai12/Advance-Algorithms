# By :- Om Nai


def Hash_Value_Generator(str: str, lengthOfStr):
    hashValue = 0
    for i in range(lengthOfStr):
        hashValue = hashValue + (ord(str[i])) * (10 ** (lengthOfStr - i - 1))

    return hashValue


def Rabin_Karp(t, p):
    n = len(t)
    m = len(p)

    hashValueOfPattern = Hash_Value_Generator(p, m)
    # Pre calculation
    tempStr = t[0:m]
    hashValueOfText = Hash_Value_Generator(tempStr, len(tempStr))
    for s in range(n - m + 1):
        if hashValueOfPattern == hashValueOfText:
            # If values same then only each character is compared
            j = 0
            i = 0
            while j < m and (t[s + i] == p[j]):
                i += 1
                j += 1

            if j == m:
                print("Pattern found at shift : ", s)

        # The starting char removed
        if s < n - m:
            hashValueOfText = hashValueOfText - (ord(t[s]) * (10 ** (m - 1)))
            # Adding of the char
            hashValueOfText = hashValueOfText * 10
            hashValueOfText = hashValueOfText + ord(t[s + m])


if __name__ == "__main__":
    text = "acaabcabaabccaaabcabaabccbbaa"
    pattern = "aab"
    Rabin_Karp(text, pattern)
