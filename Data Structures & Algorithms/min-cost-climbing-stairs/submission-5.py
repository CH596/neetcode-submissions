class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        j = len(cost)
        def f(i):
            if i >= j-1:
                return 0
            if i in memo:
                return memo[i]
            first_pay = cost[i]
            second_pay = cost[i+1]
            option_2 = second_pay+f(i+2)
            option_1 = first_pay+f(i+1)
            pay = min(option_2,option_1)
            memo[i] = pay
            return pay
        return f(0)
        