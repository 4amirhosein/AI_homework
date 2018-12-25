from random import randint,uniform
from pprint import pprint
import math
class EightPuzzle:

    searched_states = []
    def __init__(self):
        self.row_of_blank = 2
        self.column_of_blank = 2
        self.map = [[1,2,3], [4,5,6] , [7,8,0]]
        self.searched_states = []
    
    # move puzzle functions
    # these four functions below are for moving the puzzle
    def move_left(self ):
        if(self.column_of_blank > 0):
            temp = self.map[self.row_of_blank][self.column_of_blank - 1]
            self.map[self.row_of_blank][self.column_of_blank - 1] = 0
            self.map[self.row_of_blank][self.column_of_blank ] = temp
            self.column_of_blank -= 1
            if(self.map not in self.searched_states):
                self.searched_states.append([self.map])

    def move_right(self):
        if(self.column_of_blank < 2):
            temp = self.map[self.row_of_blank][self.column_of_blank + 1]
            self.map[self.row_of_blank][self.column_of_blank + 1] = 0
            self.map[self.row_of_blank][self.column_of_blank ] = temp
            self.column_of_blank += 1
            if(self.map not in self.searched_states):
                self.searched_states.append([self.map])


    def move_up(self):
        if(self.row_of_blank > 0):
            temp = self.map[self.row_of_blank -1][self.column_of_blank ]
            self.map[self.row_of_blank -1][self.column_of_blank ] = 0
            self.map[self.row_of_blank][self.column_of_blank ] = temp
            self.row_of_blank -= 1
            if(self.map not in self.searched_states):
                self.searched_states.append([self.map])

    def move_down(self): 
        if(self.row_of_blank < 2):
            temp = self.map[self.row_of_blank +1][self.column_of_blank ]
            self.map[self.row_of_blank +1][self.column_of_blank ] = 0
            self.map[self.row_of_blank][self.column_of_blank ] = temp
            self.row_of_blank += 1
            if(self.map not in self.searched_states):
                self.searched_states.append([self.map])       
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
        for i in range(80):
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

            # self.show_puzzle()
            # print("the successors of state: {} and the cost of this state :{}".format(best_successors , self.manhattan_cost()))
            # self.show_puzzle()
            best_successors = sorted(best_successors , key = lambda x: x[1] )
            best_successor = best_successors[0]


            if(best_successor[1] < current_cost):
                if(best_successor[0] == 'right'):
                    self.move_right()
                elif(best_successor[0] == 'left'):
                    self.move_left()
                elif(best_successor[0] == 'up'):
                    self.move_up()
                elif(best_successor[0] == 'down'):
                    self.move_down()
            elif ( self.manhattan_cost() == 0 ):
                # print("reached to a global minimum")
                # print(self.searched_states)
                return 1
            else:
                # print("reached to a local minimum")         
                return 0
            

    def schedule(self,t):
        
        return t - t * .04

    def simulated_annealing(self):
        T = 40
        for t in range(1000):
            successors = self.get_best_successor()
            current_cost = self.manhattan_cost()
            T = self.schedule(T)
            if T < 0:
                if self.manhattan_cost() == 0:
                    return 1
                else :
                    return 0
                break 
            random_index = randint(0,len(successors) - 1 )
            random_successor = successors[random_index]

            cost_for_random_move = 0

            if random_successor[0] == 'right':
                self.move_right()
                cost_for_random_move = self.manhattan_cost()
                self.move_left()
            elif random_successor[0] == 'left':
                self.move_left()
                cost_for_random_move = self.manhattan_cost()
                self.move_right()
            elif random_successor[0] == 'up':
                self.move_up()
                cost_for_random_move = self.manhattan_cost()
                self.move_down()
            elif random_successor[0] == 'down':
                self.move_down()
                cost_for_random_move = self.manhattan_cost()
                self.move_up()

            # print("randome successor {}".format(random_successor))
            # print("current cost {} ".format(current_cost))
            # print("random cost {} ".format(cost_for_random_move))
            
            # print("delta {}".format(delta_e))
            # print("Probabilty {}".format(uniform(0,1) < math.exp(delta_e / T)))
            # print("T : {}".format(T))
            
            delta_e = current_cost - cost_for_random_move 
            if(delta_e > 0):
                if(random_successor[0] == 'right'):
                    self.move_right()
                elif(random_successor[0] == 'left'):
                    self.move_left()
                elif(random_successor[0] == 'up'):
                    self.move_up()
                elif(random_successor[0] == 'down'):
                    self.move_down()
            elif uniform(0,1) < math.exp(delta_e / T):
                if(random_successor[0] == 'right'):
                    self.move_right()
                elif(random_successor[0] == 'left'):
                    self.move_left()
                elif(random_successor[0] == 'up'):
                    self.move_up()
                elif(random_successor[0] == 'down'):
                    self.move_down()
        if self.manhattan_cost() == 0:
            return 1
        else :
            return 0

    


    # print the state of puzzle
    def show_puzzle(self):
        print("-----")
        for i in (0,1,2):
            print(self.map[i])
        print("-----")
    




if __name__ == "__main__":
    print("8 puzzle problem")
    failed_numbers = 0
    successfull_numbers = 0
    searched_states = 0
    for i in range(100):
        puzzle = EightPuzzle()
        puzzle.break_puzzle()
        result = puzzle.hill_climbing()
        searched_states += len(puzzle.searched_states)
        if(result == 1):
            successfull_numbers += 1
        else :
            failed_numbers += 1
    print("for hill climbing for 100 example : failed : {} , and successfull : {}".format(failed_numbers,successfull_numbers))
    print("and Mean searched states for each puzzle is {}".format(searched_states/100))

    failed_numbers = 0
    successfull_numbers = 0
    searched_states = 0
    for i in range(100):
        puzzle = EightPuzzle()
        puzzle.break_puzzle()
        result = puzzle.simulated_annealing()
        searched_states += len(puzzle.searched_states)
        if(result == 1):
            successfull_numbers += 1
        else :
            failed_numbers += 1
    print("for simulated annealing 100 example : failed : {} , and successfull : {}".format(failed_numbers,successfull_numbers))
    print("and Mean searched states for each puzzle is {}".format(searched_states/100))

    