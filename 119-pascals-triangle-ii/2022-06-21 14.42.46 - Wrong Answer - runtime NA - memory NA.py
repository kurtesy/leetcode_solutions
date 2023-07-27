class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return [*map(int, str(11**rowIndex))]
        