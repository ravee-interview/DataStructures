class ListNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
    
    def insert(self,key,value):
        head = self #points to dummy head
        while head and head.next:
            #check if key already exists, if yes replace
            if head.key == key:
                head.value = value
                return
            head = head.next
        if head and head.key == key:
            head.value = value
            return
        head.next = ListNode(key,value)
        
    def get(self,key):
        head = self #points to dummy head
        head = head.next
        while head:
            if head.key == key:
                return head.value
            head = head.next
        return -1

    def remove(self,key):
        head = self
        while head and head.next and head.next.key!=key:
            head = head.next
            
        if head and head.next:
            head.next = head.next.next
        
        
class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 997
        self.hash_map = [None] * self.size
        for i in range(self.size):
            self.hash_map[i] = ListNode(-1,-1)
        
    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        hash_key = hash(key) % self.size
        head = self.hash_map[hash_key]
        head.insert(key,value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hash_key = hash(key) % self.size
        head = self.hash_map[hash_key]
        return head.get(key)
        
    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        hash_key = hash(key) % self.size
        head = self.hash_map[hash_key]
        head.remove(key)

        
        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


#for hashmap what all calirfying questions can i ask?
"""
[1 2 3 4 5 6 7]
 |
( )
 |
( )
"""

