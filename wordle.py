# Trabajo 1 Estructura de Datos
#
# Wordle Game
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

from collections import deque
import random
from tkinter import *
from tkinter import ttk
from collections import deque

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.word_count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.count = 0
        self.word_list = []

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.word_count += 1  # 
        node.is_end_of_word = True
        self.word_list.append(word)

    def search(self, word):
        node = self.root
        matched_characters = []
        for char in word:
            if char not in node.children:
                return False
            matched_characters.append(char)
            node = node.children[char]
            
        return "".join(matched_characters), node.is_end_of_word

    def retrieve_random_word(self, length):
        candidates = [word for word in self.word_list if len(word) == length]
        return random.choice(candidates)

def inputDificultad():
    while True:
        try:
            lenPalabra = int(input("Escoja la dificultad, ingrese un número entre 4 y 8 indicando el tamaño de la palabra: "))
            if 4 <= lenPalabra <= 8:
                break
            else:
                print("Error: Dificultad inválida. Por favor ingrese un número entre 4 y 8 indicando el tamaño de la palabra.")
        except ValueError:
            print("Entrada no válida. Por favor ingrese un número válido.")
    
    return lenPalabra

# Verificación palabras

def build_trie(word_list):
    root = TrieNode()
    for word in word_list:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    return root

def search_word(trie, word):
    node = trie
    for char in word:
        if char not in node.children:
            return False
        node = node.children[char]
    return node.is_end_of_word

def read_words_from_file(file_path):
    with open(file_path, 'r') as file:
        words = [line.strip() for line in file]
    return words

# Lemario versión lite (Esto debido a que se usan palabras de mas de 8 carácteres en el lmeario original que resultan redundantes en nuestro caso y hacen ineficiente el codigo per se)
def trie():
    Lemario = ['pipeline', 'beards', 'hapiness', 'dessert', 'maybe', 'puzzle', 'same', 'showroom', 'wafer', 'dracula', 'voor', 'noodle', 'reshape', 'stigma', 'dwellers', 'gripe', 'keyrings', 'dorothea', 'hecht', 'dubuque', 'widening', 'metro', 'crichton', 'wenn', 'pamphlet', 'aarhus', 'convoy', 'stone', 'fail', 'roommate', 'moro', 'paint', 'viacom', 'ebayer', 'glace', 'pension', 'bathtub', 'snot', 'vitesse', 'alonso', 'precio', 'balm', 'pointer', 'clarins', 'tendency', 'hematite', 'bromide', 'boat', 'sexually', 'aguirre', 'tarp', 'prevail', 'charles', 'comedy', 'nearing', 'freeport', 'faerie', 'silicate', 'confined', 'equinox', 'raitt', 'crud', 'bbci', 'estrogen', 'stewards', 'equate', 'fountain', 'dara', 'eugene', 'kessler', 'titleist', 'scherer', 'nutty', 'fairs', 'licences', 'osage', 'traders', 'args', 'jodie', 'samantha', 'siege', 'though', 'unable', 'lesbicas', 'upper', 'romero', 'martel', 'calvin', 'sumitomo', 'tube', 'brunson', 'monarchs', 'pedersen', 'stables', 'matte', 'couture', 'latino', 'novella', 'strat', 'ashburn', 'thirds', 'bakker', 'rotten', 'weaker', 'kylie', 'orkney', 'cheater', 'falmouth', 'gregorio', 'lampoon', 'collect', 'racer', 'faster', 'blick', 'prone', 'destroy', 'outbound', 'beet', 'shortage', 'hiphop', 'janice', 'approves', 'whats', 'neve', 'taboo', 'harms', 'closeups', 'ruger', 'cherie', 'mondo', 'fractals', 'burgers', 'sarasota', 'batten', 'colman', 'alpaca', 'owls', 'stamina', 'tower', 'textile', 'keele', 'pumpkins', 'come', 'robeson', 'testy', 'pols', 'equifax', 'contre', 'fdisk', 'lockout', 'failed', 'debadmin', 'oranges', 'picket', 'hooks', 'maryann', 'nieuwe', 'poisons', 'schrieb', 'cfnm', 'alienate', 'incoming', 'vila', 'pixma', 'reisen', 'stanford', 'carnal', 'inch', 'sara', 'alexia', 'cadence', 'wished', 'angebote', 'homage', 'capacity', 'torque', 'diflucan', 'spout', 'oyster', 'budget', 'llcs', 'driving', 'kruger', 'virgil', 'baton', 'motoring', 'leyland', 'mancha', 'wept', 'cousin', 'wartime', 'donut', 'lunatic', 'niagara', 'religion', 'heart', 'lola', 'loti', 'mildura', 'annals', 'barge', 'phases', 'debts', 'pippin', 'pollock', 'snails', 'chip', 'adjunct', 'dementia', 'elgin', 'bridger', 'consoles', 'ignored', 'hausa', 'arranges', 'worldcat', 'mowers', 'whenever', 'oddities', 'required', 'writing', 'executed', 'falcons', 'favors', 'caliber', 'hernando', 'older', 'shandong', 'endian', 'knopf', 'clever', 'iogear', 'pyle', 'ruthless', 'reign', 'rino', 'pupil', 'double', 'infosec', 'assessed', 'marketed', 'shakers', 'optimise', 'sesso', 'taro', 'ambien', 'foils', 'withdrew', 'ignite', 'pale', 'magnet', 'deering', 'alltel', 'torsion', 'plas', 'modeling', 'high', 'cosco', 'casts', 'token', 'scenic', 'rancho', 'forde', 'galore', 'allure', 'beverly', 'wooded', 'stabbing', 'klamath', 'ajmer', 'huts', 'trackers', 'rundown', 'mandated', 'junebug', 'surveys', 'sociales', 'stinky', 'sues', 'fichier', 'shiraz', 'cast', 'hansard', 'alex', 'scope', 'blinked', 'searle', 'westward', 'panic', 'soyo', 'freakin', 'built', 'reusing', 'harris', 'warmest', 'meters', 'lsat', 'memory', 'chord', 'meanings', 'serenade', 'hurley', 'mammals', 'mika', 'isola', 'devotee', 'zambezi', 'frosting', 'praises', 'myself', 'specific', 'brigade', 'gradient', 'diary', 'original', 'myer', 'inquired', 'forrest', 'pantech', 'laura', 'came', 'watcher', 'philip', 'canning', 'dscp', 'nothing', 'clemson', 'parallel', 'chard', 'partie', 'hyundai', 'pies', 'picked', 'repaired', 'tucows', 'milk', 'xpdf', 'rogues', 'fleece', 'agri', 'draw', 'doped', 'passat', 'defines', 'howling', 'slimming', 'dealer', 'talkin', 'imposing', 'techweb', 'anode', 'paragon', 'hygiene', 'watches', 'postmark', 'chatter', 'minidisc', 'michaels', 'barlow', 'jolt', 'valance', 'roselle', 'gaining', 'yorke', 'rotate', 'wang', 'lethal', 'ordering', 'toggle', 'deluxe', 'parting', 'lott', 'autonomy', 'ladybird', 'skimage', 'dominion', 'stingy', 'towns', 'rage', 'trixie', 'helios', 'militia', 'mainpage', 'oxygen', 'stis', 'rowland', 'faction', 'mifflin', 'cushion', 'vesta', 'variable', 'henning', 'louise', 'yogurt', 'howtos', 'yashica', 'bulk', 'torpedo', 'hosting', 'mise', 'bouts', 'rusk', 'appease', 'inode', 'goodness', 'kardon', 'mohawk', 'catching', 'jossey', 'musings', 'lois', 'skating', 'reims', 'koji', 'fast', 'puma', 'quiver', 'absence', 'equip', 'lebron', 'rmdir', 'hodge', 'realtor', 'winer', 'bancroft', 'rooter', 'bought', 'sophos', 'bistro', 'anza', 'simcoe', 'tactic', 'tucson', 'citroen', 'kazan', 'centre', 'meetups', 'duracell', 'sprache', 'camargo', 'frazier', 'pkgsrc', 'infill', 'joining', 'meine', 'trinket', 'boys', 'palm', 'cages', 'handling', 'junkyard', 'inner', 'erode', 'plow', 'itat', 'lawless', 'vicodin', 'pebble', 'info', 'rubles', 'looping', 'mine', 'sharks', 'dishes', 'jewelry', 'connects', 'wayne', 'tracking', 'mint', 'elders', 'berne', 'pour', 'heyday', 'bally', 'sucking', 'longing', 'awake', 'grantor', 'custom', 'martyr', 'baku', 'stade', 'balloon', 'hardwood', 'corps', 'parkside', 'astor', 'gbps', 'helsing', 'navi', 'warlock', 'shrunk', 'make', 'bossa', 'abusing', 'pleading', 'sheriffs', 'zyban', 'dumped', 'sheikh']
    trie = Trie()
    for palabra in Lemario:
        trie.insert(palabra)
    return trie


def generadorPalabra(trie, dificultad):
    palabraDelDia = trie.retrieve_random_word(dificultad)
    return palabraDelDia

def inputUsuario(trie):

    palabraDia = generadorPalabra(trie)
    user_input = input("Ingrese una palabra, recuerde que son palabras en inglés: ")
    matched_characters, is_end_of_word = trie.search(user_input)
    
    if is_end_of_word and matched_characters == palabraDia:
        print("Correcto! Ha ingresado la palabra del día correcta")
    else:
        print("Incorrecto! Has agotado tus intentos. Hasta la próxima!")

a = generadorPalabra(trie(), inputDificultad())
long = len(a)
ganados = 0
intentos= 0
ganador= False

# Validación palabra en Diccionario/Lemario de inglés
file_path = 'words.txt' 
word_list = read_words_from_file(file_path)
trie_root = build_trie(word_list)

def crear_interfaz():
    global interfaz,f1

    f1 = Frame(interfaz, width=800, height=800, bg='grey', pady=100)
    f1.pack(side="top")

    boton_iniciar_juego = Button(f1, text='Iniciar Juego de Wordle', font=("Arial", 30),
                             bg='yellow', command=iniciarjuego, justify="center", width=18, height=4, padx=82, pady=100)
    boton_iniciar_juego.grid(row=0, column=0, padx=7)

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

    def validate_input(char, current_text):
        return char.isalpha() or char == ""

    vcmd = (interfaz.register(validate_input), '%S', '%P')

    entry = Entry(input_frame, width=10, justify="left", font=["Arial", 30], validate="key", validatecommand=vcmd)
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
        global z,ganados,intentos  # Declare z as a global variable

        intento = entry.get()
        
        search_word_result = search_word(trie_root, intento)
        if search_word_result and len(intento) == long:
            colores = asignar_colores_palabra(intento)
            
            longitudesy = [100, 100, 90, 80, 70]
            longitudes = [130, 104, 87, 74, 65]
            for i in range(long):
                cv.create_text(longitudesy[long - 4] + i * longitudes[long - 4], z, text=intento[i], 
                            font=("Arial", 55), fill=colores[i])
            z += 100
            intentos+=1
            print("El intento fue el numero: ", intentos)
            entry.delete(0, END)
        else:
            print("Palabra no encontrada o palabra inválida. Por favor, ingrese una palabra válida.")
        
        # Verificar si el usuario ha adivinado la palabra
        if intento == a:
            ganador = True
            informar_ganador()
            ganados+=1
        elif intentos == 6 :
            informar_perdedor()
            

    ttk.Button(input_frame, text="Ingresar intento", width=20, command=ingresar_intento).pack(side='left', pady=0, padx=10)

def informar_ganador():
    global interfaz,intentos

    # Mensaje que se mostrará en la interfaz
    mensaje_ganador = "¡Felicidades! Has adivinado la palabra."

    # Eliminar los widgets existentes en la interfaz
    for widget in interfaz.winfo_children():
        widget.destroy()

    # Crear un nuevo marco para mostrar el mensaje y el botón
    marco_ganador = Frame(interfaz, bg='grey')
    marco_ganador.pack(expand=True)

    # Etiqueta para mostrar el mensaje de ganador
    etiqueta_ganador = Label(marco_ganador, text=mensaje_ganador, font=("Arial", 24), bg='grey', pady=20)
    etiqueta_ganador.pack()

    # Botón para reiniciar el juego
    boton_reiniciar = Button(marco_ganador, text='Reiniciar', font=("Arial", 20), command=reiniciar_juego)
    boton_reiniciar.pack(pady=20)

    ganador= True 
    intentos=0

def informar_perdedor():
    global interfaz

    # Mensaje que se mostrará en la interfaz
    mensaje_perdedor = ("Has perdido, la palabra era: ",a)

    # Eliminar los widgets existentes en la interfaz
    for widget in interfaz.winfo_children():
        widget.destroy()

    # Crear un nuevo marco para mostrar el mensaje y el botón
    marco_perdedor = Frame(interfaz, bg='grey')
    marco_perdedor.pack(expand=True)

    # Etiqueta para mostrar el mensaje de perdedor
    etiqueta_perdedor = Label(marco_perdedor, text=mensaje_perdedor, font=("Arial", 24), bg='grey', pady=20)
    etiqueta_perdedor.pack()

    # Botón para reiniciar el juego
    boton_reiniciar = Button(marco_perdedor, text='Reiniciar', font=("Arial", 20), command=reiniciar_juego)
    boton_reiniciar.pack(pady=20)


def reiniciar_juego():
    global interfaz, ganador,intentos

    # Destruir widgets adicionales
    for widget in interfaz.winfo_children():
        widget.destroy()

    # Volver al inicio del código y crear la interfaz inicial
    crear_interfaz()

    ganador = False
    print(ganados)
    intentos=0
    

interfaz = Tk()
interfaz.title('Wordle')
interfaz.geometry('600x690')
interfaz.config(bg='grey')
interfaz.resizable(width=False, height=False)

crear_interfaz()



interfaz.update()
interfaz.mainloop()

