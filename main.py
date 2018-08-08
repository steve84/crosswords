from board import Board
from solver import Solver

width = 14
height = 14
word_length = 7
clues = ['AERZTIN', 'ALRAUNE', 'ANTARES',
         'AUSFALL', 'AUSTRAL', 'AVENTIN',
         'BEKLAGT', 'BENEFIZ', 'BUERSTE',
         'GRANTIG', 'HAUSRAT', 'HEBAMME',
         'MARILYN', 'MAUSERN', 'MINDERN',
         'MUSISCH', 'PRANGER', 'PHAEAKE',
         'RUSALKA', 'SATTELN', 'SCHAUER',
         'SPONTAN', 'SPROSSE', 'SPRUDEL']

layout = ['00111111100000',
          '00101010000000',
          '11111110000000',
          '10111111100000',
          'S1111110000000',
          '10111111101000',
          '11111110101001',
          '10010101111111',
          '10010111111101',
          '00000001111111',
          '00000111111101',
          '00000001111111',
          '00000001010101',
          '00000111111100'
          ]

board = Board(height, width, word_length)
board.setupBoard(layout)
solver = Solver()
solver.solve(board, clues)