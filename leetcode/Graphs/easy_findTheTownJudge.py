class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        dic = {}
        for arr in trust:
            firstVal = arr[0]
            secondVal = arr[1]
            if(firstVal not in dic):
                dic[firstVal] = -1
            else:
                dic[firstVal] -= 1
            if(secondVal not in dic):
                dic[secondVal] = 1
            else:
                dic[secondVal] += 1
        if(len(dic) == 0 and n == 1):
            return 1
        for val in dic:
            if(dic[val] == n-1):
                return val
        return -1