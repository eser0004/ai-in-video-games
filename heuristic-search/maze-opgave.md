🧩 Maze-opgaven – samlet forklaring & løsning
🔹 Hvad opgaven beder om (kort)

Du skal:

1. Repræsentere en maze (Start, Goal, vægge)

2. Finde en vej fra Start → Goal

👉 med rekursiv Depth-First Search (DFS)

3. Forklare:

- hvad er en state

- hvad er en operation

4. Udskrive:

- mazen

- stien som (row, column)

Alt dette står direkte i PDF’en 

Maze (1)
--------------------------------------------------------------------------------------------------------------------------------

1️⃣ Repræsentation af maze (krav 1)

Vi repræsenterer mazen som en liste af strings:

1. * = væg

2. = fri vej

3. S = Start

4. G = Goal

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


Koordinater:

    (row, col)

    øverste venstre hjørne = (0,0)
(præcis som PDF’en kræver)
--------------------------------------------------------------------------------------------------------------------------------

2️⃣ DFS – rekursiv algoritme (krav 2)

Vi bruger rekursiv Depth-First Search, som opgaven siger.

Hjælpefunktioner:


def find_char(grid, ch):
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == ch:
                return (r, c)

def in_bounds(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])
--------------------------------------------------------------------------------------------------------------------------------
Rekursiv DFS:

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

--------------------------------------------------------------------------------------------------------------------------------

3️⃣ State & Operation (krav 3 – teori)

State:
Agentens nuværende position i mazen, fx (3,7).

Operation:
Et lovligt træk til en nabo:

    - op

    - ned

    - venstre

    - højre
(hvis feltet ikke er en væg)

👉 Det er præcis definitionen på state space i maze-problemer
--------------------------------------------------------------------------------------------------------------------------------

🧠 Vigtige noter (eksamen/aflevering)

    DFS er rekursiv

    Ikke garanteret korteste vej

    Finder en vej

    Meget simpel og let at implementere
--------------------------------------------------------------------------------------------------------------------------------

🔗 Sammenhæng med Heuristic Search

    - Maze + DFS = blind search

    - Maze + A* = heuristic search

    - Samme problem, bedre algoritme

👉 Det er præcis derfor I har haft:

    1. Blind search

    2. Heuristic search

    3. Maze-opgaven
