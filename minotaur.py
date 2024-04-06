import random
import maze

class Minotaur:
    """represents the mintaur that guard the maze by trying to prevent hero from escaping"""
    def __init__(self):
        """initialize minotaur at random empty spot in the maze"""
        m = maze.Maze()
        #choose randome empty space
        row = random.randint(0, len(m)-1)
        col = random.randint(0, len(m[0]) - 1)
        while m[row][col] != ' ':
            row = random.randint(0, len(m)-1)
            col = random.randint(0, len(m[0]) - 1)

        m[row][col] = "M"
        #place an 'M' to represent the Minotaur when displaying the maze

    def move_minotaur(self):
        """move minotaur towards the hero"""
        m = maze.Maze()
        row, col = m.search_maze("M")
        #find self
        hrow, hcol = m.search_maze("H")
        #find hero
        m[row][col] =" "
        #overwrite the old location

        #decide direction to move to get to hero
        #vertical, if neg then hero is below, if pos then hero above
        diff_vert = row - hrow
        #horizontal, if neg, then hero is right, if pos, hero is left
        diff_hori = col - hcol
        ch = "*"
        
        #if on the same row or col, move towards the hero
        if diff_vert == 0:
            if diff_hori < 0 :
                ch = m[row][col + 1]
                if ch != "*" and ch != "f":
                    col +=1
                    #move to left
            else:
                ch = m[row][col - 1]
                if ch != "*" and ch != "f":
                    col -=1
                    #move to right
        elif diff_hori == 0: 
            if diff_vert < 0 :
                ch = m[row+1][col]
                if ch != "*" and ch != "f":
                    row += 1
                    #move up
            else:
                ch = m[row-11][col]
                if ch != "*" and ch != "f":
                    row -= 1
                    #move down
        #otherwise set the direction based on the shorter distance
        elif diff_vert > diff_hori:
            if diff_hori < 0:
                ch = m[row][col + 1]
                if ch != "*" and ch != "f":
                    col += 1
            else:
                ch = m[row][col - 1]
                if ch != "*" and ch != "f":
                    col -= 1
        elif diff_vert <= diff_hori:
            if diff_vert < 0:
                ch = m[row + 1][col]
                if ch != "*" and ch != "f":
                    row += 1
            else:
                ch = m[row - 1][col]
                if ch != "*" and ch != "f":
                    row -= 1

        #if a informed direction can't be found, choose randomly
        while ch == "*" or ch == "f":
            r = random.randint(1,4)
            newrow = row
            newcol = col
            if r == 1:
                newrow -= 1
            elif r == 2:
                newrow += 1
            elif r == 3:
                newcol -= 1
            else:
                newcol += 1
            ch = m[newrow][newcol]

            if ch != "*" and ch != "f":
                row = newrow
                col = newcol

        ch = m[row][col]
        m[row][col] = "M"

        return ch
        # return character at this position
        # that way main will know if the minotaur captured the hero 

