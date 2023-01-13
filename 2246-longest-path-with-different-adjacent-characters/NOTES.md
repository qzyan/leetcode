length of the longest path of a node:
child_deepest + child_sec_deepest + 1
​
deepest depth of a node:
child_deepest + 1
​
init a golabl variable longest_path_len
when dfs a node,
1. calc all the child tree depth
2. calc the longest_len of the curr node(max_child_depth + sec_child_depth + 1)
3. compare longest_len of the curr node with the global variable longest_path_len
4. return the curr_depth(max_child_depth + 1)