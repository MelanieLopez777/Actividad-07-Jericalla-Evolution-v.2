from tkinter import *
from tkinter import ttk
from tkinter import filedialog

def abrir_archivo():
    # Abrir el cuadro de diálogo para seleccionar un archivo
    file_path = filedialog.askopenfilename(title="Abrir archivo", filetypes=[("Archivo ensamblador", "*.asm")])
    # Si se selecciona un archivo (no se cancela)
    if file_path:
        with open(file_path, 'r') as file:
            # Leer el contenido del archivo
            content = file.read()
            content_var.set(content)

root = Tk()

# Crea un estilo
style = ttk.Style()

# Establecer el color de fondo y el color del texto para los botones
style.configure("TButton", background="pink", foreground="blue")
style.configure("Label", width=50, height=10)

frm = ttk.Frame(root, padding=10)
frm.grid()

# Usar el estilo configurado para el botón
ttk.Label(frm, text="Elige la ruta del archivo .asm").grid(column=0, row=0)

# Crear el botón para abrir archivo
boton_abrir_archivo = ttk.Button(frm, text="Abrir", command=abrir_archivo, style="TButton")
boton_abrir_archivo.grid(column=1, row=0)

# Crear una variable StringVar() para almacenar el contenido
content_var = StringVar()

# Crear el Label que muestra el contenido del archivo
datos_archivo = ttk.Label(frm, textvariable=content_var, style="Label")
datos_archivo.grid(column=0, row=1, columnspan=2)

root.mainloop()
