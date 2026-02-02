Forberedelse – A* (Lester)

Kort opsummering

Hvad handler teksten om?

Dokumentet forklarer A* fra bunden:

    - hvordan man finder en vej i et grid/maze

    - hvordan computeren “tænker”

    - hvorfor A* er bedre end blind search

Alt er forklaret med felter (nodes), åbne/lukkede lister og F = G + H 


--------------------------------------------------------------------------------------------------------------------------------

1️⃣ Problemet A* løser

    Find den korteste vej fra Start (A) til Goal (B) i et område med forhindringer.

Typisk:

    - maze

    - grid

    - spilkort

    - pathfinding i spil
--------------------------------------------------------------------------------------------------------------------------------

2️⃣ Repræsentation (meget vigtigt)

Området deles op i et grid:

hvert felt = node

hver node kan være:

walkable

wall

start

goal

👉 Det gør problemet diskret og simpelt 

--------------------------------------------------------------------------------------------------------------------------------

3️⃣ Open list & Closed list
Open list

    - felter vi kan vælge imellem

    - kandidater til næste skridt

Closed list

    - felter vi allerede har undersøgt

    - kommer aldrig i spil igen

👉 A* arbejder ved konstant at flytte noder fra open → closed
--------------------------------------------------------------------------------------------------------------------------------


4️⃣ F = G + H (kernen i A*)
G (cost so far)

    - pris fra start → nuværende node

    - typisk:

        - 10 for vandret/lodret

        - 14 for diagonal (≈ √2)


H (heuristic)

    - estimat til målet

    -bruges Manhattan distance:

    H  = |x1 - x2| + |y1 - y2|

F (total score)

    F = G + H


👉 A* vælger altid laveste F
--------------------------------------------------------------------------------------------------------------------------------

5️⃣ Sådan kører A* (trin-for-trin)

    1. Læg start i open list

    2. Vælg node med lavest F

    3. Flyt den til closed list

    4. Undersøg naboer:

        - ignorér walls

        - ignorér closed

        - opdatér G, H, F

        - gem parent

    5. Gentag indtil:

        - goal findes

        - open list er tom (ingen løsning)
--------------------------------------------------------------------------------------------------------------------------------

6️⃣ Parent pointers (hvordan man får stien)

Når goal er fundet:

gå baglæns:

    goal → parent → parent → ... → start


Det er selve path outputtet
--------------------------------------------------------------------------------------------------------------------------------

7️⃣ Hvorfor A* er god til spil

-  hurtig

-  realistisk bevægelse

-  kan justeres (terrain cost, penalties)

standard i:

    - RTS

    - RPG

    - FPS
--------------------------------------------------------------------------------------------------------------------------------

8️⃣ Vigtig sammenligning (fra teksten)
Algoritme	    Heuristic	    Resultat
BFS	            ❌	           langsom
DFS	            ❌	           dårlig path
Dijkstra	    ❌	           korrekt men langsom
A*	            ✅	           hurtig + optimal
--------------------------------------------------------------------------------------------------------------------------------

9️⃣ Det du IKKE behøver nu

Du kan roligt springe over:

    - collision avoidance

    - influence maps

    - smoothing paths

    - performance-optimering

👉 Det er ekstra, ikke pensum
--------------------------------------------------------------------------------------------------------------------------------

9️⃣ Det du IKKE behøver nu

Du kan roligt springe over:

    - collision avoidance

    - influence maps

    - smoothing paths

    - performance-optimering

👉 Det er ekstra, ikke pensum
--------------------------------------------------------------------------------------------------------------------------------
Ultra-kort “eksamens-opsummering”

    A* finder den korteste vej ved at kombinere faktisk afstand (G) og estimeret afstand (H). Den bruger en open list og closed list og vælger altid noden med lavest F = G + H.
--------------------------------------------------------------------------------------------------------------------------------