megas = int(input())
meses = int(input())
gastou = 0 
total = 0
for mes in range(meses):
  gastou = int(input())
  total += gastou 
limite = megas  * (meses + 1)
proximo = limite  -  total
print(proximo)