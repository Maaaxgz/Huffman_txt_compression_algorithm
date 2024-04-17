#LIBRERIAS
import tkinter as tk
from tkinter import filedialog, ttk

#ABRE EL EXPLORADOR DE ARCHIVOS
def open_file_dialog():
	global file_path, label, show_file_button, show_result_button
	file_path = filedialog.askopenfilename()
	print("Archivo seleccionado:", file_path)
	#obtiene la extension separando el .txt
	extension = file_path.split(".")
	#[-1] obtiene el ultimo elemento de la lista
	print("Extensión:", extension[-1])
	#si el archivo no es un .txt
	if extension[-1] != "txt":
		label.config(text = "El archivo seleccionado no es un .txt")
		show_file_button.config(state='disabled')
		show_result_button.config(state='disabled')
	else:
		label.config(text = "Archivo txt seleccionado correctamente")
		show_file_button.config(state='normal')
		show_result_button.config(state='normal')

#ABRE UNA NUEVA VENTANA
def show_file_data():
	global file_path, main_window, lista_caracteres
	texto_conteo = ""
	#configuracion de la ventana
	new_window = tk.Toplevel(main_window)
	new_window.geometry("700x650+800+100")
	new_window.title("Ver archivo 💥")
	new_window['background'] = '#003C43'
	new_window.resizable(False, False)
	label = tk.Label(new_window, text = "Mostrando el contenido del archivo .txt", fg="white", bg='#003C43', font=("Arial", 12))
	label.place(relx=0.5, rely=0.07, anchor = 'center')
	label2 = tk.Label(new_window, text = "Mostrando el conteo de caracteres", fg="white", bg='#003C43', font=("Arial", 12))
	label2.place(relx=0.5, rely=0.55, anchor = 'center')

	#lee el archivo
	with open(file_path, "r") as file:
		texto_txt = file.read()

	#crea el widget del texto del archivo
	text = tk.Text(new_window, width = 300, height = 300, bg = '#EEEEEE', font = ("Courier", 10))
	text.place(x = 50, y = 80, width = 600, height = 200)
	#inserta el texto en el widget
	text.insert('end', str(texto_txt))
	text.configure(state='disabled')
 
	#crea el widget de texto para el conteo de caracteres
	text2 = tk.Text(new_window, width = 300, height = 300, wrap = 'none', bg = '#EEEEEE', font = ("Courier", 10))
	text2.place(x = 50, y = 380, width = 600, height = 200)
 
	#itera sobre el diccionario
	for clave, valor in lista_caracteres.items():
		if clave == "\n":
			clave = "/n"
			texto_conteo += "  Caracter: " + clave + "   |    Repeticiones: " + str(valor) + "\n"
		else:
			#agrega la clave y el valor a la cadena como renglon
			texto_conteo += "  Caracter: " + clave + "    |    Repeticiones: " + str(valor) + "\n"
	text2.insert('end', texto_conteo)
	text2.configure(state='disabled')

	#crea un scrollbar y lo asocia con el widget de texto
	scrollbar = tk.Scrollbar(new_window)
	scrollbar.place(x = 650, y = 80, height = 200)
	scrollbar.config(command = text.yview)
	text.config(yscrollcommand = scrollbar.set)

	#crea un scrollbar y lo asocia con el texto de conteo
	scrollbar2 = tk.Scrollbar(new_window)
	scrollbar2.place(x = 650, y = 380, height = 200)
	scrollbar2.config(command = text2.yview)
	text2.config(yscrollcommand = scrollbar2.set)
 
#ABRE UNA NUEVA VENTANA
def show_result_data():
	#configuracion de la ventana
	result_window = tk.Toplevel(main_window)
	result_window.geometry("700x600+750+100")
	result_window.title("Comprimir archivo 💥")
	result_window['background'] = '#003C43'
	result_window.resizable(False, False)
	label = tk.Label(result_window, text = "Mostrando el archivo comprimido", fg="white", bg='#003C43', font=("Arial", 12))
	label.place(relx=0.5, rely=0.07, anchor = 'center')

	#cree los widgets de texto
	text = tk.Text(result_window, width = 300, height = 300, bg = '#EEEEEE', font = ("Courier", 10))
	text.place(x = 50, y = 60, width = 600, height = 150)
	text.configure(state='disabled')

	text2 = tk.Text(result_window, width=300, height=300, bg='#EEEEEE', font=("Courier", 10), wrap='word')
	text2.place(x=50, y=220, width=600, height=350)
	text2.configure(state='disabled')

#CREA LA VENTANA PRINCIPAL
def show_main_window():
	global label, show_file_button, show_result_button, main_window
	#configura la ventana
	main_window = tk.Tk()
	main_window.geometry("500x250+200+100")
	main_window.title("Compresor de archivos de texto ❤")
	main_window['background'] = '#003C43'
	main_window.resizable(False, False)

	#crear el texto de la ventana principal
	label = tk.Label(main_window, text="Pulsa el botón para seleccionar un archivo .txt", fg='#E3FEF7', bg='#003C43', font=("Arial", 12))
	label.place(relx=0.5, rely=0.15, anchor='center')

	#crear el botón para escoger un archivo
	button = tk.Button(main_window, text="Seleccionar archivo", command=open_file_dialog, fg='#003C43', bg='#E3FEF7', font=("Arial", 11))
	button.place(relx=0.5, rely=0.35, anchor='center')

	#crear el botón para mostrar el texto del archivo
	show_file_button = tk.Button(main_window, text="Ver datos del archivo", command=show_file_data, state='disabled', fg='#003C43', bg='#E3FEF7', font=("Arial", 11))
	show_file_button.place(relx=0.5, rely=0.55, anchor='center')

	#crear el botón para comprimir el archivo
	show_result_button = tk.Button(main_window, text="Comprimir archivo", command=show_result_data, state='disabled', fg='#003C43', bg='#E3FEF7', font=("Arial", 11))
	show_result_button.place(relx=0.5, rely=0.75, anchor='center')

	#inicia el bucle de la ventana
	main_window.mainloop()

#INICIA EL PROGRAMA
lista_caracteres = {}
ruta = "C:/Users/JoseM/OneDrive/Documentos/CUCEI/Quinto Semestre/Analisis de Algoritmos/mondongo.txt"
with open(ruta, "r") as file:
	#lee el archivo txt
	file_contents = file.read()

#iterara sobre cada caracter del archivo
for char in file_contents:
	#si el caracter no es una clave en el diccionario
	if char not in lista_caracteres:
		#agrega el caracter al diccionario con un valor de 1
		lista_caracteres[char] = 1
	#si ya esta en el diccionario
	else:
		#aumenta el valor de la clave del caracter
		lista_caracteres[char] += 1

show_main_window()
#variables globales
file_path = ""
label, show_file_button, show_result_button, main_window = None, None, None, None
