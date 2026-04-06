from pulp import *

joueurs = [
    {"nom": "Alice", "score": 88, "salaire": 1200, "poids": 72},
    {"nom": "Bob", "score": 91, "salaire": 1800, "poids": 85},
    {"nom": "Clara", "score": 84, "salaire": 950, "poids": 68},
    {"nom": "David", "score": 93, "salaire": 2100, "poids": 90},
    {"nom": "Emma", "score": 79, "salaire": 300, "poids": 65},
    {"nom": "Frank", "score": 87, "salaire": 2400, "poids": 95},
    {"nom": "Grace", "score": 85, "salaire": 1050, "poids": 70},
    {"nom": "Hugo", "score": 89, "salaire": 1600, "poids": 80}
]

probleme = LpProblem("Basket", LpMaximize)

xA = [LpVariable("xA_" + j['nom'], 0, 1, cat='Integer') for j in joueurs]
xB = [LpVariable("xB_" + j['nom'], 0, 1, cat='Integer') for j in joueurs]

probleme += lpSum([joueurs[i]["score"] * (xA[i] + xB[i]) for i in range(len(joueurs))])

probleme += lpSum(xA) == 3  
probleme += lpSum(xB) == 3  
probleme += lpSum([joueurs[i]["salaire"] * (xA[i] + xB[i]) for i in range(len(joueurs))]) <= 8500  
probleme += lpSum([joueurs[i]["poids"] * xA[i] for i in range(len(joueurs))]) <= 250  
probleme += lpSum([joueurs[i]["poids"] * xB[i] for i in range(len(joueurs))]) <= 250  

for i in range(len(joueurs)):
    probleme += xA[i] + xB[i] <= 1

probleme.solve(PULP_CBC_CMD(msg=False))

equipe_a = [joueurs[i] for i in range(len(joueurs)) if xA[i].value() == 1]
equipe_b = [joueurs[i] for i in range(len(joueurs)) if xB[i].value() == 1]

noms_a = [j['nom'] for j in equipe_a]
score_a = sum(j['score'] for j in equipe_a)
salaire_a = sum(j['salaire'] for j in equipe_a)
poids_a = sum(j['poids'] for j in equipe_a)

noms_b = [j['nom'] for j in equipe_b]
score_b = sum(j['score'] for j in equipe_b)
salaire_b = sum(j['salaire'] for j in equipe_b)
poids_b = sum(j['poids'] for j in equipe_b)

noms_str_a = ", ".join(noms_a)
noms_str_b = ", ".join(noms_b)

print("Équipe       | Joueurs                   | Score total | Salaire   | Poids")
print("")
print("Équipe A     | " + noms_str_a + "         | " + str(score_a) + " pts     | " + str(salaire_a) + " $    | " + str(poids_a) + " Kg")
print("Équipe B     | " + noms_str_b + "         | " + str(score_b) + " pts     | " + str(salaire_b) + " $    | " + str(poids_b) + " Kg")
print("Globalement  | Optimisé                  | " + str(score_a + score_b) + " pts     | " + str(salaire_a + salaire_b) + " $    | " + str(poids_a + poids_b) + " Kg")