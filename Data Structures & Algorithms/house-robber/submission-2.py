class Solution:
    def rob(self, nums: List[int]) -> int:
        j = len(nums)
        memo = {}
        def f(i):
            if i>= j:
                return 0
            if i >= j-2:
                return max(nums[i:])
            cost_list = []
            while i <= j-1:
                if i+2 in memo:
                    cost_list.append(nums[i]+memo[i+2])
                else:
                    next_cost = f(i+2)
                    memo[i+2] = next_cost
                    cost_list.append(nums[i]+next_cost)
                i+=1
            largest_return = max(cost_list)
            return largest_return
        return f(0)

        