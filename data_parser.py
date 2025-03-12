import json
import pandas as pd

with open("./psico.json") as f:
    j = json.load(f)

def parse_details(details):
    result = {}
    for d in details:
        t = d.split(":")
        if len(t) > 1:
            result[t[0]] = t[1]
    return result

data = []
for psi in j:
    ficha = parse_details(psi["Detalles"])
    ficha["Name"] = psi['Psicologo'][0]
    data.append(ficha)
    # print(ficha)

df = pd.DataFrame(data)
df.to_csv("./EMDR_Psicologas.csv")

