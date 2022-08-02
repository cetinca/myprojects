class Solution:
    def isValid(self, s: str) -> bool:
        par = {")": "(", "]": "[", "}": "{"}
        stack = []

        for i in range(len(s)):
            if s[i] in par.values():
                stack.append(s[i])
            elif not stack:
                return False
            else:
                if stack[-1] != par[s[i]]:
                    return False
                else:
                    stack.pop()

        return stack == []