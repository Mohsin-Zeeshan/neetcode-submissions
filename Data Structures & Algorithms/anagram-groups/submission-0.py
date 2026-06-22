class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = {}

        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            if key in maps:
                maps[key].append(strs[i])   # bucket exists, drop the word in
            else:
                maps[key] = [strs[i]]       # first word for this key, start a new list
        return list(maps.values())