class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()

        posDiag = set()
        negDiag = set()

        res = []
        board = [["."]*n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                # include the new Q into possible positions
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"
                # do a recursive iterations for a single position, lead by the for loop
                backtrack(r+1)
                # clean up and try for the rest
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
        backtrack(0)
        return res
