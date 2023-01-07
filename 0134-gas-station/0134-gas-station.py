class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:        
        start_idx = 0
        while start_idx < len(gas):
            gas_in_tank = 0
            for step in range(len(gas)):
                curr_idx = (start_idx + step) % len(gas)
                gas_in_tank += gas[curr_idx] - cost[curr_idx]
                if gas_in_tank < 0:
                    start_idx = max(curr_idx, start_idx) + 1
                    break
            else:
                return start_idx
        
        return -1
                
            