import csv

def charger_pokemons_csv(fichier_csv):
    pokemons = {}
    with open(fichier_csv, 'r') as f_csv:
        reader = csv.reader(f_csv)
        for row in reader:
            nom = row[0]
            stats = list(map(int, row[1:]))
            pokemons[nom] = stats
    return pokemons

mn = charger_pokemons_csv('pokemon.csv')
for nom, stats in pkmn.items():
    print(f"{nom}: {stats}")
