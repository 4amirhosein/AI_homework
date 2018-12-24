from random import randint
from copy import copy 

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
        print("-----------------")
        map = [[0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0]]
        for i in range(8):
            for j in range(8):
                if (i,j) in self.queens_coordinates:
                    map[i][j] = 1
        for i in range(8):
            print(map[i])
        print("-----------------")
    # def move_queen(self, ueen_number , place :
    #     x, y = self.queens_coordinates(queen_number)


    def heursitic(self , board):
        threats = 0
             
        for index in board:
            sample_board = copy(board) 
            sample_board.remove(index)
            for queen in sample_board:
                if(index[0] == queen[0] ):
                    threats += 1 
                    break
                elif(index[1] == queen[1]):
                    threats += 1
                    break
                elif( index[0] - index[1] == queen[0] - queen[1] ):
                    threats += 1
                    break
                elif( index[0] + index[1] == queen[0] + queen[1] ):
                    threats += 1
                    break
        return threats



    def make_successors(self, board):
        successors = []
        for index , queen in enumerate(board):
            for i in range(8):
                for j in range(8):
                    if (i,j) not in board:
                        sample_board = copy(board)
                        sample_board[index] = (i,j)
                        cost = self.heursitic(sample_board)
                        successors.append((sample_board,cost))
        return successors

    def hill_climbing(self):
        while True:
            
            current_cost = self.heursitic(self.queens_coordinates)
            successors = self.make_successors(self.queens_coordinates)
            sorted_successors = sorted(successors , key = lambda x: x[1] )
            best_successor = sorted_successors[0]

            # self.show_in_table()
            # print(current_cost)

            if best_successor[1] < current_cost:
                self.queens_coordinates = best_successor[0]
            elif current_cost == 0:
                # print("reached to global minimum ")
                return 1
            else :
                # print("reached to local minimum ")
                return 0


if  __name__== "__main__":
    
    print("8 queen problem")
    print("waiting...")
    failed_numbers = 0
    successfull_numbers = 0
    for i in range(100):
        eight_queen = EightQueen()
        eight_queen.random_initial()
        result = eight_queen.hill_climbing()
        if(result == 1):
            successfull_numbers += 1
        else :
            failed_numbers += 1
    print("hill climbing for 100 example : failed : {} , and successfull : {}".format(failed_numbers,successfull_numbers))
    