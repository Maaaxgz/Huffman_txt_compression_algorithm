# Huffman text compression algorithm
**Algoritmo de Huffman para la compresion de archivos**
## Descripcion
El siguiente programa es una interfaz grafica para un programa de compresion de archivos. En este se puede abrir el explorador para escoger un archivo, asi como validar la extension .txt del mismo. Permite visualizar el texto contenido en el archivo, junto con un conteo de la cantidad y tipo de caracteres dentro de este. Tambien hay un apartado para mostrar el archivo comprimido y descomprimido respectivamente.
## Funcionamiento
Para el funcionamiento de este programa, es necesario tener instalada la libreria de tkinter.
Aunque esta libreria deberia instalarse junto con el entorno de desarrollo de python, puedes verificar la instalacion con la siguiente linea en el simbolo del sistema:
```
pip install tk
```
Para poder usar la libreria dentro del programa, se necesita importar con las siguiente lineas:
```
import tkinter as tk
from tkinter import filedialog, ttk
```
La funcion `open_file_dialog():` se encarga de abrir el explorador de archivos, obtener la ruta del archivo esogido y valodar que tenga su extension .txt. Si es el caso habilita los demas botones.
![imagen de la funcion 1](https://i.imgur.com/czaTymC.png)
La funcion `show_file_data():` abre una nueva ventana que mostrara el texto obtenido del archivo, junto con una lista con todos los caracteres encontrados, con la cantidad de veces que se repita cada uno de ellos.
![imagen de la funcion 2](https://i.imgur.com/JN4m0W1.png)
La funcion `show_result_data():` mostrara el archivo de texto una vez sea comprimido.
![Imagen de la funcion 3](https://i.imgur.com/K54DMPC.png)
La funcion `show_main_window():` muestra la ventana principal del programa. Contiene los botones para acceder a las demas ventanas, el selector de archivos, mostrar el contenido del archivo y mostrar la compresion del mismo.
![Imagen de la funcion 4](https://i.imgur.com/rWjX3pq.png)
El resto del programa se encarga de obtener la lista con los caracteres encontrados y su cantidad de veces que aparecen dentro del archivo.
![Imagen de la funcion 5](https://i.imgur.com/H00gxbz.png)
