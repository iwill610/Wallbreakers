class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        hashSet={}
        global hashSet
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        hashSet[key]=key

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        
        if key in hashSet:
            del hashSet[key]
        


    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        if key in hashSet:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)