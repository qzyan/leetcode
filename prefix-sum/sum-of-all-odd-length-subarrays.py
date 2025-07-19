class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        n = len(arr)
        for i in range(len(arr)):
            res += ((i + 1) * (n - i) + 1) // 2 * arr[i]

        return res