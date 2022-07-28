def isSubsequence(s: str, t: str) -> bool:
    if len(t) < len(s): return False
    if len(s) == 0: return True
    i = 0
    j = 0
    x = ""
    while i < len(s) and j < len(t):
        if s[i] != t[j]:
            j += 1
        else:
            i, j, x = i + 1, j + 1, x + s[i]

    return True if x == s else False


print(isSubsequence("abc", "abyuc"))
