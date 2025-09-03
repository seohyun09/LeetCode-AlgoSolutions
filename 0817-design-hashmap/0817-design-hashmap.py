class MyHashMap:

    def __init__(self):
        self.hash_map={}

    def put(self, key: int, value: int) -> None:
        self.hash_map[key]=value

    def get(self, key: int) -> int:
        if self.hash_map.get(key) is not None:
            return self.hash_map[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if self.hash_map.get(key) is not None:
            del self.hash_map[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)