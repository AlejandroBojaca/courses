# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """
    def __init__(self, symbol, row, column) :
    # (Rat, str, int, int) -> NoneType
        self.symbol = symbol
        self.row = row
        self.column = column
        self.num_sprouts_eaten = 0

    def __str__(self) : 
        return f"{self.symbol} at ({self.row} {self.column}) ate {self.num_sprouts_eaten} sprouts"
    
    def set_location(self, row, column) :
        self.row = row
        self.column = column

    def eat_sprout(self) :
        self.num_sprouts_eaten += 1


class Maze:
    """ A 2D maze. """
    def __init__(self, maze, rat_1, rat_2) :
    # Maze(Maze, list of lists of strings, Rat, Rat)
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = self.get_maze_sprouts()
    
    def __str__(self):
        return (
            f"{self.maze}\n"
            f"{self.rat_1.symbol} at ({self.rat_1.row} {self.rat_1.column}) ate {self.rat_1.num_sprouts_eaten} sprouts\n"
            f"{self.rat_2.symbol} at ({self.rat_2.row} {self.rat_2.column}) ate {self.rat_2.num_sprouts_eaten} sprouts"
        )
    
    def get_maze_sprouts(self):
        count = 0
        for row in self.maze:
            count += row.count(SPROUT)
        return count

    def is_wall(self, row, column) :
        return self.maze[row][column] == WALL
    
    def is_rat(self, rat, row, column) :
        return (rat.row == row) and (rat.column == column)
    
    def is_sprout(self, row, column) :
        return self.maze[row][column] == SPROUT
        
    def get_character(self, row, column) :
        if (self.is_rat(self.rat_1, row, column)) :
            return self.rat_1.symbol

        if (self.is_rat(self.rat_2, row, column)) :
            return self.rat_2.symbol
        
        return self.maze[row][column]
    
    def move(self, rat, ver, hor) :
        row = rat.row + hor
        column = rat.column + ver
        if (self.is_wall(row, column)) :
            return False
        
        rat.set_location(row, column)

        if (self.is_sprout(row, column)) :
            rat.eat_sprout()
            self.maze[row][column] = HALL
            self.num_sprouts_left -= 1

        return True

# rat1 = Rat('J', 1, 1)
# rat2 = Rat('P', 1, 4)
# maze = Maze([['#', '#', '#', '#', '#', '#', '#'], 
#       ['#', '.', '.', '.', '.', '.', '#'], 
#       ['#', '.', '#', '#', '#', '.', '#'], 
#       ['#', '.', '.', '@', '#', '.', '#'], 
#       ['#', '@', '#', '.', '@', '.', '#'], 
#       ['#', '#', '#', '#', '#', '#', '#']], 
#       rat1,
#       rat2)