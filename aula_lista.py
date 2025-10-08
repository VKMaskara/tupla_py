'''
compras =['arroz','feijão', 'alho', 'ovo', 'leite']

print(compras)
print(compras[1])
print(compras[0:2])
print(len(compras))
print(compras[0:8:2])

print("="*50)

compras[3]="frango"

print(compras)
print("="*50)

compras[1]="feijoada"
print(compras)
print("="*50)

compras.append("Café")
print(compras)
print(len(compras))
print("="*50)

compras.insert(0,"Batata")
print(compras)

print("="*50)

del compras[3]
#compras.pop(3)
#compras.remove("alho")

print(compras)
compras.append("chocolate")

print("="*50)
if 'chocolate'in compras:
 compras.remove("chocolate")
 print("ITEM REMOVIDO COM SUCESSO")
 print(compras)
else:
  print("NÃO A O ITEM CHOCOLATE")

  print("="*50)

valores=list(range(4,11))

print(valores)

print("="*50)
aleatotio = [10,50,3,4,8,4,9,1,]
aleatotio.sort()
print(aleatotio)

print("="*50)
aleatotio.sort(reverse=True)
print(aleatotio)



print("="*50)

val = [] #lista vazia

val.append(5)
val.append(6)
val.append(6)

print(val)

print("="*50)

for v in val:
  print(f"{v}...")

print("="*50)
for v in val:
  print(f"{v}...", end="")

print("="*50)

for c, v in enumerate(val):
  print (f"Na posição {c+1} encontreio valor {v}")
print("Cheguei ao final da lista")

print("="*50)


lista_usu=list()

for cont in range(0,5):
    print("\n")
    lista_usu.append(input("Digite um valor:"))
print("\n")
for c, v in enumerate(lista_usu):
  print (f"Na posição {c+1} encontreio valor {v}")
print("Cheguei ao final da lista")'''


print("="*50)


a=[1,2,3,4]
b=a[:]
b[2]=8
print(f"Lista A = {a}")
print(f"Lista B = {b}")