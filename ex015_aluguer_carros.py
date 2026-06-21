# DESAFIO 015 - Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

km = float(input("Digite a quantidade de km percorridos: "))
dias = int(input("Digite a quantidade de dias pelo qual o carro foi alugado: "))
preco = (dias * 60) + (km * 0.15)
print(f"O preço a pagar é: R$ {preco:.2f}")