# listas >> mutáveis
#listas guardam vários valores dentro de uma única variável

notas = [7.8, 8.2, 9.5]
disciplinas = ["matamática", "português", "geografia"]

#Adicionando uma nova disciplina
disciplinas.append("história")

#print(notas, type(notas),  type(notas[0]))

#Modificar a nota de matemática
notas[0] = notas[0] + 1

#Nota de história
notas.append(9)

print(f"A nota de {disciplinas[-3]} foi {notas[-3]}")
print(disciplinas[3])
print(notas[3])

#tuplas >> imutáveis

nomes = ("Maria", "João", "Paula")

print(nomes[0], nomes[-1])

#isso não funciona nas tuplas >> princípio da imutabilidade

nomes.append("Joaquim")
nomes[1] = "Marcelo"