class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "L": 
                    count += 1
                    stack = [(i, j)]
                    while stack:
                        row, col = stack.pop()
                        grid[row][col] = "W"
                        if row + 1 < rows and grid[row + 1][col] == "L":
                            stack.append((row + 1, col))
                        if row - 1 >= 0 and grid[row - 1][col] == "L":
                            stack.append((row - 1, col))
                        if col + 1 < cols and grid[row][col + 1] == "L":
                            stack.append((row, col + 1))
                        if col - 1 >= 0 and grid[row][col - 1] == "L":
                            stack.append((row, col - 1))

        return count
