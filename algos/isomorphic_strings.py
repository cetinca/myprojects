def isIsomorphic(s: str, t: str) -> bool:
    memo = {}
    memo_rev = {}
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i] not in memo:
            memo.update({s[i]: t[i]})
        if t[i] not in memo_rev:
            memo_rev.update({t[i]: s[i]})
        if memo[s[i]] != t[i] or memo_rev[t[i]] != s[i]:
            return False
    return True


print(isIsomorphic("abca", "defd"))
print(isIsomorphic("abcx", "defd"))
print(isIsomorphic("abca", "defx"))
print(isIsomorphic("abc", "de"))
print(isIsomorphic("abc", "deff"))
