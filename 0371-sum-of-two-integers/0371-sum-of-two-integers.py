class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF  # 32-bit mask
        max_int = 0x7FFFFFFF  # Maximum positive 32-bit integer
        
        while b != 0:
            # XOR for addition without carry
            sum_without_carry = (a ^ b) & mask
            
            # AND and shift for carry
            carry = ((a & b) << 1) & mask
            
            # Update a and b
            a = sum_without_carry
            b = carry
        
        # Handle negative numbers
        return a if a <= max_int else ~(a ^ mask)