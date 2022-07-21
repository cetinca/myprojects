"""Find the longest substring of a string
"""


def find_longest_subs(txt):
    res = ""
    len_ = len(txt)
    for i in range(len_):
        for j in range(i, len_):
            subs = txt[i:j + 1]
            if len(subs) == len(set(subs)) and len(subs) > len(res):
                res = subs

    return res


print(find_longest_subs("abbcdaxyuwub"))