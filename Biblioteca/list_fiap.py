# inventario=[]
# resposta="S"
# while resposta == "S":
#     inventario.append(input("Equipamento...........: ").upper())
#     inventario.append(float(input("Valor...........: ")))
#     inventario.append(int(input("Serial............: ")))
#     inventario.append(input("Departamento..........: ").upper())
#     resposta=input("Digite \"S\" para continuar: ").upper()
#
# for elemento in inventario:
#     print(elemento)

# inventario=[]
# resposta="S"
# while resposta == "S":
#     inventario.append(input("Equipamento: ").upper())
#     inventario.append(float(input("Valor: ")))
#     inventario.append(int(input("Numero Serial: ")))
#     inventario.append(input("Departamento: ").upper())
#     resposta=input("Digite \"S\" para continuar: ").upper()
#
# print(f"Equipamento.....: {inventario[0]}")
# print(f"Valor...........: {inventario[1]}")
# print(f"Serial..........: {inventario[2]}")
# print(f"Departamento....: {inventario[3]}")

equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento: ").upper())
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Numero Serial: ")))
    departamentos.append(input("Departamento: ").upper())
    resposta = input("Digite \"S\" para continuar: ").upper()

for indice in range(0, len(equipamentos)):
    #print("\nID..: ", (indice+1))
    print("\nEquipamento............: ", equipamentos[indice])
    print("Valor...........: ", valores[indice])
    print("Serial..........: ", seriais[indice])
    print("Departamento....: ", departamentos[indice])