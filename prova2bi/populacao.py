# QUESTÃO 5
popuEike = 5000
popuApollo = 3000
ano = 0

while popuApollo <= popuEike:
    popuEike += popuEike * 0.004   # crescimento de 0,4% ao ano
    popuApollo += popuApollo * 0.009  # crescimento de 0,9% ao ano
    ano += 1

print(f"A cidade de Apollo ultrapassará Eike em {ano} anos.")
print(f"População de Eike: {int(popuEike)} habitantes")
print(f"População de Apollo: {int(popuApollo)} habitantes")
