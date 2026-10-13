class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        j = len(cost)
        def f(i):
            if i <= 1:
                return 0
            if i in memo:
                return memo[i]
            last_pay = cost[i-1]
            second_to_last_pay = cost[i-2]
            option_2 = second_to_last_pay+f(i-2)
            option_1 = last_pay+f(i-1)
            pay = min(option_2,option_1)
            memo[i] = pay
            return pay
        return f(j)

        