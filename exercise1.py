import json
import csv

def lire_json_et_ecrire_csv(fichier_json, fichier_csv):
    with open(fichier_json, 'r') as f_json:
        nombres_complexes = json.load(f_json)
    
    with open(fichier_csv, 'w', newline='') as f_csv:
        writer = csv.writer(f_csv)
        writer.writerow(['reel', 'imaginaire'])
        for nombre in nombres_complexes:
            writer.writerow(nombre)

lire_json_et_ecrire_csv('data.json', 'nombres_complexes.csv')
