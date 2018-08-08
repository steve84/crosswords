from copy import deepcopy

class Solver():
    
    
    def solve(self, board, clues):
        if board.isBoardComplete():
          for clue in clues:
            if board.isWordOnBoardHorizontal(clue) or board.isWordOnBoardVertical(clue):
              clues.remove(clue)
        if clues:
            x_coord, y_coord, direction = board.findHWord()
            if x_coord < 0 and y_coord < 0:
                x_coord, y_coord, direction = board.findVWord()
                if x_coord < 0 and y_coord < 0:
                  return None

            words = self.suitableWords(x_coord, y_coord, direction, board, clues)
            if not len(words):
                return None
            for word in words:
                new_board = deepcopy(board)
                new_clues = deepcopy(clues)
                new_board.setWord(x_coord, y_coord, direction, word)
                new_clues.remove(word)
                self.solve(new_board,
                           new_clues)
        else:
            board.printBoard()
            return board
            

    def suitableWords(self, x, y, direction, board, clues):
        suitable_words = list()
        for clue in clues:
            invalid_clue = False
            if direction == 'h':
                y_coord = y
                i = 0
                for x_coord in range(x, x + board.getWordLength()):
                    if board.getField(x_coord, y_coord) == '':
                        i += 1
                        continue
                    if clue[i] != board.getField(x_coord, y_coord):
                        invalid_clue = True
                        break
                    i += 1
                if not invalid_clue:
                    suitable_words.append(clue)
            else:
                x_coord = x
                i = 0
                for y_coord in range(y, y + board.getWordLength()):
                    if board.getField(x_coord, y_coord) == '':
                        i += 1
                        continue
                    if clue[i] != board.getField(x_coord, y_coord):
                        invalid_clue = True
                        break
                    i += 1
                if not invalid_clue:
                    suitable_words.append(clue)
        return suitable_words