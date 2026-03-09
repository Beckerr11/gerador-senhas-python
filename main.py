import random
import string

print("Gerador de Senhas")

tamanho = int(input("Digite o tamanho da senha: "))

caracteres = string.ascii_letters + string.digits + string.punctuation

senha = ""

for i in range(tamanho):
    senha += random.choice(caracteres)

print("Senha gerada:", senha)
