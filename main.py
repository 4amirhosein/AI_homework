from eight_puzzle import EightPuzzle
import os




if __name__ == "__main__":
    failed_numbers = 0
    successfull_numbers = 0
    for i in range(1000):
        puzzle = EightPuzzle()
        puzzle.break_puzzle()
        result = puzzle.hill_climbing()
        if(result == 1):
            successfull_numbers += 1
        else :
            failed_numbers += 1
    print("failed : {} , and successfull : {}".format(failed_numbers,successfull_numbers))

    