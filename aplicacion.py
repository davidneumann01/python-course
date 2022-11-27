""" Confeccionar una aplicación visual con tkinter que permita ingresar en un control de tipo 
   'Entry' la URL de un sitio web y al presionar un botón recuperar los datos y mostrarlos en un control de tipo 'ScrolledText':
"""

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st
from tkinter import messagebox as mb
from urllib import request
from urllib import error

class Aplicacion:
	def __init__(self):
		self.ventana1=tk.Tk()
		self.label1=ttk.Label(text="Ingrese URL del sitio web:")
		self.label1.grid(column=0, row=0, pady=10)
		self.dato1=tk.StringVar()
		self.entry1=ttk.Entry(self.ventana1, width=100, textvariable=self.dato1)
		self.entry1.grid(column=0, row=1, pady=10)
		self.boton1=ttk.Button(self.ventana1, text="Recuperar", command=self.recuperar)
		self.boton1.grid(column=0, row=2, pady=10)
		self.scrolledtext1=st.ScrolledText(self.ventana1, width=100, height=30)
		self.scrolledtext1.grid(column=0,row=3, padx=10, pady=10)
		self.ventana1.mainloop()

	def recuperar(self):
		try:
			pagina=request.urlopen(self.dato1.get())
			datos=pagina.read().decode("utf-8")
			self.scrolledtext1.delete(1.0,tk.END)
			self.scrolledtext1.insert(tk.INSERT,datos)
		except error.HTTPError as err:
			mb.showinfo("Problemas", "No se puede aceder a dicho recurso")


aplicacion1=Aplicacion()
