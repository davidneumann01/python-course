import tkinter as tk
from tkinter import ttk
import random
from tkinter import messagebox as mb


class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.destapadas = 0
        self.enjuego = True
        self.ventana1.geometry("500x500")
        self.ventana1.title("Buscaminas")
        self.ventana1.configure(background="#BEF781")
        self.generar_tablero()
        self.generar_bombas()
        self.generar_bombas_proximas()
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1)
        opciones1.add_command(label="Reiniciar", command=self.reiniciar)
        opciones1.add_command(label="Salir", command=self.ventana1.destroy)
        menubar1.add_cascade(label="Opciones", menu=opciones1)
        self.ventana1.mainloop()

    def generar_tablero(self):
        self.tablero = []
        listafila = []
        for fila in range(0, 10):
            for columna in range(0, 10):
                boton = ttk.Button(
                    self.ventana1,
                    text="",
                    command=lambda fi=fila, co=columna: self.presion(fi, co),
                )
                boton.place(x=columna * 50, y=fila * 50, width=50, height=50)
                listafila.append(boton)
            self.tablero.append(listafila)
            listafila = []

    def generar_bombas(self):
        self.bombas = []
        listafila = []
        for fila in range(0, 10):
            for columna in range(0, 10):
                listafila.append("0")
            self.bombas.append(listafila)
            listafila = []
        cantidad = 10
        while cantidad != 0:
            fila = random.randint(0, 9)
            columna = random.randint(0, 9)
            if self.bombas[fila][columna] != "b":
                self.bombas[fila][columna] = "b"
                # self.tablero[fila][columna].configure(text="b")
                cantidad = cantidad - 1

    def generar_bombas_proximas(self):
        for f in range(0, 10):
            for c in range(0, 10):
                if self.bombas[f][c] == "0":
                    cant = self.contar_lado(f, c)
                    self.bombas[f][c] = str(cant)

    def contar_lado(self, fila, columna):
        total = 0
        if fila - 1 >= 0 and columna - 1 >= 0:
            if self.bombas[fila - 1][columna - 1] == "b":
                total = total + 1
        if fila - 1 >= 0:
            if self.bombas[fila - 1][columna] == "b":
                total = total + 1
        if fila - 1 >= 0 and columna + 1 < 10:
            if self.bombas[fila - 1][columna + 1] == "b":
                total = total + 1
        if columna + 1 < 10:
            if self.bombas[fila][columna + 1] == "b":
                total = total + 1
        if fila + 1 < 10 and columna + 1 < 10:
            if self.bombas[fila + 1][columna + 1] == "b":
                total = total + 1
        if fila + 1 < 10:
            if self.bombas[fila + 1][columna] == "b":
                total = total + 1
        if fila + 1 < 10 and columna - 1 >= 0:
            if self.bombas[fila + 1][columna - 1] == "b":
                total = total + 1
        if columna - 1 >= 0:
            if self.bombas[fila][columna - 1] == "b":
                total = total + 1
        return total

    def presion(self, fila, columna):
        if self.enjuego:
            if self.bombas[fila][columna] == "b":
                self.enjuego = False
                self.destapar()
                mb.showinfo("Informacion", "Perdiste hay una bomba")
            else:
                if int(self.bombas[fila][columna]) == 0:
                    self.recorrer(fila, columna)
                else:
                    if (
                        int(self.bombas[fila][columna]) >= 1
                        and int(self.bombas[fila][columna]) <= 8
                        and self.tablero[fila][columna].cget("text") == ""
                    ):
                        self.tablero[fila][columna].configure(
                            text=self.bombas[fila][columna]
                        )
                        self.destapadas = self.destapadas + 1
            if self.destapadas == 90:
                self.enjuego = False
                mb.showinfo("Informacion", "Ganaste")

    def recorrer(self, fil, col):
        if fil >= 0 and fil < 10 and col >= 0 and col < 10:
            if self.bombas[fil][col] == "0" and self.tablero[fil][col] != None:
                self.bombas[fil][col] = " "
                self.destapadas = self.destapadas + 1
                self.tablero[fil][col].destroy()
                self.tablero[fil][col] = None
                self.recorrer(fil, col + 1)
                self.recorrer(fil, col - 1)
                self.recorrer(fil + 1, col)
                self.recorrer(fil - 1, col)
                self.recorrer(fil - 1, col - 1)
                self.recorrer(fil - 1, col + 1)
                self.recorrer(fil + 1, col + 1)
                self.recorrer(fil + 1, col - 1)
            else:
                if self.tablero[fil][col] != None:
                    if (
                        int(self.bombas[fil][col]) >= 1
                        and int(self.bombas[fil][col]) <= 8
                        and self.tablero[fil][col].cget("text") == ""
                    ):
                        self.tablero[fil][col].configure(text=self.bombas[fil][col])
                        self.destaádas = self.destapadas + 1

    def reiniciar(self):
        self.destapadas = 0
        self.eliminar_botones()
        self.generar_tablero()
        self.generar_bombas()
        self.generar_bombas_proximas()
        self.enjuego = True

    def eliminar_botones(self):
        for fila in range(0, 10):
            for columna in range(0, 10):
                if self.tablero[fila][columna] != None:
                    self.tablero[fila][columna].destroy()
                    self.tablero[fila][columna] = None

    def destapar(self):
        for fila in range(0, 10):
            for columna in range(0, 10):
                if self.tablero[fila][columna] != None:
                    if self.bombas[fila][columna] != "0":
                        self.tablero[fila][columna].configure(
                            text=self.bombas[fila][columna]
                        )


aplicacion1 = Aplicacion()
