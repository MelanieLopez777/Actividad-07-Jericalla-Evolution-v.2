from tkinter import *
from tkinter import ttk
from tkinter import filedialog

def abrir_archivo():
    global content
    # Abrir el cuadro de diálogo para seleccionar un archivo
    file_path = filedialog.askopenfilename(title="Abrir archivo", filetypes=[("Archivo ensamblador", "*.asm")])
    # Si se selecciona un archivo (no se cancela)
    if file_path:
        with open(file_path, 'r') as file:
            # Leer el contenido del archivo
            content = file.read()
            
            text_contenido.delete('1.0', END)
            text_contenido.insert(END, content)

def decodificar():
    diccionario_opcode = {
        "and": 0,
        "or": 1,
        "add": 2,
        "sub": 3,
        "slt": 4,
        "nor": 5,
        "sw": 6,
        "lw": 7
    }

    lineas = content.split("\n")
    instrucciones_decodificadas = []  # Lista para almacenar las instrucciones decodificadas

    for i in lineas:
        palabras = i.split('\t')
        if len(palabras) > 0:
            fila_decodificada = str(format(diccionario_opcode.get(palabras[0], -1), '04b'))  # Obtener el código de la operación
            if palabras[0] == "sw":
                fila_decodificada += "zzzzz"
                fila_decodificada += format(int(palabras[1][1:]), '05b')  # Convierte el valor a binario
                fila_decodificada += format(int(palabras[2][1:]), '05b')  # Convierte el valor a binario
            elif palabras[0] == "lw":
                fila_decodificada += "zzzzz"
                fila_decodificada += format(int(palabras[1][1:]), '05b')  # Convierte el valor a binario
                fila_decodificada += "zzzzz"
            else:
                fila_decodificada += format(int(palabras[1][1:]), '05b')  # Convierte el valor a binario
                fila_decodificada += format(int(palabras[2][1:]), '05b')  # Convierte el valor a binario
                fila_decodificada += format(int(palabras[3][1:]), '05b')  # Convierte el valor a binario

            instrucciones_decodificadas.append(fila_decodificada)  # Agregar la instrucción a la lista

    with open('../Proyecto/instrucciones.txt', 'w') as archivo:
        for item in instrucciones_decodificadas:
            archivo.write(item + "\n")

root = Tk()
root.geometry("800x370")

# Crear un Frame para organizar los elementos
frame_superior = Frame(root)
frame_superior.pack(pady=20)

style = ttk.Style()
style.theme_use("clam")

# Aquí pones tus estilos :]
#style.configure("Estilo_text_contenido", width=80, height=10, wrap=NONE, padx=20, pady=20)


# Etiqueta y botón uno al lado del otro
label = Label(frame_superior, text="Elige la ruta del archivo .asm")
label.grid(row=0, column=0, padx=10)

boton_abrir = Button(frame_superior, text="abrir", command=abrir_archivo)
boton_abrir.grid(row=0, column=1, padx=10)

# Crear el cuadro de texto con scroll
frame_texto = Frame(root)
frame_texto.pack(pady=10)

text_contenido = Text(frame_texto, width=80, height=10, wrap=NONE, padx=20, pady=20)
text_contenido.pack(side=LEFT, fill=BOTH, expand=True)

scroll_y = Scrollbar(frame_texto, orient=VERTICAL, command=text_contenido.yview)
scroll_y.pack(side=RIGHT, fill=Y)

text_contenido.config(yscrollcommand=scroll_y.set)

# Botón adicional debajo del cuadro de texto
boton_decodificar = Button(root, text="Decodificar", command=decodificar)
boton_decodificar.pack(pady=10)

root.mainloop()
