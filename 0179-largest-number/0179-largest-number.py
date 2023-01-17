class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        sorted_nums = sorted(nums, key = cmp_to_key(self.comp), reverse = True)
        result = ''.join(map(str, sorted_nums))
        if result[0] == '0':
            return '0'
        return result
    
    def comp(self, a, b):
        if (str(a) + str(b) < str(b) + str(a)):
            return -1
        if (str(a) + str(b) > str(b) + str(a)):
            return 1
        return 0
        