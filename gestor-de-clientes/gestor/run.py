import menu
import sys
import ui

if __name__ == "__main__":
    # Si pasamos un argumento -t lanzamos el modo terminal
    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        menu.iniciar()
    # En cualquier otro caso lanzamos el modo grafico
    else:
        app = ui.MainWindow()
        app.mainloop()
