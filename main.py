# Austin Hall
# Elishbah Younus
# CIS-479 Program 1
# Creation Date: 1/25/2023
# Date: 1/28/2023


class Node:
    def __init__(self, data, gval, fval):
        # Initialize the node with the matrix data, accumulated path cost of the node (gval) and the calculated fvalue
        self.matrix = data
        self.fval = fval
        self.gval = gval

    # Passes in a puzzle matrix, the old x and y values, and the new x and y values
    # Will return a puzzle matrix if the new values were within the matrix parameters
    def moveTile(self, puzzle, x1, y1, x2, y2):

        if x2 >= 0 and x2 < len(self.matrix) and y2 >= 0 and y2 < len(self.matrix):
            temp_puzzle = []
            temp_puzzle = self.copy(puzzle)
            temp = temp_puzzle[x2][y2]
            temp_puzzle[x2][y2] = temp_puzzle[x1][y1]
            temp_puzzle[x1][y1] = temp
            return temp_puzzle
        else:
            return None

    # Create child nodes off of the current one
    # Will attempt to create one for each direction, but only if it is a possible move
    def generate_childNodes(self):

        x, y = self.find(self.matrix, '-')
        # Directions list contains the possible ways for the blank tile to move
        directions_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        children = []
        index = 0
        while index < len(directions_list):
            i = directions_list[index]
            child = self.moveTile(self.matrix, x, y, i[0], i[1])
            if child is not None:
                cost = 0
                # When number tile moves LEFT
                if index == 0:
                    cost = 2
                # When number tile moves RIGHT
                elif index == 1:
                    cost = 2
                # When number tile moves DOWN
                elif index == 2:
                    cost = 1
                # When number tile moves UP
                elif index == 3:
                    cost = 3
                # The path cost is determined by direction, and then added and passed onto the child node
                # as their g value, this way its path cost accumulates
                child_node = Node(child, self.gval + cost, 0)
                children.append(child_node)
            index += 1

        return children

    # Returns a tuple (x,y)
    def find(self, puzzle, k):
        for x in range(0, len(self.matrix)):
            for y in range(0, len(self.matrix)):
                if puzzle[x][y] == k:
                    return x, y

    # Returns a copy of a given matrix
    def copy(self, original):
        temp = []
        for i in original:
            row = []
            for numb in i:
                row.append(numb)
            temp.append(row)
        return temp

class Puzzle:
    def __init__(self):

        self.n = 3
        self.frontier = []
        self.terminatedNodes = []

    # Gets the puzzle matrix from the user
    def getMatrix(self):
        matrix = []
        for i in range(0, self.n):
            temp = input().split(" ")
            matrix.append(temp)
        return matrix

    # Takes in a node and a matrix
    # Returns the value of h(n) + g(n)
    def f(self, start, goal):
        # f(n) = h(n) + g(n)
        return self.h(start, goal) + start.gval

    # Takes in a node and a matrix
    # Outputs the manhattan distance between their states
    def h(self, node, goal):
        # Calculates the Manhattan distance between the different states
        start = node.matrix
        temp = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if start[i][j] != '-' and start[i][j] != goal[i][j]:
                    x_val = i
                    y_val = j
                    goals = node.find(goal, start[i][j])
                    x_goal = goals[0]
                    y_goal = goals[1]
                    x = x_val - x_goal
                    if x > 0:
                        x = x * 3
                    else:
                        x = x * -1
                    y = abs(y_val - y_goal) * 2
                    temp += x + y
        return temp

    # This acts like a main method
    def solvePuzzle(self):

        print("Enter the initial puzzle state \n")
        start = self.getMatrix()
        print("Enter the goal puzzle state \n")
        goalMatrix = self.getMatrix()

        # Start state matrix is given a gval of 0
        start = Node(start, 0, 0)
        start.fval = self.f(start, goalMatrix)
        # Put the start node in the frontier list
        self.frontier.append(start)

        print("\n")
        counter = 1
        while True:
            # Get node at front of frontier list (has the lowest f value)
            currentNode = self.frontier[0]
            print("")
            print("")
            print("  | ")
            print("  | ")
            print("  | ")
            print(" \ / \n")
            for i in currentNode.matrix:
                for j in i:
                    print(j, end=" ")
                print("")

            print("")
            print("#%d" % counter, "G:", currentNode.gval, "H:", self.h(currentNode, goalMatrix))

            # If the manhattan distance between current and goal state is 0 we have reached the goal
            if self.h(currentNode, goalMatrix) == 0:
                print("Puzzle is solved!")
                break

            # Expand the frontier for the current node
            for i in currentNode.generate_childNodes():
                i.fval = self.f(i, goalMatrix)
                # Add new nodes to the frontier list
                self.frontier.append(i)

            # Add current node to terminated list, and delete it from the frontier list
            self.terminatedNodes.append(currentNode)
            del self.frontier[0]
            counter += 1
            # sort the frontier list based on f value before it loops again
            self.frontier.sort(key=lambda x: x.fval, reverse=False)

puzzle1 = Puzzle()
puzzle1.solvePuzzle()




























