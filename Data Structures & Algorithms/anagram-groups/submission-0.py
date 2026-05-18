class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
     res = defaultdict(list)
     for n in strs:   
        s = "".join(sorted(n))
        res[s].append(n)
     return list(res.values())