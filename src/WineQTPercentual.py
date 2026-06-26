import pandas as pd

df = pd.read_csv("./data/WineQT.csv")

total_vinhos = len(df)
vinhos_alta_qualidade = (df["quality"] >= 7).sum()
vinhos_baixa_media_qualidade = (df["quality"] < 7).sum()

percentual_alta = vinhos_alta_qualidade / total_vinhos * 100
percentual_baixa_media = vinhos_baixa_media_qualidade / total_vinhos * 100

print(f"Total de vinhos: {total_vinhos}")
print(f"Vinhos de alta qualidade: {vinhos_alta_qualidade} ({percentual_alta:.2f}%)")
print(f"Vinhos de baixa/média qualidade: {vinhos_baixa_media_qualidade} ({percentual_baixa_media:.2f}%)")