""" Desarrollar un programa que permita recorrer un laberinto e indique si tiene salida o no empleando la librería tkinter.
Para resolver este problema al laberinto lo representaremos con una lista de 10 elementos de tipo lista que en cada una hay 10 Label.
El valor: 
0   Representa pasillo
1   Representa pared
9   Persona
5   Salida
A la salida ubicarla en la componente de la fila 9 y columna 9.
La persona comienza a recorrer el laberinto en la fila 0 y columna 0.
Los ceros y unos disponerlos en forma aleatoria."""

import tkinter as tk
from tkinter import ttk
import random


class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Laberinto")
        self.salida = False
        self.generar_laberinto()
        self.boton1 = ttk.Button(self.ventana1, text="Recorrer", command=self.analizar)
        self.boton1.grid(column=0, row=10, columnspan=5, padx=10, pady=10)
        self.boton2 = ttk.Button(
            self.ventana1, text="Generar otro", command=self.generar_otro
        )
        self.boton2.grid(column=5, row=10, columnspan=5, padx=10, pady=10)
        self.ventana1.mainloop()

    def generar_laberinto(self):
        self.tablero = []
        listafila = []
        for fila in range(0, 10):
            for columna in range(0, 10):
                label = ttk.Label(
                    self.ventana1, text=self.retornar_aleatorio(), foreground="red"
                )
                label.grid(column=columna, row=fila, padx=10, pady=10)
                listafila.append(label)
            self.tablero.append(listafila)
            listafila = []
        self.tablero[0][0].configure(text=0)
        self.tablero[9][9].configure(text=5)

    def generar_otro(self):
        for fila in range(0, 10):
            for columna in range(0, 10):
                self.tablero[fila][columna].configure(
                    text=self.retornar_aleatorio(), background="#f0f0f0"
                )
        self.tablero[0][0].configure(text=0)
        self.tablero[9][9].configure(text=5)

    def retornar_aleatorio(self):
        valor = random.randint(1, 4)
        if valor == 1:
            return 1
        else:
            return 0

    def analizar(self):
        self.salida = False
        self.recorrer(0, 0)
        if self.salida:
            self.ventana1.title("Tiene salida el laberinto")
        else:
            self.ventana1.title("No tiene salida el laberinto")

    def recorrer(self, fil, col):
        if fil >= 0 and fil < 10 and col >= 0 and col < 10 and self.salida == False:
            if self.tablero[fil][col].cget("text") == 5:
                self.salida = True
            else:
                if self.tablero[fil][col].cget("text") == 0:
                    self.tablero[fil][col].configure(text=9)
                    self.tablero[fil][col].configure(background="Yellow")
                    self.recorrer(fil, col + 1)
                    self.recorrer(fil + 1, col)
                    self.recorrer(fil - 1, col)
                    self.recorrer(fil, col - 1)


aplicacion1 = Aplicacion()
