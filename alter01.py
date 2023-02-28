#Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua
#situação em relação ao alistamento militar.
 #- Se estiver antes dos 18 anos, mostre em quantos anos faltam para o
#alistamento.
 #- Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do
#alistamento.

from datetime import date
nascimento = int(input("Nascimento: "))
idade = date.today().year - nascimento
if (idade < 18):
  print("Falta(m) {} ano(s) para o alistamento obrigatório.".format(18 - idade))
else:
  print("Já se passou {} ano(s) do alistamento obrigatório.".format(idade - 18))