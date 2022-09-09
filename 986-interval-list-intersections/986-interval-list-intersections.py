class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        i =0
        j = 0
        while i<len(firstList) and j<len(secondList):
            if secondList[j][0]<=firstList[i][1] and secondList[j][0]>=firstList[i][0]:
                res.append([secondList[j][0],min(firstList[i][1],secondList[j][1])])
            elif firstList[i][0]<=secondList[j][1] and firstList[i][0]>=secondList[j][0]:
                res.append([firstList[i][0],min(secondList[j][1],firstList[i][1])])
            if secondList[j][1]<firstList[i][1]:
                j+=1
            else:
                i+=1
        return res
            
        