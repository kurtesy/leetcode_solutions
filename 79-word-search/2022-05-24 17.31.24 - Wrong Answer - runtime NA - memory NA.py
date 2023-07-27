class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.found = False
        start = 0
        visited = set()
        def backtracking(k,x,y):
            if k == len(word) - 1:
                self.found = True
                return
            if self.found or x<0 or x>=len(board) or y<0 or y>=len(board[0]):
                return
            if board[x][y] == word[k] and (x,y) not in visited:
                backtracking(k+1,x+1,y)
                backtracking(k+1,x-1,y)
                backtracking(k+1,x,y+1)
                backtracking(k+1,x,y-1)
            visited.add((x,y))
        backtracking(0,0,0)
        return self.found
                