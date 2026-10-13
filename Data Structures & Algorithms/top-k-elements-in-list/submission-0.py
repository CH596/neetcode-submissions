from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_counter = Counter(nums)
        most_common_pairs = freq_counter.most_common(k)
        most_common_k = [row[0] for row in most_common_pairs]
        return most_common_k
        