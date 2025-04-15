frase = 'Python é massa'

palavras = frase.split()

print(palavras)

invertida = [p[::-1] for p in palavras]

print(invertida)

resultado = " ".join(invertida)
print(resultado)