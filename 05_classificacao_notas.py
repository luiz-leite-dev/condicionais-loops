soma = 0

for numero in range(1, 4):
    nota = float(input(f"Digite a nota {numero}: "))
    soma += nota

media = soma / 3

if media >= 7:
    resultado = "Aprovado"
elif media >= 5:
    resultado = "Em recuperação"
else:
    resultado = "Reprovado"

print(f"Média: {media:.1f}")
print(f"Resultado: {resultado}")