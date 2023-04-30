


class Game:
    def __init__(self):
        self.board = [['','',''],
                      ['','',''],
                      ['','','']]
        self.player = 0
        
    def render(self):
        y = 0
        for row in self.board:
            x = 0
            for case in row:
                if case == 'X' or 'O':
                    textSize(60)
                    fill(0, 132, 100)
                    text(case, x+ 30, y+70)
                x+=width/3
            y+=height/3
            
    def GameOver(self):
        #win by row
        for symbol in ['X','O']:
            for row in self.board:
                if row== [symbol, symbol, symbol]:
                    return True
        #win by column:
            transposed_board = list(zip(*self.board))
            for col in self.board:
                if col== (symbol, symbol, symbol):
                    return True
        #win for diagonal:
            diagonal1 = [self.board[i][i] for i in range(3)]
            diagonal2 = [self.board[i][2-i] for i in range(3)]
            if diagonal1 == [symbol, symbol, symbol] or diagonal2 == [symbol, symbol, symbol]:
               return True
                    
        #Case of Tie
        for row in self.board:
            for case in row:
                if case == '':
                    return False
        return True
        

         
def setup():
    global game
    size(300, 300)
    background(255)
    line(width/3,0,width/3, height)
    line(width*2/3,0,width*2/3, height)
    line(0,height/3,width, height/3)
    line(0,height*2/3,width, height*2/3)
    game = Game()

    
    
def draw():
    global game
    game.render()
    if game.GameOver():
        print("GAME OVER :)")
    
def mouseClicked():
        global game
        row = mouseY // (height/3)
        col = mouseX // (width/3)
        print(row, col)
        
        if game.board[row][col] == '':
            if game.player%2 == 0:
                game.board[row][col] = 'X'
            else:
                game.board[row][col] = 'O'
            game.player+=1
        
