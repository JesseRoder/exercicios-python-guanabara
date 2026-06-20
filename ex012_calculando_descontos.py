# DESAFIO 012 - Crie um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Digite o preço do produto: R$ "))
desconto = preco * 0.05
novo_preco = preco - desconto
print("O novo preço do produto com 5% de desconto é: R$ {:.2f}".format(novo_preco))