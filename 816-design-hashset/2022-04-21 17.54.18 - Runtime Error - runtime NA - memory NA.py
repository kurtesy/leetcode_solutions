class MyHashSet:

    def __init__(self):
        self.hasSet = {}

    def add(self, key: int) -> None:
        self.hasSet[key] = 1

    def remove(self, key: int) -> None:
        del self.hasSet[key]

    def contains(self, key: int) -> bool:
        return key in self.hasSet


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)