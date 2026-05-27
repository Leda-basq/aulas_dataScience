import pandas as pd
import matplotlib.pylab as plt
import numpy as np

print("=== FORMULÁRIO SOBRE FILMES ===\n")

filme_favorito = input("1. Qual é o seu filme favorito? ")
genero_favorito = input("2. Qual gênero de filme você mais gosta? ")
filmes_mes = int(input("3. Quantos filmes você assiste por mês? "))
nota_cinema = float(input("4. De 0 a 10, qual sua nota para a experiência de ir ao cinema? "))
horas_filmes = float(input("5. Quantas horas por semana você passa assistindo filmes? "))

print("\n=== RESPOSTAS REGISTRADAS ===")
print(f"Filme favorito: {filme_favorito}")
print(f"Gênero favorito: {genero_favorito}")
print(f"Filmes assistidos por mês: {filmes_mes}")
print(f"Nota para o cinema: {nota_cinema}")
print(f"Horas por semana assistindo filmes: {horas_filmes}")