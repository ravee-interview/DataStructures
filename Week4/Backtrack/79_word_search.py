class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.board = board
        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.search(r,c,word):
                    return True
        return False
    
    def search(self,r,c,word,i=0):
        
        if r >= len(self.board) or c >= len(self.board[0]) or r < 0 or c < 0:
            return False
        letter = self.board[r][c]
        if word[i] == self.board[r][c]:
            if i+1 == len(word):
                return True
            
            self.board[r][c] = "#"
            down = self.search(r+1,c,word,i+1)
            left = self.search(r,c+1,word,i+1)
            up = self.search(r-1,c,word,i+1)
            right = self.search(r,c-1,word,i+1)
            if up or down or left or right:
                return True
        self.board[r][c] = letter
        return False

#     a b c e
#     s f c s
#     a d e e
    
#     abcb
