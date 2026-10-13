class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_letter_dict = {}
        for i in range(len(strs)):
            keys = ''.join(sorted(strs[i]))
            if keys in my_letter_dict:
                my_letter_dict[keys].append(strs[i])
            else:
                my_letter_dict[keys] = [strs[i]]
        return list(my_letter_dict.values())

        