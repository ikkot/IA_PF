# IA_PF

El presente proyecto tiene por objetivo obtener a partir de la imagen de un auto, las letras y números de su patente. Para realizarlo se optó por el análisis de cuatro algoritmos para encontrar el que mejor resuelva el problema. Se decidió utilizar el formato de patente argentina de 1994, dado que resulta más sencillo para la obtención del dataset. Aun asi, los resultados se pueden extrapolar hacia el formato de patente del Mercosur introducido en 2015, realizando unas pequeñas modificaciones.

## Ejecucion
Se puede probar el algoritmo pre configurado en el siguiente link [Ejecutar](https://repl.it/@ikkot/IAPF). Sino se puede instalar manualmente teniendo en consideracion lo siguiente.

Este algoritmo fue desarrollado en **Python 3.8.5**. Se requiere su instalacion previa. 
Para probar la versión final del proyecto es necesario ejecutar el archivo `main.sh`, a fin de instalar las librerias necesarias. Luego ejecutar el `script.py`. 
En su ejecución se puede detallar el path para utilizar un dataset personalizado. Este dataset debe estar compuesto por imagen en formato png con una resolución de 59*108 pixeles,  cuyo nombre debe estar compuesto por el resultado seguido de un guión (A_896589.png para un caracter A).

Además, se pueden testear patentes recortadas de la forma siguiente.

![Texto alternativo](/img_test/img_1.jpeg)

Ingresando su path. Por ejemplo `"img_test/img_1.jpeg"`

## Archivos
En el informe llamado `IA_PF.pdf` se explica en primer lugar el funcionamiento de los algoritmos seleccionados, luego se detalla la obtención y tratamiento del dataset. Se presenta un análisis detallado de los resultados de cada algoritmo variando sus parámetros. Luego se detalla el algoritmo a utilizar con sus ajustes de parámetros. Finalmente se presenta una conclusión del proyecto junto a las posibles mejoras y posibilidades de continuidad. 

Se puede observar el dataset utilizado dentro de la carpeta `dataset` y los CSV generados dentro de la carpeta `CSV Finales`.

Se puede observar el notebook generado para la creación de este proyecto llamado `IA_PF.ipynb`. 

<iframe height="400px" width="100%" src="https://repl.it/@ikkot/IAPF?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>



