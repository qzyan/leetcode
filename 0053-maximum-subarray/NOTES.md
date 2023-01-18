init a curr_sum -> 0
init a max_sum -> -float('inf')
iterate over the num
curr_sum = max(curr_sum, 0) + nums[i]
max_sum = max(max_sum, curr_sum)