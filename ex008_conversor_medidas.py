# DESAFIO 008 - Escreva um programa que leia um valor em metros e o exiba convertido em km, hm, dam, m, dm, cm e mm.

valor = float(input("Digite um valor em metros: "))
print(f" {valor} m = {valor / 1000} km \n {valor} m = {valor / 100} hm \n {valor} m =  {valor / 10} dam \n {valor} m = {valor} m \n {valor} m = {valor * 10} dm \n {valor} m = {valor * 100} cm \n {valor} m = {valor * 1000} mm.") 
