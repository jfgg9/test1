#MAGIC MAZE HOMEWORK

print("Welcone to the Magic Maze!")
print("Which way you want to go: N, S, E, W?")

solution = "SSWNES"

lives = 3

moves = 0

direction = ""


while True:

    temp = input('Enter your move: ')


    if temp != "N" and temp != "S" and temp != "E" and temp != "W":

        print("try another way")
        print("Moves: ", moves)
        print("Lives: ", lives)


        direction = direction+temp
        moves += 1


    elif direction.__contains__(solution):

        print("You made it out!")
        print("Moves: ", moves)
        print("Lives: ", lives)
        break


    if moves% 10 == 0:

        lives = lives-1

    if lives == 0:

        print("You got lost in the maze! You die. ")