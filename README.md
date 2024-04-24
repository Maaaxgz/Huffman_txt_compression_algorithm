# Huffman text compression algorithm
**Algoritmo de Huffman para la compresion de archivos**
## Descripcion
El siguiente programa es una interfaz grafica para un programa de compresion y descompresion de archivos. En este se puede abrir el explorador para escoger un archivo de texto o binario. Permite visualizar el contenido en el archivo, junto con un conteo ordenado de la cantidad y tipo de caracteres dentro de este. Tambien hay un apartado para mostrar el archivo comprimido y descomprimido respectivamente.
## Funcionamiento
Para poder usar la libreria dentro del programa, se necesita importar  la libreria tkinter con las siguiente lineas:
```
import tkinter as tk
from tkinter import filedialog, ttk
```
La funcion `open_file_dialog():` se encarga de abrir el explorador de archivos, solicitar un archivo de texto o binario y habilitar o desabilitar los botones necesarios dependiendo del tipo de archivo seleccionado.
![imagen de la funcion 1](https://i.imgur.com/ltHRagu.png)
La funcion `show_file_data():` abre una nueva ventana que mostrara el texto obtenido del archivo, junto con una lista con todos los caracteres encontrados, con la cantidad de veces que se repita cada uno de ellos en orden ascendente.
![imagen de la funcion 2](https://i.imgur.com/KM9mfqz.png)
La funcion `show_result_data():` mostrara el archivo de texto una vez sea comprimido.
![Imagen de la funcion 3](https://i.imgur.com/K54DMPC.png)
La funcion `show_invert_data():` mostrara el archivo de texto una vez sea descomprimido.
![Imagen de la funcion 4](https://i.imgur.com/Tpp65bX.png)
La funcion `show_main_window():` muestra la ventana principal del programa. Contiene los botones para acceder a las demas ventanas, el selector de archivos, mostrar el contenido del archivo y mostrar la compresion  y descompresion del mismo.
![Imagen de la funcion 5](https://i.imgur.com/B7jOLGR.png)
La funcion `contar_caracteres():` es la encargada de contabilizar cada caracter que haya dentro del archivo de texto, y ordenar el diccionario de caracteres `lista_caracteres`, el cual contiene los caracteres y cantidad de veces que aparecen en el documento.
![Imagen de la funcion 6](https://i.imgur.com/yJKv60i.png)

## Explicacion de uso
El programa inicia con un unico boton habilitado, el cual abrira el explorador de archivos y nos pedira escoger un archivo de texto o binario.
![Explicacion 1](https://i.imgur.com/PykkuuD.png)
Si el archivo tiene la extension .txt, se habilitaran todos los botones a excepcion del boton de descompresion; si el archivo tiene la extension .bin, se habilitaran todos los botones a excepcion del boton de compresion.

Si no se selecciona ningun archivo, todos los botones seguiran deshabilitados.

El boton **Ver contenido del archivo** abrira una nueva ventana con el contenido del archivo y una lista con el conteo de caracteres.
![Explicacion 2](https://i.imgur.com/LYaLf5Q.png)
Tanto el boton **Comprimir archivo** como **Descomprimir archivo** tiene la misma estructura, la cual servira para mostrar la informacion necesaria en cada caso.
![Explicacion 3](https://i.imgur.com/bD747hB.png)
