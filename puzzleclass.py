class myPuzzle:

    def __init__(self, config):
        self.dimension = len(config[0])
        self.config = config

    def solved(self):
        n = self.dimension
        for i in range(0,n):
            for j in range(0,n):
                x = x + str(self.config[i][j])
        return x == '123456780'

    def checkitout(self):
        for k in self.config:
            print(k)
        print()





board = [[1,2,3],[4,5,6],[7,8,0]]
puzzle1 = myPuzzle(board)
puzzle1.checkitout()

#print(str(9))




