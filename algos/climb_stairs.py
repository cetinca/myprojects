class Solution:
    def climbStairs(self, n: int) -> int:
        # a = b = 1
        # for _ in range(n):
        #     a, b = b, a + b
        # return a
        # last two distinct way is the current distinct way
        # last two distinct way is the current distinct way
        memo = dict()
        memo[1] = 1
        memo[2] = 2

        def climb(n):
            if n in memo:  # if the recursion already done before first take a look-up in the look-up table
                return memo[n]
            else:  # Store the recursion function in the look-up table and return the stored look-up table function
                memo[n] = climb(n - 1) + climb(n - 2)
                return memo[n]

        return climb(n)


print(Solution().climbStairs(5))
