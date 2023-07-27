# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = []
        self.flatten(nestedList)
        print(self.nestedList)
        self.cur = 0
        
    def flatten(self, nestedList):
        for i in nestedList:
            inte = i.getInteger()
            lst = i.getList()
            print(inte, lst)
            if len(lst) > 0:
                self.flatten(lst)
            if inte != None:
                self.nestedList+=[i]
    
    def next(self) -> int:
        result = self.nestedList[self.cur]
        self.cur+=1
        return result
    
    def hasNext(self) -> bool:
        return self.cur < len(self.nestedList)
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())