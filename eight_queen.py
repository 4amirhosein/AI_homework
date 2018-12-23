from random import randint


class EightQueen:

    def __init__(self):
        self.queens_coordinates = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7)]
        
    

    def random_initial(self):
        index = 0
        while True:
            if(index > 7 ):
                break
            x = randint(0,7)
            y = randint(0,7)
            if ( (x,y) not in self.queens_coordinates ):
                self.queens_coordinates[index] = (x,y)
                index += 1

    def show_in_table(self):
        for i in range(7):
            for j in range(7):
                if (i,j) in self.queens_coordinates:
                    print("1",end="")
                else:    
                    print("0",end="")
            print()
    # def move_queen(self, ueen_number , place ):
    #     x, y = self.queens_coordinates(queen_number)

    def make_successors(self):
        pass



if __name__=="__main__":
    eight_queen = EightQueen
    eight_queen.show_in_table()