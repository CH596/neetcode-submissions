class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_num_dict = {}
        for i in range(len(nums)):
            if nums[i] not in my_num_dict:
                my_num_dict[nums[i]] = i
            else:
                return True
        return False
        