from tkinter import *
from tkinter import ttk
from collections import deque

a = "mano"
long = len(a)

def iniciarjuego():
    global entry, cv, z
    f1.destroy()

    f2 = Frame(interfaz, width=1, height=1, bg='black')
    f2.pack(side="top")

    cv = Canvas(f2, bg="#ffffff", width=600, height=600)
    cv.pack()

    for i in range(30, 550, int(550 / long)):
        for j in range(25, 575, 100):
            cv.create_rectangle(i, j, i + int(550 / long), j + 70, fill='white')


    input_frame = Frame(interfaz, bg='grey')
    input_frame.pack(side='top', pady=10)

    entry = Entry(input_frame, width=10, justify="left", font=["Arial", 30])
    entry.focus_set()
    entry.pack(side='left', padx=10)
    z = 55 

    class Letra:
        def __init__(self, letra):
            self.letra = letra
            self.n_repeticiones = 1

        def incrementar_repeticiones(self):
            self.n_repeticiones += 1

    # Función para agregar o actualizar una letra en el conjunto
    def agregar_letra(conjunto_letras, letra):
        # Buscar la letra en el conjunto
        letra_existente = next((l for l in conjunto_letras if l.letra == letra), None)

        # Si la letra ya existe, incrementar las repeticiones
        if letra_existente:
            letra_existente.incrementar_repeticiones()
        else:
            # Si no existe, crear una nueva instancia de Letra
            nueva_letra = Letra(letra)
            # Agregar la nueva letra al conjunto
            conjunto_letras.add(nueva_letra)

    def asignar_colores_palabra(palabra_escogida):
        global a # a es la palabra correcta

        conj_letras_palabra_correcta = set()
        for letra in a:
            agregar_letra(conj_letras_palabra_correcta, letra)

        #conj = set(a) # se debe implementar grafos o diccionarios para casos de letras repetidas
        colores = list()
        for i in range(len(palabra_escogida)):
            if any(letra_obj.letra == palabra_escogida[i] for letra_obj in conj_letras_palabra_correcta) and palabra_escogida[i] == a[i]:
                colores.append("green")
            elif any(letra_obj.letra == palabra_escogida[i] for letra_obj in conj_letras_palabra_correcta):
                colores.append("yellow")
            else:
                colores.append("black")
        return colores
        
    def ingresar_intento():
        global z  # Declare z as a global variable

        intento = entry.get()

        colores = asignar_colores_palabra(intento)
        
        longitudesy = [100, 100, 90, 80, 70]
        longitudes = [130, 104, 87, 74, 65]
        for i in range(long):
            cv.create_text(longitudesy[long - 4] + i * longitudes[long - 4], z, text=intento[i], 
                           font=("Arial", 55), fill=colores[i])
        z += 100
        print("el intento fue", intento)
        entry.delete(0, END)

    ttk.Button(input_frame, text="Ingresar intento", width=20, command=ingresar_intento).pack(side='left', pady=0, padx=10)

interfaz = Tk()
interfaz.title('Wordle')
interfaz.geometry('600x690')
interfaz.config(bg='grey')
interfaz.resizable(width=False, height=False)

f1 = Frame(interfaz, width=800, height=800, bg='grey', pady=100)
f1.pack(side="top")

boton_iniciar_juego = Button(f1, text='Iniciar Juego de Wordle', font=("Arial", 30),
                             bg='yellow', command=iniciarjuego, justify="center", width=18, height=4, padx=82, pady=100)
boton_iniciar_juego.grid(row=0, column=0, padx=7)



interfaz.update()
interfaz.mainloop()
