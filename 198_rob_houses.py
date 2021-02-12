class Solution(object):
    def rob(self, array):
        """
        :type nums: List[int]
        :rtype: int
        """
        #if i+k exists in the hashmap, return max_sum
        #else update map
        #Create a visited hash_map for storing max_sum at each i
        visited = [-1]*len(array) #Index: Max_sum

        #Start from the the 0th index and the 1st index
        #For every i, calculate max_sum from i+2 and i+3
        return max(self.rob_helper(array, 0, visited), 
                   self.rob_helper(array, 1, visited))
			
#len = 5
#visited = [-1, -1, -1, -1, 105]
#index = 3
#recursion stack = f(10-0) -> 10+ 90 + +105

    def rob_helper(self,array, index, visited):
        if len(array) == 0:
            return 0
        if len(array) == 1:
            return array[0]
        #return cached value
        if visited[index] != -1:
            return visited[index]
        if index >= len(array):
            return 0
        #calculate max
        if index+2 >= len(array):
            visited[index] = array[index]
        elif index+3 >= len(array):
            visited[index] = array[index] + self.rob_helper(array, index+2, visited)
        else:
            visited[index] = (array[index] + max(self.rob_helper(array, index+2, visited),
                                             self.rob_helper(array, index+3, visited)))
        return visited[index]
