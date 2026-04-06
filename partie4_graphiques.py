import matplotlib.pyplot as plt

# Graph 1: Comparaison des algorithmes

strategies = ["Score absolu", "Ratio salaire", "Ratio poids", "PuLP"]
scores = [525, 516, 516, 525]
couleurs = ['blue', 'red', 'green', 'yellow']

plt.figure(figsize=(8, 5))
plt.bar(strategies, scores, color=couleurs)

plt.axhline(y=525, color='pink', linestyle='--', label='PuLP (525 pts)')

plt.title("Comparaison du score total par algorithme")
plt.ylabel("Score Total")
plt.ylim(500, 530) 
plt.legend()
plt.show()



# Graph 2 : Croissance du nombre d'appels récursifs

appels_naif = 0
def fib_naif(n):
    global appels_naif
    appels_naif += 1
    if n == 0: return 93
    if n == 1: return 91
    return fib_naif(n-1) + fib_naif(n-2)

cache = {}
appels_memo = 0
def fib_memo(n):
    global appels_memo
    appels_memo += 1
    if n in cache: 
        return cache[n]
    if n == 0: return 93
    if n == 1: return 91
    resultat = fib_memo(n-1) + fib_memo(n-2)
    cache[n] = resultat
    return resultat

valeurs_n = list(range(1, 26))
liste_naif = []
liste_memo = []

for n in valeurs_n:
    appels_naif = 0
    fib_naif(n)
    liste_naif.append(appels_naif)
    
    appels_memo = 0
    cache.clear()
    fib_memo(n)
    liste_memo.append(appels_memo)

plt.figure(figsize=(8, 5))
plt.plot(valeurs_n, liste_naif, color='red', marker='o', label='Naif O(2^n)')
plt.plot(valeurs_n, liste_memo, color='green', marker='x', label='Mémoisé O(n)')


plt.yscale('log')
plt.title("Croissance des appels récursifs")
plt.xlabel("Valeur de n")
plt.ylabel("Nombre d'appels")
plt.legend()
plt.show()


# Graph 3: Répartition du budget et du poids par équipe
noms_equipes = ['Équipe A', 'Équipe B']
budgets = [2950, 5100]
poids = [215, 247]

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1) 

plt.bar(noms_equipes, budgets, color=['blue', 'blue'])
plt.axhline(y=8500, color='red', linestyle='--', label='Maximum (8500 $)')
plt.title("Budget")
plt.ylabel("Dollars ($)")
plt.legend()



plt.subplot(1, 2, 2) 

plt.bar(noms_equipes, poids, color=['red', 'red'])
plt.axhline(y=250, color='red', linestyle='--', label='Maximum (250 Kg)')
plt.title("Poids")
plt.ylabel("Kg")
plt.legend()

plt.tight_layout() 

plt.show()