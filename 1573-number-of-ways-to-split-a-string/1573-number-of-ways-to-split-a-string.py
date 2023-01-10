class Solution:
    def numWays(self, s: str) -> int:
        # count the number of 1
        # if count % 3 != 0 return 0
        # count_1_each_section = num_1 / 3
        
        # iterate over the s
        # count the curr number of 1
        # when have count_1_each_section
        # calc the number of slots between the next 1
        M = 10 ** 9 + 7
        
        count_1 = 0
        for char in s:
            if char == '1':
                count_1 += 1
        
        if count_1 == 0:
            return ((len(s) - 1) * (len(s) - 2) // 2)% M
        
        if count_1 % 3 != 0:
            return 0
        
        count_1_each_section = count_1 // 3
        
        count_1 = 0
        first_slot_count = 0
        second_slot_count = 0
        for char in s:           
            if char == '1':
                count_1 += 1
                
            if count_1 == count_1_each_section:
                first_slot_count += 1
                
            if count_1 == count_1_each_section * 2:
                second_slot_count += 1
                
        return (first_slot_count % M * second_slot_count % M) % M