"""
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1 
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found)

https://leetcode.com/problems/design-hashmap/
"""

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket = []
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        found = False
        for i, j in enumerate(self.bucket):
            if key == j[0]:
                self.bucket[i] = (key, value)
                found = True
        if not found:
            self.bucket.append((key, value))
            
        
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        for (i, j) in self.bucket:
            if key == i:
                return j
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        for i, j in enumerate(self.bucket):
            if key == j[0]:
                del self.bucket[i]
        
        

"""
Your MyHashMap object will be instantiated and called as such:
Your input
["MyHashMap","put","put","get","get","put","get", "remove", "get"]
[[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]
Output
[null,null,null,1,-1,null,1,null,-1]
Expected
[null,null,null,1,-1,null,1,null,-1]
"""

