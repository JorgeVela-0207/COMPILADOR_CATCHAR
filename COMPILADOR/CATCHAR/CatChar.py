import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import subprocess
from tkinter import filedialog
from AnalizadorSemantico import lexer, parser

def abrir_ventana_principal():
    Splash.destroy()

    # Aquí iría el código para abrir la ventana principal del programa
    # Creamos la ventana principal
    ventana_principal = tk.Tk()

    # Configuramos el tamaño y la posición de la ventana
    ventana_principal.geometry("900x600")
    ventana_principal.resizable(0,0)
    ancho_pantalla = ventana_principal.winfo_screenwidth()
    alto_pantalla = ventana_principal.winfo_screenheight()
    x_ventana = int((ancho_pantalla/2) - (900/2))
    y_ventana = int((alto_pantalla/2) - (600/2))
    ventana_principal.geometry(f"900x600+{x_ventana}+{y_ventana}")

    # Configuramos el título y el ícono de la ventana
    ventana_principal.title("CatChar")
    ventana_principal.iconbitmap("C:/Users/Jorge L. Vela/Desktop/COMPILADOR_CASI_LISTO/IDE/GATO.ico")

    # Cargar la imagen de fondo
    image = Image.open("C:/Users/Jorge L. Vela/Desktop/COMPILADOR_CASI_LISTO/IDE/gato_principal.jpg")

    # Obtener el ancho y alto de la ventana
    window_width = ventana_principal.winfo_width()
    window_height = ventana_principal.winfo_height()

    # Redimensionar la imagen
    resized_image = image.resize((window_width, window_height))

    # Convertir la imagen redimensionada en un objeto de imagen de Tkinter
    tk_resized_image = ImageTk.PhotoImage(resized_image)

    # Crear el widget Label para la imagen redimensionada
    label = Label(ventana_principal, image=tk_resized_image)

    # Configurar el widget Label para que llene toda la ventana
    label.place(x=0, y=0, relwidth=1, relheight=1)

    # Aquí iría el código para agregar los elementos gráficos de la ventana principal
    # ..........................................................................................................
# Crea una etiqueta para la caja de texto
    label = tk.Label(ventana_principal, text="Escribe tu código:")
    label.place(x=10,y=20)

    # Crea una caja de texto para escribir el código
    text_box = tk.Text(ventana_principal, height=30, width=50)
    text_box.place(x=10,y=40)
# Crea una función para compilar el código
    def compile_code():
    # Obtiene el código escrito en la caja de texto
        code = text_box.get("1.0", "end-1c")
    # Realiza el análisis sintáctico sin utilizar el lexer explícitamente
        try:
        # Aquí asumimos que parser.parse devuelve el resultado o lanza una excepción
            resultado = parser.parse(code)
        # Convierte el resultado a un string, si es necesario
            resultado_str = str(resultado)
            output_box.delete("1.0", "end")
            output_box.insert("1.0", resultado_str)
        except Exception as e:
            output_box.delete("1.0", "end")
            output_box.insert("1.0", f"Error en la compilación: {e}")




    # Crea un botón para compilar el código
    compile_button = tk.Button(ventana_principal, text="Compilar", command=compile_code)
    compile_button.place(x=630,y=390)

    # Crea una etiqueta para la consola de salida
    output_label = tk.Label(ventana_principal, text="Resultado:")
    output_label.place(x=450,y=20)

    # Crea una caja de texto para mostrar el resultado
    output_box = tk.Text(ventana_principal, height=20, width=50)
    output_box.place(x=450,y=40)

    # Función para crear un nuevo archivo
    def new_file():
        text_box.delete("1.0", "end")

    # Función para abrir un archivo
    def open_file():
        file_path = filedialog.askopenfilename(defaultextension=".miau")
        with open(file_path, "r") as f:
            text = f.read()
        text_box.delete("1.0", "end")
        text_box.insert("1.0", text)

    # Función para guardar un archivo
    def save_file():
        file_path = filedialog.asksaveasfilename(defaultextension=".miau")
        with open(file_path, "w") as f:
            text = text_box.get("1.0", "end-1c")
            f.write(text)

    # Función para salir del programa
    def exit_program():
        ventana_principal.quit()

    # Crea un menú de archivo
    menu_bar = tk.Menu(ventana_principal)
    ventana_principal.config(menu=menu_bar)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Archivo", menu=file_menu)
    file_menu.add_command(label="Nuevo", command=new_file)
    file_menu.add_command(label="Abrir", command=open_file)
    file_menu.add_command(label="Guardar", command=save_file)
    file_menu.add_separator()
    file_menu.add_command(label="Salir", command=exit_program)

    # Crea un menú de edición
    edit_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Editar", menu=edit_menu)
    edit_menu.add_command(label="Cortar", accelerator="Ctrl+X", command=lambda: text_box.event_generate("<<Cut>>"))
    edit_menu.add_command(label="Copiar", accelerator="Ctrl+C", command=lambda: text_box.event_generate("<<Copy>>"))
    edit_menu.add_command(label="Pegar", accelerator="Ctrl+V", command=lambda: text_box.event_generate("<<Paste>>"))
    edit_menu.add_separator()
    edit_menu.add_command(label="Deshacer", accelerator="Ctrl+Z", command=lambda: text_box.event_generate("<<Undo>>"))

    # Agrega atajos de teclado para las opciones de edición
    ventana_principal.bind("<Control-x>", lambda event: text_box.event_generate("<<Cut>>"))
    ventana_principal.bind("<Control-c>", lambda event: text_box.event_generate("<<Copy>>"))
    ventana_principal.bind("<Control-v>", lambda event: text_box.event_generate("<<Paste>>"))
    ventana_principal.bind("<Control-z>", lambda event: text_box.event_generate("<<Undo>>"))

    # Crea un menú de ayuda
    # Función para mostrar la ayuda
    def show_help():
        message = "Bienvenido al CatChar\n\n"
        message += "Para compilar el código, escribe el código en la caja de texto y presiona el botón \"Compilar\".\n\n"
        message += "Para crear un nuevo archivo, selecciona \"Archivo\" y luego \"Nuevo\".\n\n"
        message += "Para abrir un archivo existente, selecciona \"Archivo\" y luego \"Abrir\".\n\n"
        message += "Para guardar el archivo actual, selecciona \"Archivo\" y luego \"Guardar\".\n\n"
        message += "Para salir del programa, selecciona \"Archivo\" y luego \"Salir\".\n\n"
        message += "Para copiar, cortar o pegar texto, selecciona \"Editar\" y luego la opción deseada.\n\n"
        message += "Gracias por usar el C."
        tk.messagebox.showinfo("Ayuda", message)

    # Agrega la opción de ayuda al menú de ayuda
    menu_bar.add_command(label="Ayuda", command=show_help)


    
    # ..........................................................................................................
#FIN DE VENTANA PRINCIPAL
    ventana_principal.mainloop()
    
#INICIO DE VENTANA SPLASH

# Creamos la ventana splash
Splash = tk.Tk()
Splash.title("CatChar")

# Configuramos el tamaño y la posición de la ventana
Splash.geometry("300x200")
Splash.resizable(0,0)
ancho_pantalla = Splash.winfo_screenwidth()
alto_pantalla = Splash.winfo_screenheight()
x_ventana = int((ancho_pantalla/2) - (300/2))
y_ventana = int((alto_pantalla/2) - (200/2))
Splash.geometry(f"300x200+{x_ventana}+{y_ventana}")

# Cargar la imagen de fondo
image = Image.open("C:/Users/Jorge L. Vela/Desktop/COMPILADOR_CASI_LISTO/IDE/gato_splash.jpg")

# Obtener el ancho y alto de la ventana
window_width = Splash.winfo_width()
window_height = Splash.winfo_height()

# Convertir la imagen a un objeto de imagen de Tkinter
tk_image = ImageTk.PhotoImage(image)

# Crear el widget Label para la imagen
label = Label(Splash, image=tk_image)

# Agregar el widget Label a la ventana
label.pack()

# Creamos una barra de progreso
barra_progreso = ttk.Progressbar(Splash, orient="horizontal", length=280, mode="determinate")
barra_progreso.place(x=10, y=141)

# Etiqueta que muestra el texto de carga
texto_carga = tk.Label(Splash, text="Cargando...")
texto_carga.place(x=100, y=165)

# Simulamos la carga de la aplicación durante 5 segundos
for i in range(101):
    barra_progreso["value"] = i
    Splash.update()
    if i == 100:
       break
    if i%10 == 0:
       texto_carga.config(text=f"Cargando... {i}%")
       Splash.after(500)

#FIN DE VENTANA SPLASH

# (LLAMAMOS A LA FUNCION) Cerramos la ventana splash y abrimos la ventana principal
abrir_ventana_principal()