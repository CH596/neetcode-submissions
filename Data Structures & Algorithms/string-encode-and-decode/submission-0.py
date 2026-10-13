class Solution:

    def encode(self, strs: List[str]) -> str:
        new = []
        for i in range(len(strs)):
            str_len = len(strs[i])
            new_ele = [str(str_len),"#"]
            new.append(''.join(new_ele))
            new.append(strs[i])
        return ''.join(new)

    def find_next_delimiter(self,pos:int,strs:str) ->int:
        first_amp = pos
        while first_amp < len(strs):
            if  strs[first_amp] == "#":
                break
            else:
                first_amp +=1
        return first_amp


    def decode(self, s: str) -> List[str]:
        strs = []

        start = 0
        end = self.find_next_delimiter(start,s)
        while start < len(s) and end <= len(s):
            next_strs_len = int(s[start:end])
            next_str = s[end + 1:end + 1 + next_strs_len]
            strs.append(next_str)
            start = end + 1 + next_strs_len
            end = self.find_next_delimiter(start,s)
        return strs

