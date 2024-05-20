def calcular_imc (peso, altura):
    imc = peso / (altura**2)
    return imc

peso = float(input("Fale o seu peso (kg): "))
altura = float(input("Me fale sua altura (m): "))
imc = calcular_imc(peso, altura)

# Informando o IMC para o usuário

print("Seu IMC é:", imc)

# Verificando a categoria com base no IMC calculado

if imc <= 18.5:
    categoria = "Abaixo do peso"
elif imc < 25:
    categoria = "Peso saudável"
elif imc < 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidade"

# Verificando se a categoria é "Peso saudável"

if categoria == "Peso saudável":
    print("Parabéns! Você está com um peso saudável.")
else:
    print("Vamos melhorar. Sua categoria é:", categoria)