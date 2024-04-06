class Maze:
    """A class to represent a maze.
    Attributes:
        _maze: char[][] - stores the maze read in from a file
    """

    _instance = None
    _initialized = False
    def __new__(cls):
        """constructor the Maze as the singleton pattern"""
        if cls._instance is None:
            #This condition checks whether an instance of the class already exists
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Loads the maze from the file"""
        if not Maze._initialized:
            self._maze = []
            file = open("minomaze.txt")   
            for line in file:
                spaces = []
                for ch in line.strip():
                    #For each line, it strips any leading or trailing whitespace 
                    #(line.strip()) and then iterates over each character in the line
                    #prevent white space at the begin or end of the line
                    spaces.append(ch)
                self._maze.append(spaces)
            Maze._initialized = True 
    def __getitem__(self,row):
        """access a row from the maze"""
        return self._maze[row]

    def __len__(self):
        """returns the number of rows in the maze"""
        return len(self._maze)

    def __str__(self):
        """string representation of the maze"""
        s = ""
        for r in self._maze:
            for c in r:
                s += c + " "
            s += "\n"
        return s

    def search_maze(self,ch):
        """returns the row and column of the character"""
        for i,r  in enumerate (self._maze):
            for j,c in enumerate (r):
                if c == ch:
                    return [i,j]
        return [0,0]

