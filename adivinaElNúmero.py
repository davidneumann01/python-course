# Este es el juego de adivina el número.
import random


class Main:
    def __init__(self):
        self.miNombre = input("¡Hola! ¿Cómo te llamas?:")
        self.juego()

    def juego(self):
        intentosRealizados = 0
        intentos = 5
        número = random.randint(1, 20)
        print(f"Bueno. {self.miNombre}, estoy pensando en un número entre 1 y 20,")
        while intentosRealizados < 6:
            estimación = int(input("Intenta adivinar."))
            intentosRealizados = intentosRealizados + 1
            if estimación < número:
                print(
                    f"Tu estimacion es muy baja.(te quedan {intentos} intentos)"
                )  # Hay ocho espacios delante de print.
                intentos = intentos - 1
            elif estimación > número:
                print(f"Tu estimación es muy alta.(te quedan {intentos} intentos)")
                intentos = intentos - 1
            elif estimación == número:
                break

        if estimación == número:
            intentosRealizados = str(intentosRealizados)
            print(
                f"¡Buen trabajo, {self.miNombre}! ¡Has adivinado mi número en {intentosRealizados} intentos!"
            )
            r = input("Presiona intro para finalizar o [r] para volver a jugar:")
            if r == "r" or r == "R":
                self.juego()
            else:
                exit()
            exit()

        elif estimación != número:
            número = str(número)
            print(f"Pues no. El número que estaba pensando era {número}")
            s = input("Ingresa s para volver a jugar o presiona intro para finalizar")
            if s == "s" or s == "S":
                self.juego()
            else:
                exit()


# bloque principal

jugar = Main()
