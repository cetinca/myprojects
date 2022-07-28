def lengthOfLongestSubstring(s: str) -> int:
    seen = {}
    max_ = 0
    i = 0
    while i < len(s):
        c = s[i]
        if c in seen:
            i = seen[c]
            seen.clear()
        else:
            seen.update({c: i})
        max_ = max(max_, len(seen))
        i += 1
    return max_


print(lengthOfLongestSubstring("pwwkew"))
