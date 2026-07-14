class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Slicing
        if x<0:
            return False
        return str(x) == str(x)[::-1]

        # Brute Force:
        # if x<0:
        #     return False
        
        # original=x
        # reverse_num=0
        
        # while x>0:
        #     last_digit=(x%10)  # 1
        #     reverse_num= ( reverse_num * 10) + last_digit 
        #     x=(x//10) 
        # return original==reverse_num    
              