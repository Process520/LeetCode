class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        if ( len(nums)*len(nums[0]) ) != (r*c):
            return nums
        
        
        List = [ [0 for x in range(c)] for y in range(r)]

        # List = []
        # for i in range(r):
        #     List.append([])
        #     for j in range(c):
        #         List[i].append(0)
        count = 0
        for rows in nums:
            for num in rows:
                List[count/c][count%c] = num
                count = count + 1
        return List
