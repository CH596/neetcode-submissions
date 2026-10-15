class Solution:
    def rob(self, nums: List[int]) -> int:
        j = len(nums)
        memo = {}
        def f(i):
            if i>= j:
                return 0
            if i+1 in memo:
                next = memo[i+1]
            else:
                next = f(i+1)
                memo[i+1] = next
            if i+2 in memo:
                next_to_next = memo[i+2]
            else:
                next_to_next = f(i+2)
                memo[i+2] = next_to_next
            return max(nums[i]+next_to_next,next)
        return f(0)

           


        