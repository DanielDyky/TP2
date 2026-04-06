
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

def glouton(liste_joueurs, strategie):
   
    equipe_a = []
    equipe_b = []
    
   
    poids_a = 0
    poids_b = 0
    budget_utilise = 0
    score_total = 0

    
    for j in liste_joueurs:
        
       
        if len(equipe_a) < 3:
           
            if (poids_a + j["poids"] <= 250) and (budget_utilise + j["salaire"] <= 8500):
                equipe_a.append(j)
                poids_a += j["poids"]
                budget_utilise += j["salaire"]
                score_total += j["score"]
                continue 
                
        
        if len(equipe_b) < 3:
            if (poids_b + j["poids"] <= 250) and (budget_utilise + j["salaire"] <= 8500):
                equipe_b.append(j)
                poids_b += j["poids"]
                budget_utilise += j["salaire"]
                score_total += j["score"]

    
    if len(equipe_a) < 3 or len(equipe_b) < 3:
        print(f"\nErreur pour la stratégie: {strategie}, équipes incomplètes.")

    return score_total, budget_utilise


score = sorted(joueurs, key=lambda joueur: joueur["score"], reverse=True)
salaire = sorted(joueurs, key=lambda joueur: joueur["score"] / joueur["salaire"], reverse=True)
poids = sorted(joueurs, key=lambda joueur: joueur["score"] / joueur["poids"], reverse=True)


score_a, budget_a = glouton(score, "Score absolu")
score_b, budget_b = glouton(salaire, "Ratio salaire")
score_c, budget_c = glouton(poids, "Ratio poids")

meilleur_score = 525  

def ecart(score_obtenu, score_optimal):
    diff = score_obtenu - score_optimal
    if diff == 0:
        return "---"
    pourcentage = (diff / score_optimal) * 100
    return f"{diff} pts ({pourcentage:.1f}%)"


print("Stratégie         | Score total    | Budget     | Écart vs Optimal")
print("")
print("Score absolu      | " + str(score_a) + " pts        | " + str(budget_a) + " $     | " + ecart(score_a, meilleur_score))
print("Ratio salaire     | " + str(score_b) + " pts        | " + str(budget_b) + " $     | " + ecart(score_b, meilleur_score))
print("Ratio poids       | " + str(score_c) + " pts        | " + str(budget_c) + " $     | " + ecart(score_c, meilleur_score))
print("PuLP              | " + str(meilleur_score) + " pts        | 8050 $     | ---")