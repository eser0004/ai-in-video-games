🧠 Heuristics & Heuristic Search (let forklaret)
1️⃣ Hvad er en heuristic?

En heuristic er et kvalificeret gæt.

👉 Den hjælper AI med at vurdere hvor tæt en state er på målet.

Ikke garanteret korrekt

Men hurtig og nyttig

Bruges til at styre søgning

Eksempel (maze)

Hvis målet er nederst til højre:

Heuristic = afstanden til målet

Jo tættere → jo bedre

--------------------------------------------------------------------------------------------------------------------------------

2️⃣ Heuristic function – h(n)

En heuristic skrives som:

h(n)


- n = nuværende state

- h(n) = estimeret afstand til goal

Typisk heuristic

Manhattan distance (grid/maze):

h(n) = |x1 - x2| + |y1 - y2|


👉 Ignorerer vægge → derfor kun et gæt

--------------------------------------------------------------------------------------------------------------------------------

3️⃣ Hvad er Heuristic Search?

Heuristic Search = search + viden

I stedet for at:

“prøve alt”

… så:

“prøver vi det, der ser bedst ud først”

Sammenligning
Type	                    Hvordan den vælger
Blind Search	            Tilfældigt / systematisk
Heuristic Search	        Bruger h(n)

--------------------------------------------------------------------------------------------------------------------------------



4️⃣ Best-First Search (idé)

Best-First Search:

- vælger altid den node med lavest h(n)

- “ser tættest på målet ud”

❌ Kan vælge dårlige veje
❌ Ikke altid optimal


--------------------------------------------------------------------------------------------------------------------------------


5️⃣ A* Search (vigtigst)

A* er den vigtigste heuristic search-algoritme.

Den bruger:

f(n) = g(n) + h(n)


Forklaring

- g(n) = pris fra start til n

- h(n) = estimeret pris fra n til mål

- f(n) = samlet vurdering

👉 Vælg node med lavest f(n)

--------------------------------------------------------------------------------------------------------------------------------

6️⃣ Hvorfor A* er smart

- Finder korteste vej

-  Hurtigere end BFS

-  Bruges i:

    - videospil

    - navigation

    - pathfinding

Hvis h(n) er “god”, er A* meget effektiv.



--------------------------------------------------------------------------------------------------------------------------------

7️⃣ Admissible heuristic (kort note)

En heuristic er admissible, hvis den:

    aldrig overvurderer den rigtige afstand

Eksempel:

- Manhattan distance → admissible

- “gæt med straf” → ikke admissible

👉 Admissible heuristic = A* finder optimal løsning

--------------------------------------------------------------------------------------------------------------------------------

8️⃣ Mini-overblik (eksamen-venligt)

Heuristic = kvalificeret gæt

-  h(n) = estimeret afstand til mål

-  Heuristic search = guidet søgning

-  A* = g(n) + h(n)

-  God heuristic = hurtig løsning
--------------------------------------------------------------------------------------------------------------------------------
