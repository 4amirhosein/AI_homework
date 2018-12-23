from random import randint


class EightPuzzle:


    def __init__(self):
        self.row_of_blank = 2
        self.column_of_blank = 2
        self.map = [[1,2,3], [4,5,6] , [7,8,0]]
    
    # move puzzle functions
    # these four functions below are for moving the puzzle
    def move_left(self ):
        if(self.column_of_blank > 0):
            temp = self.map[self.row_of_blank][self.column_of_blank - 1]
            self.map[self.row_of_blank][self.column_of_blank - 1] = 0
            self.map[self.row_of_blank][self.column_of_blank ] = temp
            self.column_of_blank -= 1

    def move_right(self):
        if(self.column_of_blank < 2):
            temp = self.map[self.row_of_blank][self.column_of_blank + 1]
            self.map[self.row_of_blank][self.column_of_blank + 1] = 0
            self.map[self.row_of_blank][self.column_of_blank ] = temp
            self.column_of_blank += 1

    def move_up(self):
        if(self.row_of_blank > 0):
            temp = self.map[self.row_of_blank -1][self.column_of_blank ]
            self.map[self.row_of_blank -1][self.column_of_blank ] = 0
            self.map[self.row_of_blank][self.column_of_blank ] = temp
            self.row_of_blank -= 1

    def move_down(self): 
        if(self.row_of_blank < 2):
            temp = self.map[self.row_of_blank +1][self.column_of_blank ]
            self.map[self.row_of_blank +1][self.column_of_blank ] = 0
            self.map[self.row_of_blank][self.column_of_blank ] = temp
            self.row_of_blank += 1
    # end of move functions 

    # functions for calculating manhattan cost
    def get_coordinate_of_number(self,number):
        for i in (0,1,2):
            for j in (0,1,2):
                if self.map[i][j] == number :
                    return i , j

    def get_true_coordinate_of_number(self,number):
        true_coordinate_of_numbers = { 1 : (0,0) , 2 : (0,1), 3 : (0,2), 4 : (1,0), 5 : (1,1), 6 : (1,2),7 : (2,0), 8 : (2,1) }
        return true_coordinate_of_numbers.get(number)



    def manhattan_cost(self):
        cost = 0 
        for i in (1,2,3,4,5,6,7,8):
            x , y  = self.get_coordinate_of_number(i)
            x_true_place, y_true_place =  self.get_true_coordinate_of_number(i)
            cost += abs(x_true_place - x)
            cost += abs(y_true_place - y)
        return cost

    def get_best_successor(self):
        directions = []

        if(self.column_of_blank < 2):
            self.move_right()
            right_cost = self.manhattan_cost()
            directions.append(('right' , right_cost))
            self.move_left()

        if(self.column_of_blank > 0):
            self.move_left()
            left_cost = self.manhattan_cost()
            directions.append(('left' , left_cost))
            self.move_right()
        
        if(self.row_of_blank > 0):
            self.move_up()
            up_cost = self.manhattan_cost()
            directions.append(('up' , up_cost))
            self.move_down()

        if(self.row_of_blank < 2):
            self.move_down()
            down_cost = self.manhattan_cost()
            directions.append(('down' , down_cost)) 
            self.move_up()

        return directions
        


    # getting to a randome initial state
    def break_puzzle(self):
        for i in range(100):
            randome_number = randint(0,3)
            if (randome_number == 0):
                self.move_right()
            elif (randome_number == 1):
                self.move_left()
            elif (randome_number == 2):
                self.move_up() 
            elif (randome_number == 3):
                self.move_down()
                # for j in range(2):
                #     first_x = randint(0,2)
                #     second_x = randint(0,2)
                #     first_y = randint(0,2)
                #     second_y = randint(0,2)
                #     self.map[first_x][first_y] , self.map[second_x][second_y] = self.map[second_x][second_y] , self.map[first_x][first_y]



    # here is my hill climbing algorithm 
    def hill_climbing(self):
        while True:
            best_successors = self.get_best_successor()
            current_cost = self.manhattan_cost()
            print("the successors of state: {} and the cost of this state :{}".format(best_successors , self.manhattan_cost()))
            # self.show_puzzle()
            best_successors = sorted(best_successors , key = lambda x: x[1] )
            best_successor = best_successors[0]

            if(best_successor[1] < current_cost):
                if(best_successor[0] == 'right'):
                    self.move_right()
                if(best_successor[0] == 'left'):
                    self.move_left()
                if(best_successor[0] == 'up'):
                    self.move_up()
                if(best_successor[0] == 'down'):
                    self.move_down()
            elif ( self.manhattan_cost() == 0 ):
                print("reached to a global minimum")
                return 1
            else:
                print("reached to a local minimum")            
                return 0
            

        

    


    # print the state of puzzle
    def show_puzzle(self):
        print("-----")
        for i in (0,1,2):
            print(self.map[i])
        print("-----")
    




