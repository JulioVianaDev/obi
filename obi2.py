lista = []
partidas = 6
for i in range(partidas):
  lista.append(str(input()))
vitorias = 0
for partida in lista:
  if partida == 'V':
    vitorias += 1
grupo = 0
if vitorias > 4:
  grupo = 1
elif vitorias > 2 and vitorias< 5 :
  grupo = 2 
elif vitorias > 3 and vitorias > 0:
  grupo = 3
else:
  grupo = -1 
print(grupo)
