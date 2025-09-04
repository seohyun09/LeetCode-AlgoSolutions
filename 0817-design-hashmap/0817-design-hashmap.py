class Node:
    def __init__(self, key, val):
        self.key=key
        self.val=val
        self.next=None

class MyHashMap:

    def __init__(self):
        self.size=1000000
        self.hash_map=[None]*self.size

    def put(self, key: int, value: int) -> None:
        index=key%self.size
        if self.hash_map[index] is None:
            self.hash_map[index]=Node(key, value)
            return
        node=self.hash_map[index]
        while node:
            if node.key==key:
                node.val=value
                return
            if node.next:
                node=node.next
            else:
                break
        node.next=Node(key, value)
        return

    def get(self, key: int) -> int:
        index=key%self.size
        if self.hash_map[index] is None:
            return -1
        node=self.hash_map[index]
        while node:
            if node.key==key:
                return node.val
            node=node.next
        return -1

    def remove(self, key: int) -> None:
        index=key%self.size
        if self.hash_map[index] is None:
            return
        node=self.hash_map[index]
        if node.key==key:
            if node.next is None:
                self.hash_map[index]=None
            else:
                self.hash_map[index]=node.next
        prev=node
        while node:
            if node.key==key:
                prev.next=node.next
                return
            prev=node
            node=node.next
        return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)