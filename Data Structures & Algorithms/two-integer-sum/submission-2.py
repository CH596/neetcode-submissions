class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_int_dict = {}
        for i in range(len(nums)):
            my_int_dict[nums[i]] = i
        print (my_int_dict)
        for j in range(len(nums)):
            if (target-nums[j] in my_int_dict):
                l = my_int_dict[target-nums[j]]
                if j != l:
                    return [j,my_int_dict[target-nums[j]]]
        return
        