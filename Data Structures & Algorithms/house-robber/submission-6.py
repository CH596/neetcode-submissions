class Solution:
    def rob(self, nums: List[int]) -> int:
        j = len(nums)
        memo = {}
        def f(i):
            if i in memo:
                return memo[i]
            if i>= j:
                return 0
            skip = f(i+1)
            skip_to_next = f(i+2)
            max_value = max(nums[i]+skip_to_next,skip)
            memo[i] = max_value
            return max_value
        return f(0)

           


        