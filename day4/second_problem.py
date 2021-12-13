# Idea:

#   Inputs: []int
#   Mats: [][][](int, bool)
# For each input:
#   For each mat:
#       Mark input as seen
#       Check rows and coloums for completeness

import re

bingo_input = []
mats = []
winning_mats = []

# Aux
def pp_mat(mat):
    print("--------------------------------------------")
    for row in mat:
        print(row)
    print("--------------------------------------------")

# Read the input
with open("input.txt", "r") as file:
    regex = re.compile(r"\s{2,}")
    bingo_input = [int(s) for s in file.readline().strip().split(",")]


    line = file.readline()
    while line != "":
        if line == "\n":
            line = file.readline()
        else:
            new_mat = []
            for _ in range(5):
                new_mat.append([(int(x), False) for x in re.sub(regex, " ", line.strip()).split(" ")])
                line = file.readline()
            mats.append(new_mat)

def check_victory(mat, row, coloumn):
    if len([y for x, y in mat[row] if y == True]) == 5:
        return True
    else:
        all_match = True
        for row in mat:
            all_match = all_match and row[coloumn][1]
        return all_match

def check_mat_for_number(mat, number):
    won = False
    marked = False
    mod_mat = mat
    for i, row in enumerate(mat):
        for j, (x, seen) in enumerate(row):
            if x == number:
                mod_mat[i][j] = x, True
                marked = True
                won = check_victory(mod_mat, i, j)
                break

    return won, marked, mod_mat

def find_looser_mat(bingo_mats, bingo_input):
    for number in bingo_input:
        for i, mat in enumerate(mats):
            if i in winning_mats:
                continue
            won, marked, mod_mat = check_mat_for_number(mat, number)
            if marked:
                mats[i] = mod_mat
            if won:
                winning_mats.append(i)
                if len(winning_mats) == len(mats):
                    print("loosing index: %d" % i)
                    print("loosing mat: %s" % pp_mat(mats[i]))
                    print("final number: %d" % number)
                    return mats[i], number

def calculate_solution_score(mat, number):
    unmarked_numbers = sum([[x for x, y in row if y == False] for row in mat], [])
    print("sum of unmarked numbers: %d" % sum(unmarked_numbers))
    return sum(unmarked_numbers) * int(number)

loosing_mat, final_number = find_looser_mat(mats, bingo_input)
solution_score = calculate_solution_score(loosing_mat, final_number)
print("Solution Score: %d" % solution_score)
