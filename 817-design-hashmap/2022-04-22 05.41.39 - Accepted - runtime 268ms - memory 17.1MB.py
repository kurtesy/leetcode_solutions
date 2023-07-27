class MyHashMap:

    def __init__(self):
        self.hasMap = {}

    def put(self, key: int, value: int) -> None:
        self.hasMap[key] = value

    def get(self, key: int) -> int:
        try:
            return self.hasMap[key]
        except Exception as e:
            return -1

    def remove(self, key: int) -> None:
        try:
            del self.hasMap[key]
        except Exception as e:
            pass
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)