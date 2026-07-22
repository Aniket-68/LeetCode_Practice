class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        # return Counter(s) == Counter(t) #nlogn
        
        # return sorted(s) == sorted(t) # nlogn


        # HashMap Approach : Approach 1
        freq={}
        for ch in s:
        #   if ch not in t:
        #     return False # O(n) --> Since List, String,tuple
          freq[ch]=freq.get(ch,0)+1 


        for ch in t:
            if ch not in freq: # O(1) Lookup since dict, set
                return False
            freq[ch]-=1
            
            if freq[ch] <0:
                return False
        return True

            
        
             
        
        