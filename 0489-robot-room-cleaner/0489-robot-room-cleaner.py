# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

DIRECTIONS = ((-1, 0), (0, 1), (1, 0), (0, -1))

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        curr_pos = (0, 0)
        visited = set()
        self.backtrack(curr_pos, robot,visited, 0)
        
    def backtrack(self, pos, robot, visited, dirt_idx):
        robot.clean()
        visited.add(pos)
        
        for i in range(4):
            new_dirt_idx = (dirt_idx + i) % 4
            d_row, d_col = DIRECTIONS[new_dirt_idx]
            nxt_pos = (pos[0] + d_row, pos[1] + d_col)
            if nxt_pos not in visited and robot.move():
                self.backtrack(nxt_pos, robot,visited, new_dirt_idx)
                self.go_back(robot)
            
            robot.turnRight()
            
    def go_back(self, robot):
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()
        
        
        