"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo = 1
        hi = num
        while lo <= hi:
            mi = (lo + hi)//2
            mi_sqrt = mi * mi
            if mi_sqrt == num:
                return True
            elif mi_sqrt < num:
                lo = mi + 1
            else:
                hi = mi - 1
        
        return False