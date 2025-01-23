import random

codigos = "*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = 5  # Número de dígitos que quieres en la contraseña
contrasena = ""

for _ in range(longitud):
    contrasena += random.choice(codigos)

print("Tu contraseña de 5 dígitos es:", contrasena)