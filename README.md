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
La funcion `open_file_dialog():` se encarga de abrir el explorador de archivos, obtener la ruta del archivo esogido y valodar que tenga su extension .txt. Si es el caso habilita los demas botones. Tambien se encarga de llamar a la funcion que cuenta los caracteres del archivo.
![imagen de la funcion 1](https://i.imgur.com/OvrQ9Ib.png)
La funcion `show_file_data():` abre una nueva ventana que mostrara el texto obtenido del archivo, junto con una lista con todos los caracteres encontrados, con la cantidad de veces que se repita cada uno de ellos.
![imagen de la funcion 2](https://i.imgur.com/KM9mfqz.png)
La funcion `show_result_data():` mostrara el archivo de texto una vez sea comprimido.
![Imagen de la funcion 3](https://i.imgur.com/K54DMPC.png)
La funcion `show_invert_data():` mostrara el archivo de texto una vez sea descomprimido.
![Imagen de la funcion 4](https://i.imgur.com/Tpp65bX.png)
La funcion `show_main_window():` muestra la ventana principal del programa. Contiene los botones para acceder a las demas ventanas, el selector de archivos, mostrar el contenido del archivo y mostrar la compresion  y descompresion del mismo.
![Imagen de la funcion 5](https://i.imgur.com/B0A1Dub.png)
La funcion `contar_caracteres():` es la encargada de contabilizar cada caracter que haya dentro del archivo de texto.
![Imagen de la funcion 6](https://i.imgur.com/o5gRd2q.png)

## Explicacion de uso
El programa inicia con un unico boton habilitado, el cual abrira el explorador de archivos y nos pedira escoger un archivo txt.
![Explicacion 1](https://i.imgur.com/KGRoUjZ.png)
Si el archivo tiene la extension .txt, se habilitaran los demas botones, de caso contrario seguiran inaccesibles.

El boton **Ver datos del archivo** abrira una nueva ventana con el contenido del archivo y una lista con el conteo de caracteres.
![Explicacion 2](https://i.imgur.com/EDsB70x.png)
Tanto el boton **Comprimir archivo** como **Descomprimir archivo** tiene la misma estructura, la cual servira para mostrar la informacion necesaria en cada caso.
![Explicacion 3](https://i.imgur.com/bD747hB.png)
