class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        next_to_prev = n-1
        prev = n-2
        current = n-3
        f_next_prev = nums[n-1]
        f_prev= max(nums[n-1],nums[n-2])
        f = f_prev
        while current >= 0:
            f = max(nums[current]+f_next_prev,f_prev)
            f_next_prev = f_prev
            f_prev = f
            current -=1
        return f
        




        