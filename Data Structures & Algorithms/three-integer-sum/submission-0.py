class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numsSorted = sorted(nums)
        res = []
        for i in range(len(numsSorted)-2):
            target = numsSorted[i] * -1 
            l = i + 1
            r = len(numsSorted)-1
            while l<r:
                if (numsSorted[l] + numsSorted[r]) == target:
                    res.append((numsSorted[i],numsSorted[l],numsSorted[r]))
                    l+=1
                elif (numsSorted[l] + numsSorted[r]) > target:
                    r-=1
                else:
                    l+=1
        return list(set(res))
        """
        unique = []
        for item in res:
            if item not in unique:
                unique.append(item)
        return unique
        """




            
