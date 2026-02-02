maze = [
    "*************",
    "* * * * *   *",
    "* * * *** * *",
    "* S***     *",
    "* * *** *  *",
    "* * *** * * *",
    "* * * *** * *",
    "* * *** * * *",
    "*  G*       *",
    "*************",
]

def pad_maze(lines):
    width = max(len(line) for line in lines)
    return [line.ljust(width) for line in lines]

def find_char(grid, ch):
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == ch:
                return (r, c)
    return None

def in_bounds(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def dfs(grid, current, goal, visited, path):
    if current == goal:
        path.append(current)
        return True

    visited.add(current)
    r, c = current

    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        nr, nc = r + dr, c + dc

        if not in_bounds(grid, nr, nc):
            continue
        if grid[nr][nc] == '*':
            continue
        if (nr, nc) in visited:
            continue

        if dfs(grid, (nr, nc), goal, visited, path):
            path.append(current)
            return True

    return False

def solve_maze(maze_lines):
    maze_lines = pad_maze(maze_lines)          # ✅ gør alle linjer lige lange
    grid = [list(row) for row in maze_lines]

    start = find_char(grid, 'S')
    goal = find_char(grid, 'G')

    if start is None or goal is None:
        raise ValueError("Maze must contain both 'S' (Start) and 'G' (Goal).")

    visited = set()
    path = []

    found = dfs(grid, start, goal, visited, path)

    # Print maze
    for row in grid:
        print("".join(row).rstrip())

    if not found:
        print("No path found.")
        return

    path.reverse()

    # Print path (row, col)
    print("path=" + "".join(f"({r},{c})" for r, c in path))

solve_maze(maze)

