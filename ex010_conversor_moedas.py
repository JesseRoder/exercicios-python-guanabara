# DESAFIO 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere 1 US$ = R$ 5.15

real = float(input("Quantos reais você tem na carteira? R$ "))
dolar = real / 5.15
print("Com R$ {:.2f}, você pode comprar US$ {:.2f}.".format(real, dolar))