class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # # Approach 1:
        # return len(nums) != len(set(nums))
        # # TC: O(n), SC:O(n)

        
        # Approach 2 : Stops at k index when found
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False    
        # TC: O(n), SC:O(n)