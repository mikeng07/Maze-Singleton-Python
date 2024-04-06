import maze
import minotaur
import hero

def main_menu():
    """display the main menu"""
    dir = ""
    while dir != "W" and dir != "A" and dir != "S" and dir != "D":
        dir = input("Choose a Direction (WASD): ").upper()
    return dir

def main():
    m = maze.Maze()
    mino = minotaur.Minotaur()
    h = hero.Hero()
    print(m)

    play = True
    while play:
        dir = main_menu()
        ch = ""
        if dir == "W":
            ch = h.go_up()
        elif dir == "A":
            ch = h.go_left()
        elif dir == "S":
            ch = h.go_down()
        elif dir == "D":
            ch = h.go_right()

        if ch == 'f':
            pint(m)
            print("You found the exit")
            play = False
        elif ch == 'M':
            print(m)
            print("You ran into the minotaur!")
            play = False
        else:
            if ch == "*":
                print ("You ran into a wall...")
            let = mino.move_minotaur()
            print(m)
            if let == "H":
                print("The minotaur has captured you!")
                print("Game Over")
                play = False
main()