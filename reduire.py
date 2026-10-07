import pandas as pd

# Mets le chemin complet vers ton fichier CSV
df = pd.read_csv(r"C:\Users\dell\Desktop\Power Bi\job_postings_flat.csv", nrows=20000)

df.to_csv(r"C:\Users\dell\Desktop\Power Bi\echantillon.csv", index=False)
print("Fichier echantillon.csv créé avec succès !")