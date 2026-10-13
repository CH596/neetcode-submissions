from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_counter = Counter(nums)
        freq_list = [[] for i in range(len(nums)+1)]
        for item in freq_counter:
            freq_list[freq_counter[item]].append(item)
        flattend_list = []
        for row in freq_list:
            for j in row:
                flattend_list.append(j)
        return flattend_list[-k:]
        