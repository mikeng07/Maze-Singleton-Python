import maze
class Hero:
    """Represents the Hero that will navigate the maze"""
    def __init__(self):
        #place hero at the start of the maze
        #replace the s with h
        m = maze.Maze()
        row, col = m.search_maze("s")
        m[row][col]="H"
        #places an 'H' on map to represent hero location 

    def go_up(self):
        """move hero north in the maze"""
        m = maze.Maze()
        row,col = m.search_maze("H")
        ch = m[row-1][col]
        if ch != "*":
            m[row][col] = " "
            #delete old H
            row -= 1
            m[row][col] = "H"
            #places new H
        return ch 
        #return character that was in the hero's current position 
        #that way main can check that it's not a '*'

    def go_down(self):
        """move hero south in the maze"""
        m = maze.Maze()
        row,col = m.search_maze("H")
        ch = m[row+1][col]
        if ch != "*":
            m[row][col] = " "
            #delete old H
            row += 1
            m[row][col] = "H"
            #places new H
        return ch 

    def go_left(self):
        """move hero west in the maze"""
        m = maze.Maze()
        row,col = m.search_maze("H")
        ch = m[row][col-1]
        if ch != "*":
            m[row][col] = " "
            #delete old H
            col -= 1
            m[row][col] = "H"
            #places new H
        return ch 

    def go_right(self):
        """move hero east in the maze"""
        m = maze.Maze()
        row,col = m.search_maze("H")
        ch = m[row][col+1]
        if ch != "*":
            m[row][col] = " "
            #delete old H
            col += 1
            m[row][col] = "H"
            #places new H
        return ch 
