import time

joueurs = [
    {"nom": "Alice", "score": 88}, {"nom": "Bob", "score": 91},
    {"nom": "Clara", "score": 84}, {"nom": "David", "score": 93},
    {"nom": "Emma", "score": 79}, {"nom": "Frank", "score": 87},
    {"nom": "Grace", "score": 85}, {"nom": "Hugo", "score": 89}
]

joueurs_tries = sorted(joueurs, key=lambda j: j["score"], reverse=True)

def score_cumule(liste, k):
    if k == 0:
        print("score_cumule(joueurs, 0) = 0")
        return 0
    
    score_precedent = score_cumule(liste, k-1)
    
    score_actuel = liste[k-1]["score"]
    nom = liste[k-1]["nom"]
    total = score_precedent + score_actuel
    

    print("score_cumule(joueurs, " + str(k) + ") = " + str(score_precedent) + " + " + str(score_actuel) + " (" + nom + ") = " + str(total))
    return total

print("Score cumulatif")
score_cumule(joueurs_tries, 3)
print("")


appels_naif = [0]
appels_memoisation = [0]

def fib_naif(n):
    appels_naif[0] += 1
    if n == 0: return 93 
    if n == 1: return 91 
    return fib_naif(n-1) + fib_naif(n-2)

cache = {}

def fib_memo(n):
    appels_memoisation[0] += 1
    if n in cache: 
        return cache[n]
    if n == 0: 
        return 93
    if n == 1: 
        return 91
    
    resultat = fib_memo(n-1) + fib_memo(n-2)
    cache[n] = resultat
    return resultat

debut_naif = time.perf_counter()
resultat_naif = fib_naif(35)
fin_naif = time.perf_counter()
temps_naif = round(fin_naif - debut_naif, 3)

debut_memoisation = time.perf_counter()
resultat_memoisation = fib_memo(35)
fin_memoisation = time.perf_counter()
temps_memoisation = round(fin_memoisation - debut_memoisation, 6)


print("Version (n=35) | Résultat   | Temps      | Nb Appels")
print("")
print("Naif          | " + str(resultat_naif) + "   | " + str(temps_naif) + " s    | " + str(appels_naif[0]))
print("Mémoisé       | " + str(resultat_memoisation) + "   | " + str(temps_memoisation) + " s  | " + str(appels_memoisation[0]))