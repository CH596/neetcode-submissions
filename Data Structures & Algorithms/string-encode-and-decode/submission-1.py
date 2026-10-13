class Solution:

    def encode(self, strs: List[str]) -> str:
        new = []
        for i in range(len(strs)):
            str_len = len(strs[i])
            new_ele = [str(str_len),"#"]
            new.append(''.join(new_ele))
            new.append(strs[i])
        return ''.join(new)


    def decode(self, s: str) -> List[str]:
        strs = []
        start = 0
        end = s.find("#",start)
        while start < len(s):
            next_strs_len = int(s[start:end])
            next_str = s[end + 1:end + 1 + next_strs_len]
            strs.append(next_str)
            start = end + 1 + next_strs_len
            end = s.find("#",start)
        return strs

