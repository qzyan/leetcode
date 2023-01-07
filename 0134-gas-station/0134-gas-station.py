class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        curr_gas = 0
        start_idx = 0
        for idx in range(len(gas)):
            total_gas += gas[idx] - cost[idx]
            curr_gas += gas[idx] - cost[idx]
            if curr_gas < 0:
                start_idx = idx + 1
                curr_gas = 0
                
        return -1 if total_gas < 0 else start_idx
                