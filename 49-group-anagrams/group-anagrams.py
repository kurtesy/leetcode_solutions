class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Strategy is to sort each string and then check for anagram
        # Next is to form groups with original strings by index based storage
        result = []
        anaMap = {}
        for index, s in enumerate(strs):
            subStr = ''.join(sorted(s))
            if subStr in anaMap:
                anaMap[subStr].append(index)
            else:
                anaMap[subStr] = [index]
        for val in anaMap.values():
            temp = []
            print(len(s))
            for index in val:
                temp.append(strs[index])
            result.append(temp)
        return result

        