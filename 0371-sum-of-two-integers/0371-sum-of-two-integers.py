class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        mask_int = 0x7FFFFFFF
        
        while b != 0:
            total = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a = total
            b = carry
        return a if a <= mask_int else ~(a ^ mask)
        