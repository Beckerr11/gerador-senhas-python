import random
import string

tamanho = int(input("Tamanho da senha: "))

caracteres = string.ascii_letters + string.digits + string.punctuation

senha = "".join(random.choice(caracteres) for i in range(tamanho))

print("Senha gerada:", senha)
