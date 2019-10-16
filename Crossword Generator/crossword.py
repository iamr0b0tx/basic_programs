class Crossword:
    def __init__(self, word_list):
        self.word_list = word_list

        self.virtual_board = None
        virtual_board = self.connectWords()
        
        self.generateCrossword(virtual_board)

    def connectWords(self):
        # all words
        words = self.word_list.copy()

        # first word
        word = words.pop().lower()

        virtual_board = {(0, i):[c, 1] for i, c in enumerate(word)}
        vpi = [(0, i) for i in range(len(word))]

        for p in vpi:
            position = list(p)                
            c, state = virtual_board[p]

            # print(c, p)
            if state == -1:
                continue

            for wx in words:
                w = wx.lower()
                if c in w:
                    status = self.placeWord(w, c, state, position, virtual_board)

                    if status != False:
                        virtual_board, vpis = status
                        virtual_board[p][1] = -1

                        vpi.extend(vpis)
                        words.remove(wx)

                        # print(virtual_board)
                        # self.generateCrossword(virtual_board)
                        break

        return virtual_board

    def placeWord(self, word, insection_character, state, relative_origin, virtual_board=None):
        if virtual_board is None:
            virtual_board = self.virtual_board

        state = (state+1) % 2

        for intersection_position, ch in enumerate(word):

            # newly added positions
            new_positions = []
            vb = virtual_board.copy()

            if ch != insection_character:
                continue

            li = []
            for i, c in enumerate(word):
                if i == intersection_position:
                    continue
                
                d = list(relative_origin)
                d[state] = i - intersection_position + relative_origin[state]
                vb[tuple(d)] = [c, state]

                if self.checkValidity(state, d, relative_origin, vb) == False:
                    new_positions = []
                    break

                li.append([c, d])
                new_positions.append(tuple(d))

            if len(new_positions) > 0:
                # for x in li:
                #     print('------------------', x)

                return vb, new_positions

        return False

    def generateCrossword(self, virtual_board):
        min_ = [0, 0]
        max_ = [0, 0]
        for p in virtual_board:
            for i in range(2):
                if p[i] < min_[i]:
                    min_[i] = p[i]

                if p[i] > max_[i]:
                    max_[i] = p[i]

        size = (max_[i] - min_[i] + 3 for i in range(2))
        height, width = size
        
        for i in range(height):
            line = ''
            for j in range(width):
                p = (i+min_[0]-1, j+min_[1]-1)
                # c = ' '+ virtual_board[p][0]+' ' if p in virtual_board else '███'
                c = '| {} |'.format(virtual_board[p][0].upper()) if p in virtual_board else '|XXX|'
                line += c
            print(line)
        print()
        return

    def checkPlacementValidity(self, state, relative_origin, virtual_board):
        inc = [[0, 1], [0, -1]]
        for incx in inc:
            incy = incx[::-1] if state == 1 else incx
            p = tuple(relative_origin[i]+x for i, x in enumerate(incy))
    
            print(p, state)
            if p in virtual_board:
                return False

    def checkValidity(self, state, position, relative_origin, virtual_board):
        inc = [[0, 1], [1, 0], [-1, 0]]
        position = list(position)

        for incx in inc:
            incy = incx[::-1] if state == 0 else incx
            p = tuple(position[i]+x for i, x in enumerate(incy))
            
            if tuple(relative_origin) == p:
                continue

            if p in virtual_board:
                return False

        return True

    
if __name__ == "__main__":
    word_list = ['crabs', 'soup', 'pale', 'lagos']
    word_list = ['pale', 'lagos', 'crabs', 'soup', 'envelope', 'catastrophe', 'histogram']
    crossword_instance = Crossword(word_list)
