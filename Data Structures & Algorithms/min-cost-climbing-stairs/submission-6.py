class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if len(cost) < 1:
            return 0 
        if len(cost) == 1:
            return cost[0]
        index_1 = 0
        index_2 = 1
        cost_1 = 0
        cost_2 = 0
        new_cost = min(cost_1,cost_2)
        new_index = 2
        while new_index <= n:
            new_cost = min(cost[new_index-1]+cost_2,cost[new_index-2]+cost_1)
            cost_1, cost_2 = cost_2, new_cost
            new_index+=1
        return new_cost

        