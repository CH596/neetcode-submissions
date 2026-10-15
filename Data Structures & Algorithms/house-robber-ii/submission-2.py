class Solution:
     def rob_sub(self,nums:List[int])->int:
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
     def rob(self, nums: List[int]) -> int:
            if len(nums) <= 1:
                return nums[0]
            choice_1 = self.rob_sub(nums[1:])
            choice_2 = self.rob_sub(nums[:-1])
            return max(choice_1,choice_2)