class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        left = [gas[i] - cost[i] for i in range(len(cost))]

        if sum(left) < 0:
            return -1

        gas_in_tank = 0
        start_idx = 0
        for i in range(len(left)):
            gas_in_tank += left[i]
            if gas_in_tank < 0:
                gas_in_tank = 0
                start_idx = i + 1

        return start_idx