class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        memo_2_step = 1
        memo_1_step = 1
        for i in range(2,n+1):
                memo = memo_2_step+memo_1_step
                memo_2_step = memo_1_step
                memo_1_step = memo
        return memo



            