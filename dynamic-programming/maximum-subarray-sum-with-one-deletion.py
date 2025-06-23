class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        no_delete_curr_max = arr[0]
        one_delete_curr_max = 0
        max_sum = arr[0]

        for i in range(1, len(arr)):
            no_delete_prev_max = no_delete_curr_max
            no_delete_curr_max = max(no_delete_prev_max + arr[i], arr[i])
            one_delete_curr_max = max(one_delete_curr_max + arr[i], no_delete_prev_max)
            max_sum = max(max_sum, no_delete_curr_max, one_delete_curr_max)

        return max_sum