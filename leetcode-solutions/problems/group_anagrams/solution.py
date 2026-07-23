class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        grp={}
        for str in strs:
            key="".join(sorted(str))
            grp.setdefault(key,[]).append(str)
            
        return list(grp.values())