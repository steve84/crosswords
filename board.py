NO_FIELD_CHAR = '0'
FIELD_CHAR = '1'

class Board():


    def __init__(self, height, width, word_length):
        self.height = height
        self.width = width
        self.word_length = word_length
        self.board = list()

    def findHWord(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                if self.board[y][x] != NO_FIELD_CHAR and not self.isCompletedWord(x, y, 'h'):
                    x_coord, y_coord, direction = self.findStart(x, y, 'h')
                    if not self.isAWord(x_coord, y_coord, 'h'):
                        continue
                    return x_coord, y_coord, direction
        return -1, -1, ''

    def findVWord(self):
        for x in range(0, self.width):
            for y in range(0, self.height):
                if self.board[y][x] != NO_FIELD_CHAR and not self.isCompletedWord(x, y, 'v'):
                    x_coord, y_coord, direction = self.findStart(x, y, 'v')
                    if not self.isAWord(x_coord, y_coord, 'v'):
                        continue
                    return x_coord, y_coord, direction
        return -1, -1, ''
            
    def findStart(self, x, y, direction):
        if direction == 'h':
            if x < 1:
                return x, y, direction
            if self.board[y][x-1] == NO_FIELD_CHAR:
                return x, y, direction
            else:
                return self.findStart(x-1, y, direction)
        else:
            if y < 1:
                return x, y, direction
            if self.board[y-1][x] == NO_FIELD_CHAR:
                return x, y, direction
            else:
                return self.findStart(x, y-1, direction)

    def setWord(self, x, y, direction, word):
        if direction == 'h':
            y_coord = y
            i = 0
            for x_coord in range(x, x + self.word_length):
                self.board[y_coord][x_coord] = word[i]
                i += 1
        else:
            x_coord = x
            i = 0
            for y_coord in range(y, y + self.word_length):
                self.board[y_coord][x_coord] = word[i]
                i += 1

    def getField(self, x, y):
        return self.board[y][x]
    
    def setupBoard(self, layout):
        for y in range(0, self.height):
            tmp = list()
            for x in range(0, self.width):
                value = layout[y][x]
                if value == FIELD_CHAR:
                    tmp.append('')
                else:
                    tmp.append(value)
            self.board.append(tmp)
                    
    def getWordLength(self):
        return self.word_length

    def printBoard(self):
        for y in range(0, self.height):
            print(self.board[y])
            
    def isCompletedWord(self, x, y, direction):
        x_coord, y_coord, direction = self.findStart(x, y, direction)
        if x_coord > -1 and y_coord > -1:
            if direction == 'h':
                for x_inc in range(x_coord, x_coord + self.word_length):
                    if x_inc >= self.width:
                        return False
                    if self.board[y][x_inc] == '':
                        return False
                return True
            else:
                for y_inc in range(y_coord, y_coord + self.word_length):
                    if y_inc >= self.height:
                        return False
                    if self.board[y_inc][x] == '':
                        return False
                return True
    
    def isAWord(self, x, y, direction):
        if direction == 'h':
            for x_coord in range(x, x + self.word_length):
                if x_coord >= self.width:
                    return False
                if self.board[y][x_coord] == '0':
                    return False
            startCheck = True
            endCheck = True
            if x > 0:
                startCheck = self.board[y][x-1] == '0'
            if x+self.word_length-1 < (self.width -1):
                endCheck = self.board[y][x+self.word_length] == '0'
            return startCheck and endCheck
        else:
            for y_coord in range(y, y + self.word_length):
                if y_coord >= self.height:
                    return False
                if self.board[y_coord][x] == '0':
                    return False
            startCheck = True
            endCheck = True
            if y > 0:
                startCheck = self.board[y-1][x] == '0'
            if y+self.word_length-1 < (self.height -1):
                endCheck = self.board[y+self.word_length][x] == '0'
            return startCheck and endCheck
    
    def isBoardComplete(self):
      for y in range(0, self.height):
          for x in range(0, self.width):
            if self.board[y][x] == '':
              return False
      return True
      
    
    def isWordOnBoardHorizontal(self, word):
      for y in range(0, self.height - self.word_length + 1):
        for x in range(0, self.width - self.word_length + 1):
          if ''.join(self.board[y][x:x+self.word_length]) == word:
            return False
      return False


    def isWordOnBoardVertical(self, word):
      for y in range(0, self.height - self.word_length + 1):
        for x in range(0, self.width - self.word_length + 1):
          if self.getBoardValueVertical(x, y) == word:
            return True
      return False
      
    
    def getBoardValueVertical(self, x, y):
      word = ''
      for i in range(y, y + self.word_length):
        word += self.board[i][x]
      return word
      
