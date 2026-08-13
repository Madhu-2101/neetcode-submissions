class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        res1 = []
        # res = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s)
        for i in res.values():
            res1.append(i)
        print(res1)
        return res1

        