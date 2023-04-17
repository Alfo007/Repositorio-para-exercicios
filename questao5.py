'''
5) Escreva um programa que inverta os caracteres de um string.]
'''
normal = "Edinaldo"
inverter = ""  

for i in range(len(normal)-1, -1, -1):
    inverter += normal[i]
print(inverter) 
