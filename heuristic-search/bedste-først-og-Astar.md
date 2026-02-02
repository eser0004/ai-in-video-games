Heuristic Search – Slides (kort opsummering)
1️⃣ Hvad vil slidesene lære dig?

Slidesene viser:

    - forskellen på Best-First Search, Dijkstra og A*

    - hvordan priority queues bruges

    - hvordan heuristics påvirker rækkefølgen af søgning

    - eksempler med:

        - grafer

        - 8-puzzle

        - maze-lignende problemer

👉 Fokus er hvordan algoritmen vælger næste node

--------------------------------------------------------------------------------------------------------------------------------

2️⃣ Best-First Search (fra slides)

Best-First Search:

    - vælger node med lavest heuristisk værdi

    - bruger priority queue

    - prioritet:

    P(s,t) = price from start to state t

Vigtigt:

- ser kun på “hvad ser bedst ud nu”

- ingen garanti for korteste vej

Slidesene gennemgår trin-for-trin:

1. Push nye states på queue

2. Pop den bedste

3. Test om goal er nået

--------------------------------------------------------------------------------------------------------------------------------

3️⃣ Dijkstra (kort forklaret)

Dijkstra:

    - bruger kun g(n) (ingen heuristic)

    - finder altid korteste vej

    - men:

        - langsom

        - udforsker mange unødige noder

Slidesene bruger Dijkstra som kontrast til A*
--------------------------------------------------------------------------------------------------------------------------------

4️⃣ Heuristic Search (generelt)

Heuristic search:

    - bruger estimat til at styre søgning

    - stadig:

        - push

        - pop

        - test

    - forskellen er prioriteten

I slidesene:

    F(t) = P(s,t) + h(t)


👉 Det er A* forklaret i generel form
--------------------------------------------------------------------------------------------------------------------------------

5️⃣ A* i slidesene (meget vigtigt)

A* bruger:

    f(t) = g(t) + h(t)


Hvor:

    - g(t) = pris fra start til t

    - h(t) = estimeret pris til goal

Slidesene viser:

    - hvorfor A* er bedre end Best-First

    - hvorfor A* er hurtigere end Dijkstra
--------------------------------------------------------------------------------------------------------------------------------
6️⃣ Heuristics-eksempler (8-puzzle)

Slidesene viser to klassiske heuristics:

h₁: Hamming distance

    - antal brikker der er forkert placeret

    - hurtig, men grov

h₂: Manhattan distance

    - summen af afstande hver brik er fra sin rigtige plads

    - langsommere, men bedre

👉 Slidesene viser at:

    h₂ ≥ h₁

og derfor h₂ er mere informativ
--------------------------------------------------------------------------------------------------------------------------------
7️⃣ “Dominating heuristics”

Slidesene siger:

    Hvis h₂(n) ≥ h₁(n) for alle n, så dominerer h₂

Konsekvens:

- færre noder udvides

- hurtigere søgning

👉 Brug altid den mest præcise admissible heuristic

--------------------------------------------------------------------------------------------------------------------------------

8️⃣ Hvad du skal kunne forklare (vigtigt!)

Du skal kunne:

    - forklare forskel på:

        - Best-First

        - Dijkstra

        - A*

forklare:

    - g(n)

    - h(n)

    - f(n)

forklare hvorfor heuristic hjælper

--------------------------------------------------------------------------------------------------------------------------------
9️⃣ Ultra-kort slide-cheat-sheet

Best-First: bruger kun heuristic

    - Dijkstra: bruger kun cost

    - A*: cost + heuristic

    - Priority Queue styrer rækkefølgen

    - Bedre heuristic → hurtigere search
--------------------------------------------------------------------------------------------------------------------------------

📌 Hvordan det passer med Maze-opgaven

Slidesene er teorien.
Maze-opgaven er praktikken:

maze = grid

felter = states

naboer = moves

heuristic = afstand til mål

A* = algoritmen

👉 Det hele hænger direkte sammen.