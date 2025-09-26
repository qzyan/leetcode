class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bit_count = [0] * 32
        for num in nums:
            for i in range(32):
                bit = num & 1
                num = num >> 1
                if bit == 1:
                    bit_count[i] += 1

        res = 0
        for bit, count in enumerate(bit_count):
            if count % 3 != 0:
                res += 1 << bit

        return res if bit_count[-1] % 3 == 0 else res - (1 << 32)