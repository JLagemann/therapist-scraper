import pandas as pd

df = pd.read_csv("./EMDR_Psicologas.csv")
clinicos = df[df["Nivel"] == "Nivel II Adultos"].dropna()

ingles = clinicos[clinicos["Idioma"].str.contains("Inglés")]
ingles.to_csv("./English_nivelII.csv")