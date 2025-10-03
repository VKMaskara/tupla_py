import os

os.system('cls')

print("="*50)
compras = ('arroz','feijão', 'alho', 'ovo', 'leite')
print(compras)
print(compras[1])
print(compras[0:2])
print(compras[0:8:2])
print(len(compras))
print("="*50)

for c in compras:
    print(c)
print("="*50)

for c in range(0,len(compras)):
    print(c)

print("="*50)

for c in range(0,len(compras)):

    print(f"{compras[c]} esta na posição {c + 1}")

print("="*50)

for item in compras:
    print(f"Eu vou comprar {item}")

print("="*50)

for c in range(0,len(compras)):
    print(f"Eu vou comprar {compras[c]} esta na posição {c + 1}")

print("="*50)

for pos, item in enumerate(compras):
  print(f"Eu  vou comprar {item} na posição {pos+1}")

print("="*50)

a = (1,2,3,4)
b = (5,7,2,0,8)
c = b+a

print(c)

print(c.count(4))

print(c.index(2))

print("="*50)

pessoa = ('Eu ', "m ", 1.88, 100) 