1️⃣ A* (A-star) – forklaret simpelt
Hvad er A*?

A* er en søgealgoritme, der finder den bedste (korteste) vej fra start til mål.

Den er smart, fordi den:

    - bruger viden (heuristic)

    - men stadig tager den rigtige vej (i modsætning til greedy search)

--------------------------------------------------------------------------------------------------------------------------------
A*’s kerneidé (meget vigtigt)

A* vælger altid den node, der har lavest samlet score:

f(n) = g(n) + h(n)

Hvad betyder det?

    - g(n) → hvad har det kostet at komme hertil fra start?

    - h(n) → hvor langt tror vi der er til målet?

    - f(n) → hvor “god” er denne node samlet set?

👉 A* = “billig indtil nu” + “ser lovende ud”

--------------------------------------------------------------------------------------------------------------------------------


Intuition (maze-eksempel)

Forestil dig en maze:

    - g(n) = antal skridt du allerede har taget

    - h(n) = afstand til målet (fx Manhattan distance)

A* spørger:

    “Hvilken position virker samlet set bedst lige nu?”

--------------------------------------------------------------------------------------------------------------------------------
Hvad gør A* bedre end BFS?
BFS	                                                A*
Søger alle retninger	                            Søger mod målet
Langsom i store rum	                                Meget hurtigere
Ingen viden	                                        Bruger heuristic
Krav for at A* virker optimalt


Hvis h(n) aldrig overvurderer, så:

finder A* altid den korteste vej

(det kaldes admissible heuristic)
--------------------------------------------------------------------------------------------------------------------------------


2️⃣ A* – Pseudokode (note-venlig)

Det her er klassisk A* pseudokode (du må gerne skrive noget lignende til eksamen):

open_set = {start}
closed_set = {}

g(start) = 0
f(start) = h(start)

while open_set is not empty:
    current = node in open_set with lowest f(n)

    if current is goal:
        return path

    remove current from open_set
    add current to closed_set

    for each neighbor of current:
        if neighbor in closed_set:
            continue

        tentative_g = g(current) + cost(current, neighbor)

        if neighbor not in open_set or tentative_g < g(neighbor):
            parent(neighbor) = current
            g(neighbor) = tentative_g
            f(neighbor) = g(neighbor) + h(neighbor)

            if neighbor not in open_set:
                add neighbor to open_set


👉 Åbn-sæt = hvad vi kan vælge imellem
👉 Lukket-sæt = allerede undersøgt
--------------------------------------------------------------------------------------------------------------------------------


3️⃣ A* – Meget simpelt Python-eksempel (grid)

Det her er minimal A*, uden alt for meget støj.

Heuristic (Manhattan distance) :

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
--------------------------------------------------------------------------------------------------------------------------------

A* algoritme (simpel version) :

import heapq

def astar(start, goal, grid):
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            neighbor = (current[0] + dx, current[1] + dy)

            if neighbor not in grid:
                continue

            tentative_g = g_score[current] + 1

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f, neighbor))

    return None

--------------------------------------------------------------------------------------------------------------------------------

Path reconstruction :

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path
--------------------------------------------------------------------------------------------------------------------------------


Hvad du skal forstå (ikke memorere!)

    - A* bruger priority queue

    - Den vælger altid lavest f(n)

    - came_from bruges til at bygge stien bagefter
--------------------------------------------------------------------------------------------------------------------------------

Mini-cheat sheet (kort!)

    - A* = f(n) = g(n) + h(n)

    - g(n): faktisk pris

    - h(n): estimeret pris

    - admissible heuristic → optimal løsning

    - meget brugt i spil & pathfinding
--------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------