class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = collections.defaultdict(list)
        for s in strs:   
            counter = [0] * 26
            for i in s:
                counter[ord(i)-ord('a')]+=1
            sol[tuple(counter)].append(s)        
        return sol.values()
            
            