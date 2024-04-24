# Huffman text compression algorithm
**Algoritmo de Huffman para la compresión de archivos**
## Descripción
El siguiente programa es una interfaz gráfica para un programa de compresión y descompresión de archivos. En este se puede abrir el explorador para escoger un archivo de texto o binario. Permite visualizar el contenido en el archivo, junto con un conteo ordenado de la cantidad y tipo de caracteres dentro de este. También hay un apartado para mostrar el archivo comprimido y descomprimido respectivamente.
## Funcionamiento
Para poder usar la librería dentro del programa, se necesita importar la librería tkinter con las siguiente líneas:
```
import tkinter as tk
from tkinter import filedialog, ttk
```
La función `open_file_dialog():` se encarga de abrir el explorador de archivos, solicitar un archivo de texto o binario y habilitar o deshabilitar los botones necesarios dependiendo del tipo de archivo seleccionado.
![imagen de la función 1](https://i.imgur.com/ltHRagu.png)
La función `show_file_data():` abre una nueva ventana que mostrara el texto obtenido del archivo, junto con una lista con todos los caracteres encontrados, con la cantidad de veces que se repita cada uno de ellos en orden ascendente.
![imagen de la función 2](https://i.imgur.com/KM9mfqz.png)
La función `show_result_data():` mostrara el archivo de texto una vez sea comprimido.
![Imagen de la función 3](https://i.imgur.com/K54DMPC.png)
La función `show_invert_data():` mostrara el archivo de texto una vez sea descomprimido.
![Imagen de la función 4](https://i.imgur.com/Tpp65bX.png)
La función `show_main_window():` muestra la ventana principal del programa. Contiene los botones para acceder a las demás ventanas, el selector de archivos, mostrar el contenido del archivo y mostrar la compresión y descompresión de este.
![Imagen de la función 5](https://i.imgur.com/B7jOLGR.png)
La función `contar_caracteres():` es la encargada de contabilizar cada carácter que haya dentro del archivo de texto, y ordenar el diccionario de caracteres `lista_caracteres`, el cual contiene los caracteres y cantidad de veces que aparecen en el documento.
![Imagen de la función 6](https://i.imgur.com/yJKv60i.png)

## Explicación de uso
El programa inicia con un único botón habilitado, el cual abrirá el explorador de archivos y nos pedirá escoger un archivo de texto o binario.
![Explicación 1](https://i.imgur.com/PykkuuD.png)
Si el archivo tiene la extensión .txt, se habilitarán todos los botones a excepción del botón de descompresión; si el archivo tiene la extensión .bin, se habilitarán todos los botones a excepción del botón de compresión.

Si no se selecciona ningún archivo, todos los botones seguirán deshabilitados.

El botón **Ver contenido del archivo** abrirá una nueva ventana con el contenido del archivo y una lista con el conteo de caracteres.
![Explicación 2](https://i.imgur.com/LYaLf5Q.png)
Tanto el botón **Comprimir archivo** como **Descomprimir archivo** tiene la misma estructura, la cual servirá para mostrar la información necesaria en cada caso.
![Explicación 3](https://i.imgur.com/bD747hB.png)
