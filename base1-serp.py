# Trabajo 1 Estructura de Datos
#
# Snake Game
#
# Integrantes:
# + Hans Guillermo García Vargas - hggarciag@unal.edu.co
# + Jose Manuel Molina Vásquez  - josemoloinav@unal.edu.co
# + Juan Jose Alzate Rojas - jalzatero@unal.edu.co
# + Fabian Andres Chiran Guevara - fchirang@unal.edu.co
#
# Universidad Nacional de Colombia
#
#

from tkinter import *
import random
import sys
import os 
from collections import deque

# Serpiente

class Serpiente:
    instances = []

    def __init__(self):
        self.body_size = 3
        self.posicion = deque() # Posicion de cada uno de las partes de la serpiente Cabeza + Cuerpo [[x1,y1],[x2,y2],[x3,y3],...]
        self.squares = deque() # Posicion de cada uno de las partes de la serpiente Cabeza + Cuerpo EN EL CANVAS, es decir
                             #   de manera grafíca [[x1,y1],[x2,y2],[x3,y3],...]

        Serpiente.instances.append(self)

        for i in range(self.body_size):
            self.posicion.append([150, 150 + i * 25])

        self.head = self.posicion[0]

        for i, (x, y) in enumerate(self.posicion):
            if i == 0:
                square = cv.create_rectangle(
                    x, y, x + 25, y + 25, fill="#808080", tag="snake_head"
                )
            else:
                square = cv.create_rectangle(
                    x, y, x + 25, y + 25, fill="#bfbfbf", tag="snake"
                )
            self.squares.append(square)


# Movimiento Serpiente
def movimiento(nuevaDiereccion):
    
    global direccion
    
    if nuevaDiereccion == 'up':
        if direccion != 'down':
            direccion = nuevaDiereccion
    elif nuevaDiereccion == 'down':
        if direccion != 'up':
            direccion = nuevaDiereccion
    elif nuevaDiereccion == 'right':
        if direccion != 'left':
            direccion = nuevaDiereccion
    elif nuevaDiereccion == 'left':
        if direccion != 'right':
            direccion = nuevaDiereccion

# Manzana
class Manzana:
    
    instances = deque()
    
    def __init__(self):
        if Turno.turno == 0:
            cordxmanzana = 225
            cordymanzana = 75
        else:
            while True:
                cordxmanzana = random.randint(0, (325 / 25) - 2) * 25
                cordymanzana = random.randint(0, (325 / 25) - 2) * 25
                apple_position = [cordxmanzana, cordymanzana]
                snake_positions = [pos for pos in Serpiente.instances[0].posicion]
                snake_future_positions = [snake_positions[0]]  # Posicion actual serpiente
                # Posiciones futuras de la serpiente basadas en la actual
                x, y = snake_positions[0]
                if direccion == "up":
                    y -= 25
                elif direccion == "down":
                    y += 25
                elif direccion == "left":
                    x -= 25
                elif direccion == "right":
                    x += 25
                snake_future_positions.append([x, y])
                
                # Verificar que la posicion de la manzana no es ni la actual ni una futura de la serpiente
                is_safe = True
                for pos in snake_positions:
                    if apple_position == pos:
                        is_safe = False
                        break
                for pos in snake_future_positions:
                    if apple_position == pos:
                        is_safe = False
                        break
                if is_safe:
                    break
        self.cords = [cordxmanzana, cordymanzana]
        self.apple_instance = cv.create_rectangle(cordxmanzana, cordymanzana, cordxmanzana + 25, cordymanzana + 25, fill="#000000", tag="manzana")
        Manzana.instances.append(self)
        
    def remove(self):
        cv.delete(self.apple_instance)
    

class Turno:
    turno = 0
    movimientos = -1
    aparicion = 0
    manzana = 0

def siguienteTurno(snake, food):
    global score

    if Turno.turno > 0:
        x, y = snake.posicion[0]

        if direccion == "up":
            y -= 25
            if Turno.aparicion != 0:
                Turno.movimientos += 1
        elif direccion == "down":
            y += 25
            if Turno.aparicion != 0:
                Turno.movimientos += 1
        elif direccion == "left":
            x -= 25
            if Turno.aparicion != 0:
                Turno.movimientos += 1
        elif direccion == "right":
            x += 25
            if Turno.aparicion != 0:
                Turno.movimientos += 1
                
        if Turno.movimientos == Turno.aparicion and Turno.manzana == 0:
                food = Manzana()
                Turno.movimientos = 0
                Turno.aparicion = 0
                Turno.manzana = 1
        
        snake.posicion.appendleft([x, y])
        square = cv.create_rectangle(x, y, x + 25, y + 25, fill="#808080")
        snake.squares.appendleft(square)
        cv.delete(snake.squares[1])
        snake.squares[1] = cv.create_rectangle(
            snake.posicion[1][0], snake.posicion[1][1],
            snake.posicion[1][0] + 25, snake.posicion[1][1] + 25, fill="#bfbfbf")
        
        # La serpiente se come una manzana 
        if x == food.cords[0] and y == food.cords[1]:
            global score
            score += 1
            cantidad4.config(text="{}".format(score))
            if food:
                food.remove()
            Turno.aparicion = random.randint(1, 10)
            Turno.manzana = 0
                
            snake.body_size += 1
            if len(snake.posicion) < snake.body_size:
                snake.posicion.append([x, y])
        else: # Actualización de las partes del cuerpo de la serpiente cuando se mueve
            snake.posicion.pop()
            cv.delete(snake.squares.pop())  
                
    if Colision(snake):
        game_over()
    else:
        Turno.turno = 1
        interfaz.after(100, siguienteTurno, snake, food)
        
            
food_instance = None
           
#Muerte serpiente         
def Colision(snake):
    if not snake:
        return False

    x, y = snake.posicion[0]

    if x < 0 or x >= 325:
        return True
    elif y < 0 or y >= 325:
        return True

    for i in range(1, len(snake.posicion)):
        body_part = snake.posicion[i]
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

#Terminar juego
def game_over(): 
    cv.delete(ALL)
    cv.create_text(163, 150, font=('consolas', 30), text="Has chocado\n\nGame over", fill="red", tag="gameover", justify = ['center'])

# Iniciar programa
def iniciar_programa():
    if len(Serpiente.instances) == 0 and len(Manzana.instances) == 0:
        message = cv.create_text(163, 285, font=('consolas', 15), text="Use W, A, S o D para moverse\nCada 1 a 10 movimientos\n aparecerá una manzana", fill="red", justify=['center'])
        # Tiempo de espera para borrado del mensaje (milisegundos)
        interfaz.after(4000, lambda: cv.delete(message))
        snake = Serpiente()
        food = Manzana()
        siguienteTurno(snake, food)

#Reiniciar programa
def reiniciar_programa():
    python = sys.executable
    os.execl(python, python, * sys.argv)

#Interfaz

interfaz = Tk()
interfaz.title('Snake')
interfaz.geometry('325x350')
interfaz.config(bg='white')
interfaz.resizable(width=False, height=False)

score = 0
direccion = 'up'

# se crea el frame para los botones, y la info del juego
f1 = Frame(interfaz, width=325, height=14, bg='grey')
f1.grid(column=0, row=0)

# se crea el frame para el juego
f2 = Frame(interfaz, width=325, height=350, bg='black')
f2.grid(column=0, row=1)

# se crea el Canvas (superficie de dibujo) y se pone en el frame 2
cv = Canvas(f2, bg="#ffffff", width=325, height=350)
cv.pack()

# se crean los rectangulos en el canvas
for i in range(0,325,25):
    for j in range(0,350,25):
        cv.create_rectangle(i,j,i+25, j+25, fill='white')

# se crea el boton de iniciar, y se pone en el frame f1
button1 = Button(f1, text='Iniciar', bg='orange', command = iniciar_programa, width=5, height=1)
button1.grid(row=0, column=0, padx=7)

# Botón de reinicio

button3 = Button(f1, text="Reset", command=reiniciar_programa, width=5, height=1)
button3.grid(row=0, column=2, padx=7)

# se crea el boton de salir, y se pone en el frame f1
button4 = Button(f1, text='Salir', bg='blue', command = interfaz.destroy, width=5, height=1)
button4.grid(row=0, column=3, padx=7)

# los siguientes 3 Labels, son para indicar la cantidad de manzanas comidas
# se crea el Label al lado del contador de manzanas comidas, y se pone en el frame f1
cantidad1 =Label(f1, text='Score : ', bg='grey', fg = 'black', font=('Arial',12, 'bold'))
cantidad1.grid(row=0, column=4, padx=0)

cantidad4 =Label(f1, text="{}".format(score), bg='grey', fg = 'black', font=('Arial',12, 'bold'))
cantidad4.grid(row=0, column=7, padx=0)

interfaz.update()

interfaz_width = interfaz.winfo_width()
interfaz_height = interfaz.winfo_height()
screen_width = interfaz.winfo_screenwidth()
screen_height = interfaz.winfo_screenheight()

x = int((screen_width/2) - (interfaz_width/2))
y = int((screen_height/2) - (interfaz_height/2))

interfaz.geometry(f"{interfaz_width}x{interfaz_height}+{x}+{y}")

# Control de comandos - verificación de ingreso de eventos por movimiento
def handle_key(event):
    key = event.keysym
    if key == 'w':
        movimiento('up')
    elif key == 'a':
        movimiento('left')
    elif key == 's':
        movimiento('down')
    elif key == 'd':
        movimiento('right')
    else:
        error_message = cv.create_text(163, 275, font=('consolas', 15), text="Comando equivocado\nUse W, A, S o D para moverse", fill="red", justify=['center'])
        # Tiempo de espera para borrado del mensaje (milisegundos)
        interfaz.after(2000, lambda: cv.delete(error_message))

interfaz.bind('<Key>', handle_key)


interfaz.mainloop()
