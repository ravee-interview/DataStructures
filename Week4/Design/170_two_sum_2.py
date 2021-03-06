from collections import defaultdict
class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_map = defaultdict(int)
        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        self.hash_map[number]+=1
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for key,count in self.hash_map.items():
            complement = value - key
            print count
            print key
            if complement == key and count > 1:
                return True
            elif complement == key and count < 2:
                continue
            elif complement in self.hash_map:
                return True
        return False

"""
time complexity : o(n)
space complexity : o(n)
"""
# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)


